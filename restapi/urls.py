from django.urls import path, include
from django.conf import settings
from .views import ProductList, ProductDetail
from django.conf.urls.static import static

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>', ProductDetail.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)