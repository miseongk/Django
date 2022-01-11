# Django
1. [Django 프로젝트 시작하기](#Django-프로젝트-시작하기)
2. [ORM](#ORM)
3. [Django REST Framework](#Django-REST-Framework)
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
> serializers.py 추가 -> DRF를 사용하기 위해서 따로 생성

> urls.py -> app단위로 분리해서 url을 정의하고, 프로젝트의 urls.py에서 한번에 import하는 방식으로 설계하기 위해 따로 생성
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
 ## ORM         
 [공식문서(모델)](https://docs.djangoproject.com/ko/4.0/topics/db/models/)  
 [공식문서(Model field reference)](https://docs.djangoproject.com/ko/4.0/ref/models/fields/)
 [공식문서(쿼리)](https://docs.djangoproject.com/ko/4.0/topics/db/queries/)
### 필드
```python
# models.py
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```
---
### 관계
**Many-to-one relationships**
```python
class Manufacturer(models.Model):
    # ...
    pass
class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...
```
**Many-to-many relationships**
```python
class Topping(models.Model):
    # ...
    pass
class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)
```
- 다대다(many-to-many)관계를 정의하기 위해서 ManyToManyField 사용
- 예를들어, Pizza가 여러개의 Topping objects를 가질 수 있고, 하나의 Topping이 여러개의 Pizza 위에 올려질 수 있음.
```python
class Person(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    def __str__(self):
        return self.name
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
```
- 데이터(Membership)를 두 모델(Person, Group) 간의 관계와 연결
- through 인수를 사용하여 연결

## Django REST Framework
```shell
$> pipenv install django-rest-framework
```
- django-rest-framework 설치하기
```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework', # 추가
]
```
### Serializer
- JSON에서 Django 모델로, Django 모델에서 JSON으로 변환시켜주는 역할
```python
# models.py

class Student(models.Model):
	name = models.CharField(max_length=128)
	age = models.IntegerField()
	is_male = models.BooleanField()
```
```python
# serializers.py

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'
```

### API view
```python
# views.py

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class StudentListCreateAPIView(ListCreateAPIView):
	serializer_class = StudentSerializer
	queryset = Student.objects.all()
	
class StudentRetrieveUpdateDestroyAPIVIew(RetrieveUpdateDestroyAPIView):
	serializer_class = StudentSerializer
	queryset = Student.objects.all()
	lookup_url_kwarg = 'student_pk'
```
```python
# urls.py in app

from django.urls import path

from .views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIVIew

urlpatterns = [
    path('student/', StudentListCreateAPIView.as_view()),
    path('student/<student_pk>', StudentRetrieveUpdateDestroyAPIVIew.as_view())
]
```
- url 연결
- GET / POST student  
- PATCH / DELETE / PUT student/{student_pk}