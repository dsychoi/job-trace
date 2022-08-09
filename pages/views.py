from django.views.generic import TemplateView


class HomePageView(TemplateView):
	template_name = "home.html"


class ExamplePageView(TemplateView):
	template_name = "example.html"


class GetStartedPageView(TemplateView):
	template_name = "get_started.html"