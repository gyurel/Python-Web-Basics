from django.urls import path

from my_music_app.web.views import home_page, add_album, album_details, edit_album, delte_album, profile_detalils, \
    delete_profile, create_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:id>/',album_details, name='album details'),
    path('album/edit/<int:id>/', edit_album, name='edit album'),
    path('album/delete/<int:id>/', delte_album, name='delete album'),
    path('profile/details/', profile_detalils, name='profile details'),
    path('profile/delete/', delete_profile, name='profile delete'),
    path('profile/create/', create_profile, name='create profile'),
)