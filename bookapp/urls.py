from django.urls import  path

from bookapp.views import HomePage

urlpatterns = [
    (path("",HomePage.as_view(),name="home")),
]