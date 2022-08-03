from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('add_post/', views.add_post, name='add_post'),
    path('update_post/<int:id>/', views.update_post, name='update_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
]