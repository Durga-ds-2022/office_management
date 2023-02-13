from django.urls import path
from .views import *
urlpatterns = [
    path('home/', home, name='home'),
    path('add_emp/', add_emp, name='add_emp'),
    path('all_emp/', all_emp, name='all_emp'),
    path('remove_emp/', remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>/', remove_emp, name='remove_emp'),
    path('update_emp/<int:emp_id>/', update_emp, name='update_emp'),
    path('filter_emp/', filter_emp, name='filter_emp'),

]
