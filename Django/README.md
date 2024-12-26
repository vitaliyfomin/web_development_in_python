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
#### Зарегистрируем приложение в project_name/settings.py:
```
INSTALLED_APPS = [
    ...
    'recipes',
]
```