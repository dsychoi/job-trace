from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Application


class ApplicationListView(ListView):
	model = Application
	template_name = "application_list.html"


class ApplicationDetailView(DetailView):
	model = Application
	template_name = "application_detail.html"


class ApplicationUpdateView(UpdateView):
	model = Application
	fields = (
		"company_name",
		"status",
	)
	template_name = "application_edit.html"


class ApplicationDeleteView(DeleteView):
	model = Application
	template_name = "application_delete.html"
	success_url = reverse_lazy("application_list")