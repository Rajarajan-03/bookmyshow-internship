from django.urls import path
from .views import movie_list, movie_timing, theater_list, book_seats, reservation_payment_page, timeout_page,about,contact
urlpatterns=[
    path('',movie_list,name='movie_list'),
    path('<int:movie_id>/theaters',theater_list,name='theater_list'),
    path('theater/<int:theater_id>/seats/book/',book_seats,name='book_seats'),
    path('movie/<int:movie_id>/', movie_timing, name='movie_timing'),
    path('about/', about,name='about'),
    path('contact/',contact,name='contact'),
    path('payment/<str:seat_ids>/', reservation_payment_page, name='reservation_payment_page'),
    path('timeout/',timeout_page,name='payment_timeout')
]