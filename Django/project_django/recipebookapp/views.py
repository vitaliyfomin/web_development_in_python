from random import randint
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from functools import wraps
import logging

from .forms import SignInForm, SignUpForm, RecipeForm
from .models import Recipe

logger = logging.getLogger(__name__)

def log_this(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        logger.info(f'Func "{f.__name__}" was called')
        return res
    return wrapper

def get_random_recipe():
    queryset = Recipe.objects.filter(is_visible=True)
    count = queryset.count()
    if count == 0:
        return None
    random_index = randint(0, count - 1)
    return queryset[random_index]

@log_this
def index(request):
    number_of_cards = 8
    recipes = list(Recipe.objects.filter(is_visible=True).order_by('?')[:number_of_cards])
    return render(request, "recipebookapp/index.html", {'recipes': recipes})

@log_this
def user(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            reg_form = SignUpForm(request.POST)
            if reg_form.is_valid():
                reg_form.save()
                email = reg_form.cleaned_data['email']
                password = reg_form.cleaned_data['password1']
                user = authenticate(request, email=email, password=password)
                login(request, user)
                return redirect('/cooker')
            else:
                messages.error(request, 'Форма регистрации заполнена неверно')
        elif 'login' in request.POST:
            login_form = SignInForm(request.POST)
            if login_form.is_valid():
                if user := authenticate(request, **login_form.cleaned_data):
                    login(request, user)
                    return redirect('/cooker')
                messages.error(request, 'Ошибка авторизации')
            else:
                messages.error(request, 'Форма авторизации заполнена неверно')

    reg_form = SignUpForm()
    login_form = SignInForm()

    context = {
        'reg_form': reg_form,
        'login_form': login_form
    }
    return render(request, 'recipebookapp/user.html', context)

@log_this
@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

@log_this
@login_required
def cooker(request):
    recipes = Recipe.objects.filter(is_visible=True, author=request.user)
    return render(request, "recipebookapp/cooker.html", {'recipes': recipes})

@log_this
@login_required
def recipe_add(request):
    is_completed = False
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.author = request.user
            form.save()
            is_completed = True
    else:
        form = RecipeForm()
    return render(request, 'recipebookapp/recipe_add.html',
                  {'form': form, 'is_completed': is_completed})

@log_this
@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user != recipe.author:
        return redirect('/')
    
    is_completed = False
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            is_completed = True
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipebookapp/recipe_edit.html',
                  {'form': form, 'is_completed': is_completed, 'recipe_img': recipe.image})

@log_this
@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user != recipe.author:
        return redirect('/')
    
    recipe.delete()
    return redirect('/cooker')

@log_this
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipebookapp/recipe_detail.html', context)

@log_this
def handler404(request, exception):
    return render(request, '404.html', status=404)

@log_this
def handler500(request):
    return render(request, '500.html', status=500)
