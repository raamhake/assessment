from django.shortcuts import render
from .models import Movie
from .models import MovieSchedule

def movie_list(request):
    movies = Movie.objects.all()

    # Filtering by Genre
    selected_genres = request.GET.getlist('genre')
    if selected_genres:
        movies = movies.filter(genre__in=selected_genres)

    # Searching by Title
    search_query = request.GET.get('title')
    if search_query:
        movies = movies.filter(title__icontains=search_query)

    context = {
        'movies': movies,
        'selected_genres': selected_genres,
        'search_query': search_query,
    }
    return render(request, 'movies/movie_list.html', context)





def movie_schedule(request):
    # Fetch movie schedule data and group movies by date
    schedule = MovieSchedule.objects.select_related('movie').order_by('date')
    schedule_by_date = {}
    for item in schedule:
        date = item.date
        if date not in schedule_by_date:
            schedule_by_date[date] = []
        schedule_by_date[date].append(item.movie)

    context = {
        'schedule_by_date': schedule_by_date,
    }
    return render(request, 'movies/movie_schedule.html', context)