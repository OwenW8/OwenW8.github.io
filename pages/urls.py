from django.urls import path

from .views import home_page_view, AboutPageView, ContactPageView, ExperiancesPageView, ProjectsPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name = "about"),
    path("", home_page_view, name="home"),
    path("contact/", ContactPageView.as_view(), name = "contact"),
    path("experiance/", ExperiancesPageView.as_view(), name = "experiance"),
    path("projects/", ProjectsPageView.as_view(), name = "projects"),
    
]