"""
URL configuration for first_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# articles app이 가지고 있는 views 모듈
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 사용자가 index 라는 경로로 요청을 보내면?
        # 상대 경로
    # views에 있는 index 함수를 실행시킨다.
    path('index/', views.index),
    # varibale routing
    # 경로에 사용자가 적은 값을 변수에 담고 싶어
        # <변수명> -> 여기에 정수만 허용하고 싶어
    # path('article/<variable_name>/', views.detail)
    # path('article/<int:variable_name>/', views.detail)
    path('article/<int:artivle_pk>/', views.detail)
]
