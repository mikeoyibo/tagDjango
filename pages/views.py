from django.shortcuts import render

from django.views.generic import ListView

# from django.views.generic import TemplateView, ListView

from .models import Post

# Create your views here.


# class HomePageView(TemplateView):

#     template_name = "home.html"


# class AboutPageView(TemplateView):
#     template_name = "about.html"


class HomePageView(ListView):
    model = Post
    template_name = "home.html"
