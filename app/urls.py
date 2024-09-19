from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home_view, name='home'),
    path('customers/', include('customers.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),

    path('api/v1/', include("authentication.urls")),
    path('api/v1/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
