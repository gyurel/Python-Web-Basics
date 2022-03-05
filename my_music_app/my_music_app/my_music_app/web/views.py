from django.shortcuts import render, redirect

# Create your views here.
from my_music_app.web.forms import CreateProfileForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from my_music_app.web.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]


def home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    albums = Album.objects.all()

    context = {
        'albums': albums,
    }

    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'request':request,
    }

    return render(request, 'home-no-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = AddAlbumForm()

    context = {
        'form': form,
    }

    return render(request, 'add-album.html',context)



def album_details(request, id):
    album = Album.objects.get(id=id)

    context = {
        'album': album,
    }

    return render(request, 'album-details.html', context)


def edit_album(request, id):
    album = Album.objects.get(id=id)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditAlbumForm(instance=album)
    context = {
        'form': form,
    }

    return render(request, 'edit-album.html', context)


def delte_album(request, id):
    album = Album.objects.get(id=id)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
    }

    return render(request, 'delete-album.html', context)


def profile_detalils(request):
    profile = get_profile()
    albums_count = len(Album.objects.all())

    context = {
        'profile': profile,
        'albums_count': albums_count,
    }

    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        form.save()
        return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)
