"""
URL configuration for djangoTravlr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from main.views import HtmlView

urlpatterns = [
    path("", HtmlView.as_view(template_name="index.html", title="Home"), name="home"),
    path("index/", HtmlView.as_view(template_name="index.html", title="Home"), name="index"),
    path("about/", HtmlView.as_view(template_name="about.html", title="About"), name="about"),
    path("contact/", HtmlView.as_view(template_name="contact.html", title="Contact"), name="contact"),
    path("meals/", HtmlView.as_view(template_name="meals.html", title="Meals"), name="meals"),
    path("news/", HtmlView.as_view(template_name="news.html", title="News"), name="news"),
    path("rooms/", HtmlView.as_view(template_name="rooms.html", title="Rooms"), name="rooms"),
    path("travel/", HtmlView.as_view(template_name="travel.html", title="Travel"), name="travel"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
