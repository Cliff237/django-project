// Movie Detail Page Interactions

document.addEventListener('DOMContentLoaded', function() {
    // Show/Hide Review Form
    const showFormBtn = document.getElementById('show-review-form');
    const reviewFormContainer = document.getElementById('review-form-container');
    const cancelBtn = document.getElementById('cancel-review-btn');
    const deleteBtn = document.getElementById('delete-review-btn');
    const deleteForm = document.getElementById('delete-review-form');
    
    if (showFormBtn && reviewFormContainer) {
        showFormBtn.addEventListener('click', function() {
            if (reviewFormContainer.style.display === 'none') {
                reviewFormContainer.style.display = 'block';
                reviewFormContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
                showFormBtn.textContent = 'Hide Review Form';
                showFormBtn.innerHTML = '<i class="fas fa-times"></i> Hide Review Form';
            } else {
                reviewFormContainer.style.display = 'none';
                showFormBtn.textContent = 'Write a Review';
                showFormBtn.innerHTML = '<i class="fas fa-pen"></i> Write a Review';
            }
        });
    }
    
    // Cancel button
    if (cancelBtn && reviewFormContainer && showFormBtn) {
        cancelBtn.addEventListener('click', function() {
            reviewFormContainer.style.display = 'none';
            showFormBtn.textContent = 'Write a Review';
            showFormBtn.innerHTML = '<i class="fas fa-pen"></i> Write a Review';
        });
    }
    
    // Delete review confirmation
    if (deleteBtn && deleteForm) {
        deleteBtn.addEventListener('click', function() {
            if (confirm('Are you sure you want to delete your review? This action cannot be undone.')) {
                deleteForm.submit();
            }
        });
    }
    
    // Animate rating bars when they come into view
    const bars = document.querySelectorAll('.bar');
    if (bars.length) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const bar = entry.target;
                    const width = bar.style.width;
                    bar.style.width = '0';
                    setTimeout(() => {
                        bar.style.width = width;
                    }, 100);
                    observer.unobserve(bar);
                }
            });
        });
        
        bars.forEach(bar => observer.observe(bar));
    }
    
    // Star rating hover effect enhancement
    const starInputs = document.querySelectorAll('.star-rating input');
    starInputs.forEach(input => {
        input.addEventListener('change', function() {
            const rating = this.value;
            console.log(`Rating selected: ${rating} stars`);
        });
    });
});