from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Application


class ApplicationListView(LoginRequiredMixin, ListView):
	model = Application
	template_name = "application_list.html"


class ApplicationDetailView(LoginRequiredMixin, DetailView):
	model = Application
	template_name = "application_detail.html"


class ApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Application
	fields = (
		"company_name",
		"status",
	)
	template_name = "application_edit.html"

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user


class ApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Application
	template_name = "application_delete.html"
	success_url = reverse_lazy("application_list")

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user

class ApplicationCreateView(LoginRequiredMixin, CreateView):
	model = Application
	template_name = "application_new.html"
	fields = (
		"company_name",
		"status",
	)

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)