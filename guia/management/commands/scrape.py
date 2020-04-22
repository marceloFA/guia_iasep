from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import traceback

from guia.models import City, Service, Place

class Command(BaseCommand):
    ''' Scrapes into IASEP medical guide and get their info '''

    help = "Scrapes into IASEP medical guide and get their info"
    
    def handle(self, *args, **options):
        ''' For each model, scrap the html and save information to the database '''

        def update_city_list(soup):
        
            print('Started updating cities list')
            city_select_tag = soup.find('select', {'name':'pfiltro_cod_municipio'})
            city_option_tags = city_select_tag.find_all("option")
            cities_list = [city.get_text(strip=True) for city in city_option_tags]
            id_list = [city['value'] for city in city_option_tags]

            # Save it on the database
            for id, city in zip(id_list, cities_list):
                if not id: continue
                try:
                    City.objects.create(name=city,id=id)
                    print(f'Added {city}')
                except:
                    #traceback.print_exc()
                    print(f'Did not add {city}')
            
            print('Finished adding cities')


        def update_service_list(soup):
            
            service_select_tag = soup.find('select', {'name':'pfiltro_cod_especialidade'})
            service_option_tags = service_select_tag.find_all('option')
            services_list = [service.get_text(strip=True) for service in service_option_tags]
            id_list = [service['value'] for service in service_option_tags]

            # Save it on the database
            for id, service in zip(id_list, services_list):
                try:
                    if not id: continue
                    Service.objects.create(name=service,id=id)
                    print(f'Added {service}')
                except:
                    #traceback.print_exc()
                    print(f'Did not add {service}')


        def update_place_list(url, parser):
        
            form_data = {
                'paction': 6, # Action code
                'pcod_especialidade': 0, # Medical Specialty Code
                'pfiltro_tipo_consulta': 'especialidade', # Consultation Type
                'pnum_pagina':1, # Number of pages
                'pnum_registros':2000, # Number of records
                'pnum_coluna_ord':1 # IDK
            }

            for city in City.objects.all():
                
                # request the date and soupify it
                form_data['pfiltro_cod_municipio'] = int(city.id)
                response = requests.post(url, form_data)
                soup = BeautifulSoup(response.content, parser)

                # Search for the div that contains places information
                try:
                    places_span = soup.find('div', {'id':'corpo'}).find_all('span')
                except:
                    print(f'Could not obtain body for city {city.name}')

                for place in places_span:

                    ##############print('place: \n',place)
                    place_dict = { 'city':city }
                    name = get_place_name(place)
                    service_id = get_place_service_id(place)

                    if not name or not service_id:
                        continue

                    place_dict['name'] = name
                    place_dict['adress'] = get_place_adress(place)
                    place_dict['phone'] =  get_place_phone(place)
                    place_dict['service'] = service_id
                    
                    # maybe save new places
                    try:
                        Place.objects.create(**place_dict)
                        print(f'Added {place_dict["name"]}')
                    except:
                        print(f'Did not add {place_dict["name"]} \n\n\n')
                        traceback.print_exc()
            
        
        # helper functions

        
        def get_place_name(place):
            name_anchor = place.find('div',{'class':'info-medico'}).find('a')
            try:
                name_text = name_anchor.get_text(strip=True)
            except:
                 name_text =None
            finally:
                return name_text

        def get_place_adress(place):
            adress_li = place.find('div',{'class':'info-endereco'}).find('ul').select('ul > li')[0]
            return adress_li.get_text(strip=True)
        
        def get_place_phone(place):
            phone_li = place.find('div',{'class':'info-endereco'}).find('ul').select('ul > li')[1]
            return phone_li.get_text(strip=True)
        
        def get_place_service_id(place):
            service_h1 = place.find_previous_sibling('h1')
            service_text = service_h1.get_text(strip=True)
            service_instance = Service.objects.filter(name=service_text).first() or None
            # in case we can't find the service instance this will return none
            return service_instance
        
        
        ################## Main ##################        
        
        
        url  = 'http://www.e-saude.iasep.pa.gov.br/guiamedico/guia.cfm'
        parser = 'lxml'
        html = urlopen(url)
        soup = BeautifulSoup(html, parser)
        
        update_city_list(soup)
        update_service_list(soup)
        update_place_list(url, parser)


    
