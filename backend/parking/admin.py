from django.contrib import admin

from .models import (Location, ParkingSpace, Payment, PriceRate, Receipt,
                     Reservation, Size)

admin.site.register([Location, ParkingSpace, Payment,
                    PriceRate, Receipt, Reservation, Size])
