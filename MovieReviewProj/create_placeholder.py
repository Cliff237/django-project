
import os
from pathlib import Path

# Create directories if they don't exist
media_path = Path('media/movie_posters')
media_path.mkdir(parents=True, exist_ok=True)

# List of movies that match your fixture data
movies = ['inception', 'shawshank', 'dark_knight', 'stranger_things', 'irishman', 'shrek', 'endgame']

print("Creating placeholder text files...")

for movie in movies:
    # Create a simple text file as placeholder
    output_path = f'media/movie_posters/{movie}.jpg.txt'
    with open(output_path, 'w') as f:
        f.write(f"Placeholder for {movie} poster\n")
        f.write("Upload a real poster image here")
    print(f'✓ Created placeholder for: {movie}')

print("\n⚠️  Note: These are text files, not actual images.")
print("You'll need to upload real poster images through Django admin.")
