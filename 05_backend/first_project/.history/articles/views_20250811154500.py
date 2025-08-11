from django.shortcuts import render
# django가 가지고 있는 http에 따른 응답 방식
from django.http import JsonResponse
# RESTful한 API를 만들도록 해주는 framework
from rest_framework.decorators import api_view

# Create your views here.
# 행위 -> RESTful API를 위한 것
def index(request):
    # 모든 view 함수는 첫번째 인자 request 고정
        # 물론 인자명 request는 다른 이름이어도 상관은 없지만
        # django의 가이드 상, request이므로, 다른 이름으로 적지 않음
    # 응답: JSON 형태로 Response -> {'message': 'Hello, Django!'}
    return JsonResponse({'message': 'Hello, Django!'})