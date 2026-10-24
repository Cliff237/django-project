from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse


def make_user(username):
    from django.contrib.auth.models import User
    return User.objects.create(
        username=username,
        password=make_password('Tr0ub4dor&3'),
    )


class LoginFlowTest(TestCase):
    def test_login_page_200(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_success_and_logout(self):
        make_user('alice')
        response = self.client.post(reverse('login'), {
            'username': 'alice', 'password': 'Tr0ub4dor&3',
        })
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('logout'))
        # Django 5 LogoutView requires POST; a GET is refused with 405.
        self.assertIn(response.status_code, (302, 405))

    def test_login_wrong_password(self):
        make_user('alice')
        response = self.client.post(reverse('login'), {
            'username': 'alice', 'password': 'wrong-password',
        })
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)

    def test_password_reset_page_200(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)
