from django.urls import path, include
from . import views

urlpatterns = [
  path('create/', views.create, name='create'),
  path('<int:product_id>', views.detail, name='detail'),
  path('<int:product_id>/upvote', views.upvote, name='upvote'),
  path('contact/', views.contact, name='contact'),
  path('about/', views.about, name='about'),
  path('<int:mob_id>/',views.detail_view, name="detail_view"),

]
