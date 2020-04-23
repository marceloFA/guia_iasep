from django.shortcuts import render
from guia.models import City, Service, Place

def homepage(request, template_name="homepage.html"):
    """ Raíz do website"""
    context = {
        "cities":City.objects.all(),
        "services":Service.objects.all()
        }
    return render(request, template_name, context=context)

def city_detail(request, city_slug, template_name="city_detail.html"):
    """ All Services of a City"""
    
    city = City.objects.get(slug=city_slug)
    services = get_city_services(city.id)
    context= {
        "city":city,
        "services":services,
       }

    return render(request, template_name, context=context)

def places_listing(request, city_slug, service_slug, template_name="places_listing.html"):
    """ Places providing a certain Service on a certain City"""
    
    city = City.objects.get(slug=city_slug)
    service = Service.objects.get(slug=service_slug)

    context={
        "city":city,
        "service":service,
        "places":Place.objects.filter(city=city.id,service=service.id)
        }
    return render(request, template_name, context=context)

def get_city_services(city_id):
    # Get all srevices from a city
    all_city_services = Place.objects.filter(city=city_id)
    # Filter unique services
    services_ids = list(all_city_services.order_by().values_list('service',flat=True).distinct())
    # Map ids to their name
    city_services = [Service.objects.get(id=id) for id in services_ids]
    return city_services