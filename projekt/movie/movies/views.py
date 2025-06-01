from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET.get('next') or 'movie_list')
        else:
            return render(request, 'movies/login.html', {'error': 'Nieprawidłowe dane logowania'})
    return render(request, 'movies/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'movies/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
def movie_list(request):
    query = request.GET.get('q')
    director = request.GET.get('director')
    genre = request.GET.get('genre')
    sort_by = request.GET.get('sort', 'title')

    movies = Movie.objects.all()

    if query:
        movies = movies.filter(Q(title__icontains=query))

    if director:
        movies = movies.filter(director__icontains=director)

    if genre:
        movies = movies.filter(genre__icontains=genre)

    if sort_by:
        movies = movies.order_by(sort_by)

    return render(request, 'movies/movie_list.html', {'movies': movies})

@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})

@login_required
def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form})
