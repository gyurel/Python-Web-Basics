from django.shortcuts import render, redirect

# Create your views here.
from online_library.register_app.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, AddBookForm, \
    EditBookForm
from online_library.register_app.models import Profile, Book


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    books = Book.objects.all()

    context = {
        'books': books,
        'profile': profile,
    }

    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'request': request,
        'profile': profile,
    }

    return render(request, 'home-no-profile.html', context)


def profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home page')
    else:
        form = AddBookForm()

    context = {
        'form': form,
    }

    return render(request, 'add-book.html', context)


def book_details(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book,
    }

    return render(request, 'book-details.html', context)


def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditBookForm(instance=book)

    context = {
        'form': form,
    }

    return render(request, 'edit-book.html', context)


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()

    return redirect('home page')
