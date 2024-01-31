from django.urls import path
from . import views
urlpatterns = [
    path('sizes/', views.SizeListCreateView.as_view()),
    path('sizes/<int:pk>', views.SizeRetrieveUpdateDestroyAPIView.as_view()),

    path('locations/', views.LocationListCreateView.as_view()),
    path('locations/<int:pk>', views.LocationRetrieveUpdateDestroyAPIView.as_view()),

    path('spaces/', views.ParkingSpaceListCreateView.as_view()),
    path('spaces/<int:pk>',
         views.ParkingSpaceRetrieveUpdateDestroyAPIView.as_view()),
    path('pricerate/', views.PriceRateListCreateView.as_view()),
    path('pricerate/<int:pk>',
         views.PriceRateRetrieveUpdateDestroyAPIView.as_view()),

    path('receipts/', views.ReceiptListCreateView.as_view()),
    path('receipts/<int:pk>',
         views.ReceiptRetrieveUpdateDestroyAPIView.as_view()),

    path('reservations/', views.ReservationListCreateView.as_view()),
    path('reservations/<int:pk>',
         views.ReservationRetrieveUpdateDestroyAPIView.as_view()),

    path('payments/', views.PaymentListCreateView.as_view()),
    path('payments/<int:pk>',
         views.PaymentRetrieveUpdateDestroyAPIView.as_view()),
]
