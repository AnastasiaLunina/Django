from django.urls import path
from .views import SensorListCreateAPIView, SensorRetrieveUpdateAPIView, MeasurementListCreateAPIView

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view()),
    path('sensors/<int:pk>', SensorRetrieveUpdateAPIView.as_view()),
    path('measurements/', MeasurementListCreateAPIView.as_view())

]
