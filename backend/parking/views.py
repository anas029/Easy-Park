from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
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
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class ParkingSpaceListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ParkingSpaceSerializer
    # queryset = ParkingSpace.objects.select_related(
    #     'price_rate__size', 'location')

    # # Using select_related to fetch the related models in a single query
    # queryset = ParkingSpace.objects.select_related('location', 'price_rate')

    # # Using prefetch_related for reverse foreign key relationships
    # queryset = PriceRate.objects.prefetch_related(
    #     'location_set', 'location_set')
    def get_queryset(self):
        # Using select_related to fetch the related models in a single query
        queryset = ParkingSpace.objects.select_related(
            'location', 'price_rate')

        # Using prefetch_related for reverse foreign key relationships
        queryset = queryset.prefetch_related('price_rate__location_set')

        return queryset


class ParkingSpaceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ParkingSpaceSerializer
    queryset = ParkingSpace.objects.all()


class PaymentListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PriceRateListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PriceRateSerializer
    queryset = PriceRate.objects.all()


class PriceRateRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PriceRateSerializer
    queryset = PriceRate.objects.all()


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


class ReservationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
