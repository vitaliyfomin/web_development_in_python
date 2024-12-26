from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_steps', 'cooking_time', 'image', 'ingredients', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
        }
