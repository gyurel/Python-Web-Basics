from django.urls import path

from employees_app.employees.views import department_details, list_departments

urlpatterns = (
    path('<int:id>/', department_details),
    path('', list_departments),
    # path('create/', create_department),
    # path('update/', update_department),
    # path('delete/', delete_department)
)