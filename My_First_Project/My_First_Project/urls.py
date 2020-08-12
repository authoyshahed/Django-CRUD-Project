from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_app.urls')),
    # path('',views.home,name='home'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
]
