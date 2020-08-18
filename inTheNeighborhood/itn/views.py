from django.shortcuts import render, HttpResponse, redirect
from .models import Artist, Restaurant, BeautyBrand, Book, Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#just to see server
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def resources(request):
    return render(request, "resources.html")

def books(request):
    context = {
        'books': Book.objects.all(),
        'articles': Article.objects.all()
    }
    return render(request, "books.html", context)

def beautyBrands(request):
    context = {
        'brands': BeautyBrand.objects.all()
    }
    return render(request, "beauty_brands.html", context)

def donate(request):
    return render(request, "donate.html")

def localArtists(request):
    context = {
        'artists': Artist.objects.all()
    }
    return render(request, "local_artists.html", context)

def restaurants(request):
    context = {
        'restaurants': Restaurant.objects.all()
    }
    return render(request, "restaurants.html", context)

def products_services(request):
    return render(request, "products_services.html")

@login_required
def new_artist(request):
    return render(request, "new_artist.html")

@login_required
def new_restaurant(request):
    return render(request, "new_restaurant.html")

@login_required
def new_beauty(request):
    return render(request, "new_beauty.html")

@login_required
def new_book(request):
    return render(request, "new_book.html")

@login_required
def new_article(request):
    return render(request, "new_article.html")

def create_artist(request):
    if request.method == 'POST':
        errors = Artist.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/new-artist')
        else:
            Artist.objects.create(
                name = request.POST['name'],
                category = request.POST['category'],
                photo = request.POST['photo'],
                link = request.POST['link']
            )
            return redirect('/local-artists')

def create_restaurant(request):
    if request.method == 'POST':
        errors = Restaurant.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/new-restaurant')
        else:
            Restaurant.objects.create(
                name = request.POST['name'],
                category = request.POST['category'],
                description = request.POST['description'],
                photo = request.POST['photo'],
                link = request.POST['link']
            )
            return redirect('/restaurants')

def create_beauty(request):
    if request.method == 'POST':
        errors = BeautyBrand.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/new-beauty')
        else:
            BeautyBrand.objects.create(
                name = request.POST['name'],
                category = request.POST['category'],
                photo = request.POST['photo'],
                link = request.POST['link']
            )
            return redirect('/beauty-brands')

def create_book(request):
    if request.method == 'POST':
        errors = Book.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/new-book')
        else:
            Book.objects.create(
                title = request.POST['title'],
                author = request.POST['author'],
                category = request.POST['category'],
                publisher = request.POST['publisher'],
                description = request.POST['description'],
                photo = request.POST['photo'],
                link = request.POST['link']
            )
            return redirect('/books-articles')

def create_article(request):
    if request.method == 'POST':
        errors = Article.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/new-article')
        else:
            Article.objects.create(
                title = request.POST['title'],
                author = request.POST['author'],
                link = request.POST['link']
            )
            return redirect('/books-articles')