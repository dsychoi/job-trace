from django.urls import path

from .views import HomePageView, ExamplePageView, GetStartedPageView


urlpatterns = [
	path("", HomePageView.as_view(), name="home"),
	path("example/", ExamplePageView.as_view(), name="example"),
	path("get_started", GetStartedPageView.as_view(),name="get_started"),
]