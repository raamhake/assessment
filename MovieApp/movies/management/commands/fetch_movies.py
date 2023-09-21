import requests
import json
from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Fetch movies data from the TMDb API and save it to the database'

    def handle(self, *args, **kwargs):
        api_key = '0aac7868ae95010f90f62f4bbcfc1c64'  # TMDb API key
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            data = response.json()
            movies = data.get('results', [])

            for movie in movies:
                Movie.objects.create(
                    title=movie.get('title', ''),  # Use lowercase 'title'
                    poster=f'https://image.tmdb.org/t/p/w500/{movie.get("poster_path", "")}',
                    genre='Unknown',  # You can add genre logic based on available data
                    rating=float(movie.get('vote_average', 0)),
                    year_release=int(movie.get('release_date', '').split('-')[0]),
                    metacritic_rating=0.0,  # You can add metacritic rating logic
                    runtime=int(movie.get('runtime', 0))
                )
            self.stdout.write(self.style.SUCCESS('Successfully fetched and saved movie data'))
        except requests.exceptions.RequestException as e:
            self.stderr.write(self.style.ERROR(f'Error fetching data: {e}'))
        except json.JSONDecodeError as e:
            self.stderr.write(self.style.ERROR(f'Error decoding JSON data: {e}'))
