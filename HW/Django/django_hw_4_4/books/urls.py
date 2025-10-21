from django.urls import path
from .views import BookListView, BorrowBookView

urlpatterns = [
    path('api/', BookListView.as_view(), name='book-list'),
    path('api/borrow/<str:isbn>/', BorrowBookView.as_view(), name='borrow-book'),
]