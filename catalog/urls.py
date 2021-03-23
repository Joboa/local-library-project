from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my_borrowed'),
    path('book_details', views.BookDetailView.as_view(), name='book-detail')
]