from django.contrib import admin
from FarmerApp.models import FarmerData , FarmData , ScheduleData

admin.site.register(FarmerData)
admin.site.register(FarmData)
admin.site.register(ScheduleData)