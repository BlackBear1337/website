from django.urls import path

from .views import index, create, edit, details, delete, adminpanel, comment

app_name = 'demo'

urlpatterns = [
    path('', index, name='index'),
    path('adminpanel/', adminpanel, name='adminpanel'),
    path('create/', create, name='create'),
    path('edit/<int:pk>', edit, name='edit'),
    path('details/<int:pk>/', details, name='details'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('comment/<int:pk>', comment, name='comment')
]
