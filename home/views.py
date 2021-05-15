from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
        )

from .models import Recipes

class PostListView(ListView):
    model = Recipes
    template_name = 'home/home.html'
    context_object_name = 'items'
    ordering = ['add_date']
    paginate_by = 20

class TypePostListView(ListView):
    model = Recipes
    template_name = 'home/recipes_type.html'

    def get_queryset(self):
        query = Recipes.objects.all().filter(type=type)
        object_list = Recipes.objects.filter(Q(type__icontains=query))
        return object_list

class PostDetailView(DetailView):
    model = Recipes

class PostCreateView(CreateView):
    model = Recipes
    fields = ['name', 'ingredients', 'description', 'type', 'rating', 'image']

    def form_valid(self, form):
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Recipes
    fields = ['name', 'ingredients', 'description', 'type', 'rating', 'image']

    def form_valid(self, form):
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Recipes
    success_url = '/home/'

class SearchResultView(ListView):
    model = Recipes
    template_name = 'home/recipes_search.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =  Recipes.objects.filter(Q(name__icontains=query))
        return object_list

