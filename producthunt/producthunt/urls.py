"""producthunt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('about/', include('products.urls')),
    path('contact/', include('products.urls')),
    path('mobile/', views.mobile, name='mobile'),
    path('people/', views.people, name='people'),
    path('sucess/', views.sucess, name='sucess'),
    path('admit_card/', views.admit_card, name='admit_card'),
    path('thankyou/', views.thankyou, name='thankyou'),



]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
