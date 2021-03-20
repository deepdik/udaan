from django.conf.urls import include, url

from dukaan.views import api_root


urlpatterns = [
    url(r'^$', api_root, name='api_root'),
    url(r'^', include('dukaan.apps.store.routers')),
    url(r'^', include('dukaan.apps.users.routers')),
    url(r'^', include('dukaan.apps.products.routers')),
    url(r'^', include('dukaan.apps.orders.routers')),
    url(r'^', include('dukaan.apps.udaan_app.routers')),

]