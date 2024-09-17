from django.contrib import admin
from django.urls import include, path

from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home_view, name='home'),
    path('customers/', include('customers.urls')),
]
