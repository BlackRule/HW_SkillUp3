from django.urls import path, include

from blog.views import home_page_view

urlpatterns = [
    path('', home_page_view),
]
