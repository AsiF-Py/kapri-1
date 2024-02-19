"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from show.views import home
from sponsor.views import create_subscribe
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about/',TemplateView.as_view(template_name='about.html')),
    path('contact/',TemplateView.as_view(template_name='contact.html')),
    path('faq/',TemplateView.as_view(template_name='faq.html')),
    
    path('',home,name='home'),
    path('',home,name='home'),
    
    path('subscribe/',create_subscribe,name='home'),
    path('blog/',include('blog.urls')),
    path('show/',include('show.urls')),
    path('sponsor/',include('sponsor.urls')),
    path('ms58303002.txt', read_file),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def read_file(request):
    f = open('ms58303002.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
