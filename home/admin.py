from django.contrib import admin
from .models import Recipes

class RecipesAdmin(admin.ModelAdmin):
    list_display = ("name", "type",)

admin.site.register(Recipes, RecipesAdmin)
