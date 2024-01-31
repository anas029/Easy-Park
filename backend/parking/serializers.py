from rest_framework import serializers

from .models import (Location, ParkingSpace, Payment, PriceRate, Receipt,
                     Reservation, Size)


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ParkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpace
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PriceRateSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    size = SizeSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), write_only=True, source='location'
    )
    size_id = serializers.PrimaryKeyRelatedField(
        queryset=Size.objects.all(), write_only=True, source='size'
    )

    class Meta:
        model = PriceRate
        fields = '__all__'


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
