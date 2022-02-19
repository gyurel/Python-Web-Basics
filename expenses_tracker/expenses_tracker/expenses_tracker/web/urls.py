from django.urls import path

urlpatterns = (
    path('', show_index, name='home page'),
    path('expense/create/', create_expense, name='create expense'),
    path('edit/<id:pk>/', edit_expense, name='edit expense'),
    path('delete/<id:pk>/', delete_expense, name='delete expense'),
    path('profile/', show_profile, name='profile'),
    path('profileedit//', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)