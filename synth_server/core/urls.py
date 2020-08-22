from django.urls import path
from core.views import show_main_page, create_line, delete_line, edit_line, stop_line, AJAX_test, refresh_page

urlpatterns = [
    path('', show_main_page, name='show_main_page'),
    path('create_page/', create_line, name='create_line'),
    path('delete_page/', delete_line, name='delete_line'),
    path('edit_page/', edit_line, name='edit_line'),
    path('stop_page/', stop_line, name='stop_line'),
    path('test/', AJAX_test),
    path('refresh_page/', refresh_page, name='refresh_page')
]