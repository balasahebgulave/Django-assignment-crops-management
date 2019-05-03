from django.shortcuts import render 
from django.http import HttpResponse
from datetime import datetime
from FarmerApp.models import FarmerData , FarmData , ScheduleData


def homepage(request):
	sheduledata = ScheduleData.objects.all()
	farmers = FarmerData.objects.all()
	context = {'sheduledata':sheduledata, 'farmers':farmers}
	name = request.POST.get('farmer')
	if name != None:
		if request.method == 'POST':
			name = request.POST.get('farmer')
			farmer_object = FarmerData.objects.get(name = name)
			farm_object = FarmData.objects.get(name = farmer_object)
			shedule_object = ScheduleData.objects.filter(crop = farm_object)
			price = [int(i.price) for i in shedule_object]
			context['price'] = sum(price)
			context['shedule_object'] = shedule_object
			return render (request, 'FarmerApp/homepage.html', context)
	else:
		if request.method == 'POST':
			shedule = request.POST.get('shedule')
			crop_farm_object = FarmData.objects.all()
			shedule_data = []
			if shedule == 'Today':
				for crop in crop_farm_object:
					days = (datetime.now().date() - crop.sowing_date).days
					shedule_object = ScheduleData.objects.filter(crop = crop)
					for obj in shedule_object:
						if days == obj.days_after_sowing:
							shedule_data.append(obj)
			if shedule == 'Tomorrow':
				for crop in crop_farm_object:
					days = (datetime.now().date() - crop.sowing_date).days + 1
					shedule_object = ScheduleData.objects.filter(crop = crop)
					for obj in shedule_object:
						if days == obj.days_after_sowing:
							shedule_data.append(obj)
			print(shedule_data)
			context['shedule_data'] = shedule_data
			return render (request, 'FarmerApp/homepage.html', context)
	return render (request, 'FarmerApp/homepage.html', context)


