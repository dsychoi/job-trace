from django.contrib import admin
from django.urls import path, include


urlpatterns = [
	path("admin/", admin.site.urls),
	path("accounts/", include("accounts.urls")),  # new
	path("accounts/", include("django.contrib.auth.urls")),  # new
	path("applications/", include("applications.urls")),
	path("", include("contact.urls")),
	path("", include("pages.urls")),
]
