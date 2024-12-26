#### Настройка виртуального окружения в VS Code
В терминале VS Code создайте виртуальное окружение для проекта:
```
python -m venv venv
```
#### Активируйте виртуальное окружение:
Выполнение PowerShell-скриптов в системе может быть запрещено политикой безопасности. Проверим и исправим это, командами:
```
Get-ExecutionPolicy
```
Если вывод будет **Restricted**, это означает, что выполнение скриптов запрещено.

Чтобы разрешить выполнение скриптов, выполним следующую команду:
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
*Описание параметров*:

- **Scope CurrentUser**: Изменяет политику только для текущего пользователя.
- **ExecutionPolicy RemoteSigned**: Разрешает локальные скрипты и требует подпись для удалённых.
#### Теперь выполните команду для активации:
```
.\venv\Scripts\Activate.ps1
```
### Установите библиотеку Pillow:

Выполните следующую команду в активированном виртуальном окружении:
```
pip install Pillow
```
#### Проверьте успешность установки:

После установки выполните команду:
```
pip show Pillow
```
#### Устанавливаем Django:
```
pip install django
```
#### Создайте новый проект:
```
django-admin startproject recipes_site .
```
#### Запустите сервер для проверки:
```
python manage.py runserver
```
Перейдём в браузер по адресу http://127.0.0.1:8000, чтобы убедиться, что проект работает.

При запуске серера и переход по адресу http://127.0.0.1:8000 будут ошибки так как не выполнены миграции
```
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```
#### Для начало создадим приложения для рецептов:
```
python manage.py startapp recipes
```
#### Зарегистрируем приложение в **project_name/settings.py*:
```
INSTALLED_APPS = [
    ...
    'recipes',
]
```
### Настройка моделей
#### Добавим следующие модели в **recipes/models.py*:
```
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preparation_steps = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="Time in minutes")
    image = models.ImageField(upload_to='recipes/')
    ingredients = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='recipes')

    def __str__(self):
        return self.title
```
### Создание и выполнение миграций
Создадим миграцию:
```
python manage.py makemigrations
```
Применим миграцию:
```
python manage.py migrate
```
### Создание суперпользователя
Создадим административного пользователя для управления проектом:
```
python manage.py createsuperuser
```
### Настройка админ-панели
Добавим модели в админ-панель *recipes/admin.py*:
```
from django.contrib import admin
from .models import Recipe, Category

admin.site.register(Recipe)
admin.site.register(Category)
```
Перезапустим сервер и зайдём в админ-панель http://127.0.0.1:8000/admin/, чтобы убедиться, что модели доступны.