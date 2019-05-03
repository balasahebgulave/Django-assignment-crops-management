from django.db import models

class FarmerData(models.Model):
	phone = models.CharField(max_length = 20)
	name = models.CharField(max_length = 100)
	language = models.CharField(max_length = 100)

class FarmData(models.Model):
	name = models.ForeignKey(FarmerData, on_delete = models.CASCADE)
	area = models.CharField(max_length = 100)
	village = models.CharField(max_length = 100)
	crop = models.CharField(max_length = 100)
	sowing_date = models.DateField(auto_now_add=False, blank=True)

class ScheduleData(models.Model):
	UNIT_CHOICES = (
        ('L', 'Litre'),
        ('kg', 'kilograms'),
        ('g', 'grams'),
        ('mL', 'mililitre'),
        ('ton', 'tones')

    )
	crop = models.ForeignKey(FarmData, on_delete = models.CASCADE)
	price = models.CharField(max_length = 100)
	days_after_sowing = models.IntegerField(blank = True , default = 0)
	fertilizer = models.CharField(max_length = 100)
	quantity = models.IntegerField()
	unit = models.CharField(max_length = 10 , choices = UNIT_CHOICES)