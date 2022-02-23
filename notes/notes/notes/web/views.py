from django.shortcuts import render, redirect

# Create your views here.
from notes.web.forms import CreateProfileForm, CreateNoteForm, EditNoteForm
from notes.web.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    notes = Note.objects.all()

    context = {
        'notes': notes,
        'add_note_menu': True,
        'profile_menu': True,
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()

        context = {
            'form': form,
            'add_note_menu': False,
            'profile_menu': False,
        }

        return render(request, 'home-no-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateNoteForm()

    context = {
        'form': form,
        'profile_menu': True,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        form.save()

        return redirect('home page')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
        'add_note_menu': True,
        'profile_menu': True,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request):
    pass


def note_details(request):
    pass


def profile(request):
    pass

