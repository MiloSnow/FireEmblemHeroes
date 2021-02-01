"""miSitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

urlpatterns = [
  	path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('social-auth/', include('social_django.urls',namespace="social")),
    path('', include('pwa.urls')),
]

urlpatterns += [
   path('accounts/', include('django.contrib.auth.urls')),    
]

LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = [
    'social.core.backends.facebook.FacebookOMuth2',
    'django.contrib.auth.backends.ModelBackend',
]

PWA_APP_NAME = "EJEMPLOCLASE"
PWA_APP_DESCRIPTION = "PAGINA QUE NO ES DE JUEGO"
PWA_APP_THEME_COLOR = "#FE350A"
PWA_APP_BACKGROUND_COLOR = "#45FE0A"

#Android
PWA_APP_ICONS =[
    {
        "scr": "/",
        "sizes":"160x160"
    }
]

#Apple
PWA_APP_ICONS_APPLE =[
    {
        "scr": "/",
        "sizes":"160x160"
    }
]



