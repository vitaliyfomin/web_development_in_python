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
```
source venv/bin/activate
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

#### Установите модуль dotenv:
```
pip install python-dotenv
```
### Создайте папку для записи логов:
web_development_in_python\Django\project_django\logs\

#### Создайте файл .env (там где находится файл manage.py)
В файл .env добавьте:
```
SECRET_KEY= ключ можно сгенерировать на сайте gjecrety.ir
DEBUG=True

```

#### Создайте новый проект:
```
django-admin startproject recipes_site .
```
#### Запустите сервер для проверки:
```
python manage.py runserver
```
```
python manage.py runserver 0.0.0.0:8000
```
Перейдём в браузер по адресу http://127.0.0.1:8000, чтобы убедиться, что проект работает.

При запуске серера и переход по адресу http://127.0.0.1:8000 будут ошибки так как не выполнены миграции
```
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```
### Создание и выполнение миграций
Создадим миграцию:
Сначало удалите содержимое папки *recipebookapp\migrations* оставьте только файл __init__.py
Так же рекомендуется удалить файл *db.sqlite3* который находится рядом с файлом *manage.py*
Теперь можно запускать комманды:
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
