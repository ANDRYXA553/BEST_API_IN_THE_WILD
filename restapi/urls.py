from django.urls import path, include
from django.conf import settings
from .views import ProductList, ProductDetail, CategoryList
from django.conf.urls.static import static

urlpatterns = [
    path('api/v1/', ProductList.as_view()),
    path('api/v1/<slug:category_slug>/<slug:product_slug>', ProductDetail.as_view()),
    path('api/v1/<slug:category_slug>/', CategoryList.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)