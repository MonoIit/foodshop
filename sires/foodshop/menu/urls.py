from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', RedirectView.as_view(url='/shop/', permanent=False)),
    path('shop/', views.show_shop, name='shop'),
    path('shop/<slug:cat_slug>/', views.products_by_category, name='products_by_category'),
    path('delivery/', views.delivery, name='delivery'),
    path('blog/', views.blogs, name='blogs'),
    path('organic/', views.organic, name='organic'),
    path('offers/', views.offers, name='offers'),
    path('sales/', views.sales, name='sales'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)