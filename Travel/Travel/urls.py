"""Travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import places.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',places.views.home,name='home'),
    path('',places.views.first,name='first'),
    path('orders/',places.views.orders , name='orders'),
    path('edit/<int:pk>',places.views.edit_order,name='edit_order'),
    path('catalog/',places.views.catalog,name='catalog'),
    path('cat/<int:cat_id>',places.views.catdetails,name='catdetails'),
    path('register/',places.views.registerPage,name='register'),
    path('login/',places.views.login,name='login'),
    path('history/',places.views.history,name='history'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
