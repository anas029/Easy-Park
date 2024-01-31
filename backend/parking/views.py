from rest_framework import status
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     RetrieveAPIView,
                                     ListAPIView)
from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import (Location, ParkingSpace, Payment, PriceRate, Receipt,
                     Reservation, Size)
from .permissions import IsAdminUserOrReadOnly
from .serializers import (LocationSerializer, ParkingSpaceSerializer,
                          PaymentSerializer, PriceRateSerializer,
                          ReceiptSerializer, ReservationSerializer,
                          SizeSerializer)

# Create your views here.


class SizeListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SizeSerializer
    queryset = Size.objects.all()


class SizeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SizeSerializer
    queryset = Size.objects.all()


class LocationListCreateView(ListCreateAPIView):
    # permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class ParkingSpaceListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ParkingSpaceSerializer
    queryset = ParkingSpace.objects.select_related(
        'price_rate__size', 'location', 'price_rate__location')


class ParkingSpaceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ParkingSpaceSerializer
    queryset = ParkingSpace.objects.select_related(
        'price_rate__size', 'location', 'price_rate__location')


class PaymentListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PaymentSerializer
    # queryset = Payment.objects.all()
    queryset = Payment.objects.select_related(
        'reservation')


class PaymentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PriceRateListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PriceRateSerializer
    queryset = PriceRate.objects.select_related(
        'size', 'location')


class PriceRateRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PriceRateSerializer
    queryset = PriceRate.objects.select_related(
        'size', 'location')


class ReceiptListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ReceiptSerializer
    queryset = Receipt.objects.all()


class ReceiptRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ReceiptSerializer
    queryset = Receipt.objects.all()


class ReservationListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    # queryset = Reservation.objects.select_related('user', 'parking_space').prefetch_related(
    #     'receipt_set', 'payment_set')
    # queryset = queryset.prefetch_related('childmodel_set')


class ReservationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
