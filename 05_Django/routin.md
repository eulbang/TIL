# Django 프로젝트 생성 전 루틴
1. 가상환경(venv) 생성
  - $ python -m venv venv
2. 가상환경 활성화
  - $ source venv/Scripts/activate
3. Django 설치
  - $ pip install django
  - $ pip install ...
4. 의존성 파일 생성
  - $ pip freeze > requirements.txt
- requirements.txt 파일이 생성되어 있거나 가져온 경우
  - $ pip install -r requirements.txt

# Django 프로젝트 생성
- 프로젝트 생성
  - $ django-admin startproject pjt_name .
    - command                / 프로젝트명 / 목표 생성 위치
- 서버 실행
  - $ python manage.py runserver
- 서버 종료
  - ctrl + c
- 어플리케이션 생성
  - $ python manage.py startapp app_name
  - pjt_name/settings.py -> INSTALLED_APPS 리스트에 'app_name', 추가

# APi 작성 순서
0. 설치한 어플, 프레임워크 추가
  - settings.py 리스트에 작성
1. 식별
  - urls.py
  - path('index/', views.index)
    - 경로에 포함된 값을 변수로 받고 싶을 경우
    - 'index/<data_type:variable_name>/'
      - view.py 에서 함수를 정의할 떄 뒤 값도 받아야 함
      - def index(request, variable_name): return JSON
  - path 부분이 index/ 로 이루어진 url 경로로 요청 받았을 때 views 에 있는 index 함수를 실행한다.
2. 행위
  - GET, POST, PUT/PATCH, Create, Read, Update, Delete 등 method
  - views.py
  - RESTful한 API를 만들도록 해주는 framework - RESTful : 규약에 맞는
    - from rest_framework.decorators import api_view
    - @api_view(['GET'])
3. 표현
  - JSON 데이터를 반환
  - views.py
    - from django.http import JsonResponse
    - def index(request): return JsonResponse(data)

# DRF 사용 전 준비
1. 가상환경(venv) 생성
  - $ python -m venv venv
2. 가상환경 활성화
  - $ source venv/Scripts/activate
3. Django 설치
  - $ pip install django
4. DjangoRestFramework 설치
  - $ pip install djangorestframework
5. settings.py 수정
  - pjt_name/settings.py -> INSTALLED_APPS 리스트에 'rest_framework', 추가
6. 의존성 파일 추가
  - $ pip freeze > requirements.txt