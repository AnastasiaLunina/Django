from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensors'

    def __str__(self):
        return self.name, self.description


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='smart_home/images', blank=True)

    class Meta:
        verbose_name = 'Measurement'
        verbose_name_plural = 'Measurements'

    def __str__(self):
        return self.sensor, self.temperature, self.created_at

