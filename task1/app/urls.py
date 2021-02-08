from django.contrib import admin
from django.urls import path

from .views import inflation_view

urlpatterns = [
    path('', inflation_view, name='main'),
    # path('index/', index_view, name='index'),
    path('admin/', admin.site.urls),
    # path('hello/<name>', view_hello, name='hello')
]
