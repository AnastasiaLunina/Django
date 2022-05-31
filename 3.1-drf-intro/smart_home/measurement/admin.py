from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Sensor, Measurement

# Register your models here.


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    ordering = ['id']


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'sensor', 'temperature', 'created_at', 'image']
    ordering = ['id']


