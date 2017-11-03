"""game_catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url

from catalog.views.rest_view import rest_category_view,\
    rest_esrb_view,\
    rest_game_view,\
    rest_platform_view,\
    rest_genre_view

urlpatterns = [
    url(r'catalog/', include('catalog.urls')),
    url(
        r'rest-category-list/',
        rest_category_view.category_list
    ),
    url(
        r'rest-esrb-list/',
        rest_esrb_view.esrb_list
    ),
    url(
        r'rest-genre-list/',
        rest_genre_view.genre_list
    ),
    url(
        r'rest-platform-list/',
        rest_platform_view.platform_list
    ),
    url(
        r'rest-game-list/',
        rest_game_view.game_list
    ),
    path('admin/', admin.site.urls),
]
