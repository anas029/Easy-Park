import random
import string

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Location(models.Model):
    name = models.CharField(max_length=256, unique=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    State = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=15, null=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.size


class PriceRate(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    initial_rate = models.DecimalField(max_digits=10, decimal_places=3)
    rate_per_hour = models.DecimalField(max_digits=10, decimal_places=3)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['location', 'initial_rate', 'rate_per_hour', 'size']

    def __str__(self):
        return f'{self.initial_rate} + {self.rate_per_hour}/hour in {self.location}, size: {self.size}'


class ParkingSpace(models.Model):
    is_available = models.BooleanField(default=True)
    story = models.IntegerField()
    space_number = models.CharField(max_length=10)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price_rate = models.ForeignKey(PriceRate, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ['location', 'story', 'space_number']

    def __str__(self):
        return f'{self.location} - {self.story}:{self.space_number}'


RESERVATION_STATUS = (
    ('P', 'Pending'),
    ('A', 'Approved'),
    ('C', 'Cancelled'),
    ('I', 'Checked in'),
    ('O', 'Checked out'),
    ('E', 'Expired'),
    ('D', 'Overdue'),
)


class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    reservation = models.DateTimeField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    status = models.CharField(max_length=1, choices=RESERVATION_STATUS)


class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    payment_date_time = models.DateTimeField()
    payment_method = models.CharField(max_length=15)
    payment_reference = models.CharField(max_length=300, null=True)


class Receipt(models.Model):
    receipt_reference = models.CharField(max_length=300, unique=True)
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    email_sent = models.BooleanField()

    def __str__(self):
        return self.receipt_reference

    def save(self, *args, **kwargs):
        if not self.receipt_reference:
            # Generate random characters
            random_chars = ''.join(random.choices(
                string.ascii_uppercase + string.digits, k=6))
            # Generate a unique reference combining date/time, receipt PK, and random characters
            timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
            # Assuming receipt PK is padded with zeros up to 6 digits
            pk_str = str(self.pk).zfill(6)
            self.receipt_reference = f"{timestamp}{pk_str}-{random_chars}"
        super().save(*args, **kwargs)
