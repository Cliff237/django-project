document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const genreFilter = document.getElementById('genre-filter');
    const typeFilter = document.getElementById('type-filter');
    const movieGrid = document.getElementById('movie-grid');
    const resetBtn = document.getElementById('reset-btn');

    if (!searchInput || !genreFilter || !typeFilter || !movieGrid) {
        console.error('❌ Some filter elements are missing. Check your HTML.');
        return;
    }

    function filterMovies() {
        const searchTerm = searchInput.value.toLowerCase().trim();
        const selectedGenre = genreFilter.value;
        const selectedType = typeFilter.value;

        const cards = movieGrid.querySelectorAll('.movie-card');
        let visibleCount = 0;

        cards.forEach(card => {
            const title = (card.dataset.title || '').toLowerCase();
            const type = card.dataset.type || '';
            const genres = card.dataset.genres ? card.dataset.genres.split(',') : [];

            const matchSearch = !searchTerm || title.includes(searchTerm);
            const matchGenre = !selectedGenre || genres.includes(selectedGenre);
            const matchType = !selectedType || type === selectedType;

            if (matchSearch && matchGenre && matchType) {
                card.style.display = 'block';
                visibleCount++;
            } else {
                card.style.display = 'none';
            }
        });

        // No results message
        let noMsg = document.getElementById('no-results');
        if (visibleCount === 0 && cards.length > 0) {
            if (!noMsg) {
                noMsg = document.createElement('p');
                noMsg.id = 'no-results';
                noMsg.style.gridColumn = '1 / -1';
                noMsg.style.textAlign = 'center';
                noMsg.style.color = '#888';
                noMsg.style.padding = '50px 0';
                noMsg.textContent = 'No movies match your filters.';
                movieGrid.appendChild(noMsg);
            }
        } else if (noMsg) {
            noMsg.remove();
        }
    }

    // Live filtering
    searchInput.addEventListener('input', filterMovies);
    genreFilter.addEventListener('change', filterMovies);
    typeFilter.addEventListener('change', filterMovies);

    // Reset button
    if (resetBtn) {
        resetBtn.addEventListener('click', function () {
            searchInput.value = '';
            genreFilter.value = '';
            typeFilter.value = '';
            filterMovies();
            searchInput.focus();
        });
    }

    // Initial run
    filterMovies();

    console.log('%c✅ CineRate - Live filter loaded successfully!', 'color:#00f7ff; font-size:16px;');
});