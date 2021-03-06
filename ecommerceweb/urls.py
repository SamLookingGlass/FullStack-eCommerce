"""ecommerceweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static 
from django.conf import settings 
# from accounts.views import login, logout, register, profile
from cart.views import CartView


# Include all app urls here
urlpatterns = [
    #Django Admin Access
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    # Using namespace to cluster all products.urls, contains homepage
    path('', include('products.urls', namespace='mainapp')), 

    # Using namespace to cluster all accounts.urls, contains account functions
    path('account/', include('accounts.urls', namespace='accounts')),
    # Reset Functionalities
    path('account/', include('django.contrib.auth.urls')), 

    # Path for carts
    path('cart/', include('cart.urls', namespace='cart')),
    # Path for checkout
    path('checkout/', include('checkout.urls', namespace='checkout')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

