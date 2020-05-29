from django.urls import path, include
from .views import homePageView, HomePage, AboutPage

urlpatterns = [
    # path('',homePageView,name="home"),
    path('',HomePage.as_view(),name="home"),
    path('about/',AboutPage.as_view(),name="about")
]