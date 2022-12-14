from django.urls import path
from .views import (
	ApplicationListView,
	ApplicationDetailView,
	ApplicationUpdateView,
	ApplicationDeleteView,
	ApplicationCreateView,
)


urlpatterns = [
	path("<int:pk>/", ApplicationDetailView.as_view(), name="application_detail"),
	path("<int:pk>/edit/", ApplicationUpdateView.as_view(), name="application_edit"),
	path("<int:pk>/delete/", ApplicationDeleteView.as_view(), name="application_delete"),
	path("new/", ApplicationCreateView.as_view(), name="application_new"),
	path("", ApplicationListView.as_view(), name="application_list"),
]