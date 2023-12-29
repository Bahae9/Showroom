from django.shortcuts import render, redirect
from .models import Car
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer

def upload(request):
    if request.method == 'POST':
        car_name = str(request.POST['car_name'])
        car_price_str = request.POST['car_price']
        car_price = float(car_price_str) if car_price_str else 0.0
        if Car.objects.filter(car_name=car_name).exists():
            messages.info(request, 'Car name already exists!')
            return render(request, 'main/upload_car.html')
        else:
            if request.FILES.get('car_image') == None:
                new_car = Car.objects.create(car_name=car_name, price=car_price)
            else:
                car_image = request.FILES.get('car_image')
                new_car = Car.objects.create(car_name=car_name, image=car_image, price=car_price)
            new_car.save()
    return render(request, 'main/upload_car.html')


def search(request):
    try:
        search_result = request.POST['search']
        if search_result :
            cars = Car.objects.filter(car_name__icontains=search_result)
        elif search_result == '':
            cars = Car.objects.all()
        context = {
            'cars' : cars
        }
        return render(request, 'main/show.html', context)
    except:
        return redirect('/')

def remove(request):
    try:
        remove = request.POST.get('remove')
        car = Car.objects.get(car_name=remove)
        car.image.delete()
        car.delete()
        return render(request, 'main/show.html', {'cars' : Car.objects.all()})
    except Car.DoesNotExist:
        return redirect('/')
    
@api_view(['GET'])
def car_list(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)