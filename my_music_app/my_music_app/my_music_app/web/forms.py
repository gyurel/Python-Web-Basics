from django import forms

from my_music_app.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


# class DeleteAlbumForm(forms.ModelForm):
#     class Meta:
#         model = Album
#         fields = '__all__'


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        Album.objects.all().delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()
