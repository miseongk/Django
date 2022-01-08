# Django
1. [Django 프로젝트 시작하기](#Django-프로젝트-시작하기)
## Django 프로젝트 시작하기
**프로젝트 만들기**
```shell
$> django-admin startproject <프로젝트명>
```
- 프로젝트 디렉토리 생성
```
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
- 서버 실행
```shell
$> python manage.py runserver
```
---
**앱 만들기**
```shell
&> django-admin startapp <앱명>
```
- 앱 디렉토리 생성
```
myapp/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
---
**프로젝트 파일구조**
```
myproject/
    manage.py
    pipfile
    pipfile.lock
    myproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    myapp/
      __init__.py
      admin.py
      apps.py
      migrations/
          __init__.py
      models.py
      tests.py
      views.py
```
            
