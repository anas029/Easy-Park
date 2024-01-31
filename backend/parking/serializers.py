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


class ParkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpace
        fields = '__all__'

    size = serializers.CharField(read_only=True)
    location = LocationSerializer(read_only=True)
    price_rate = PriceRateSerializer(read_only=True)
    price_rate_id = serializers.PrimaryKeyRelatedField(
        queryset=PriceRate.objects.all(), write_only=True, source='price_rate'
    )

    def validate(self, data):
        data['location_id'] = data['price_rate'].location.id
        existing_spaces = ParkingSpace.objects.filter(
            location=data['location_id'],
            story=data['story'],
            space_number=data['space_number']
        )
        if self.instance:
            existing_spaces = existing_spaces.exclude(
                pk=self.instance.pk)  # Exclude current instance if updating
        if existing_spaces.exists():
            raise serializers.ValidationError(
                "A parking space with the same location, story, and space number already exists.")
        return data


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
