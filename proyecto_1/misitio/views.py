from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
import requests
from django.http import JsonResponse
from .models import Measurement
# Create your views here.

def start(request):
    data = extract_api_data()


    return render(request, 'home.html', {
        'devices': data,  
    })
def sub(request):
    data = extract_api_data_0()

    return render(request, 'sub.html', {
        'devices' : data
    })
def one(request):
    data = extract_api_data_1()

    return render(request, 'one.html', {
        'devices' : data
    })
def two(request):
    data = extract_api_data_2()

    return render(request, 'two.html', {
        'devices' : data
    })
def three(request):
    data = extract_api_data_3()

    return render(request, 'three.html', {
        'devices' : data
    })
def four(request):
    data = extract_api_data_4()

    return render(request, 'four.html', {
        'devices' : data
    })
def five(request):
    data = extract_api_data_5()

    return render(request, 'five.html', {
        'devices' : data
    })
def top(request):
    data = extract_api_data_6()

    return render(request, 'top.html', {
        'devices' : data
    })

def servers(request):
    return render(request, 'servers.html')

API_URLS = [
    'http://10.68.172.4/api/dev',
    'http://10.68.172.5/api/dev',
    'http://10.68.172.6/api/dev',
    'http://10.68.172.3/api/dev',
    'http://10.68.172.30/api/dev',
    'http://10.68.172.7/api/dev',
    'http://10.68.172.8/api/dev',
    'http://10.68.172.9/api/dev',
    'http://10.68.172.10/api/dev',
    'http://10.68.172.11/api/dev',
    'http://10.68.172.12/api/dev',
    'http://10.68.172.13/api/dev',
    'http://10.68.172.14/api/dev',
    'http://10.68.172.15/api/dev',
    'http://10.68.172.16/api/dev',
    'http://10.68.172.17/api/dev',
    'http://10.68.172.18/api/dev',
    'http://10.68.172.19/api/dev',
    'http://10.68.172.20/api/dev',
    'http://10.68.172.21/api/dev',
    'http://10.68.172.22/api/dev',
    'http://10.68.172.23/api/dev',
    'http://10.68.172.24/api/dev',
    'http://10.68.172.25/api/dev',
    'http://10.68.172.26/api/dev',
    'http://10.68.172.27/api/dev',
    'http://10.68.172.28/api/dev',
    'http://10.68.172.29/api/dev',
]


def process_device_data(main_data, label_filter=None):
    """
    Procesa la información de los dispositivos y las mediciones para estructurarlas correctamente.
    """
    processed_data = []
    
    for device_id, device_info in main_data.items():

        label = device_info.get('label', 'N/A')
        
        if label_filter is not None and label_filter not in str(label):
            continue
        device_data = {
            "device_id": device_id,
            "type": device_info.get('type', 'N/A'),
            "state": device_info.get('state', 'N/A'),
            "name": device_info.get('name', 'N/A'),
            "label": device_info.get('label', 'N/A'),
            "measurements": []
        }
        entity = device_info.get('entity', {}).get('0', {})
        measurements = entity.get('measurement', {})
        
        for measurement_id, measurement in measurements.items():
            measurement_data = {
                "id": measurement_id,
                "type": measurement.get('type', 'N/A'),
                "value": measurement.get('value', 'N/A'),
                "units": measurement.get('units', ''),
                "state": measurement.get('state', 'N/A'),
                "alarm_state": measurement.get('alarm', {}).get('state', 'N/A'),
                "datalog_enabled": measurement.get('datalogEnabled', False),
                "display_enabled": measurement.get('displayEnabled', False)
            }
            device_data['measurements'].append(measurement_data)
        
        processed_data.append(device_data)
    
    return processed_data


def extract_api_data():
    """
    Obtiene los datos de múltiples APIs externas y los procesa.
    """
    all_processed_data = []
    api_ips = []

    for api_url in API_URLS:
        try:
            ip = api_url.split('/')[2]
            api_ips.append(ip)
            
            response = requests.get(api_url)
            response.raise_for_status() 

            data = response.json()

            if data.get('retCode') != 0:
                error_message = data.get('retMsg', 'Unknown error')
                print(f"API request failed for {api_url}. Message: {error_message}")
                continue 

            main_data = data.get('data', {})
            processed_data = process_device_data(main_data)

            for device_data in processed_data:
                device_data['api_ip'] = ip

            all_processed_data.extend(processed_data)

        except requests.RequestException as e:
            print(f"Error fetching data from API ({api_url}): {str(e)}")
            continue  

        except (KeyError, TypeError) as e:
            print(f"Error processing API response ({api_url}): {str(e)}")
            continue  

        except Exception as e:
            print(f"Unexpected error with API {api_url}: {str(e)}")
            continue  
    
    return all_processed_data
def extract_api_data_0():
    """
    Obtiene los datos de múltiples APIs externas y los procesa.
    """
    all_processed_data = []
    api_ips = []

    for api_url in API_URLS:
        try:
            ip = api_url.split('/')[2]
            api_ips.append(ip)
            
            response = requests.get(api_url)
            response.raise_for_status() 

            data = response.json()

            if data.get('retCode') != 0:
                error_message = data.get('retMsg', 'Unknown error')
                print(f"API request failed for {api_url}. Message: {error_message}")
                continue 

            main_data = data.get('data', {})
            processed_data = process_device_data(main_data,label_filter='0')

            for device_data in processed_data:
                device_data['api_ip'] = ip

            all_processed_data.extend(processed_data)

        except requests.RequestException as e:
            print(f"Error fetching data from API ({api_url}): {str(e)}")
            continue  

        except (KeyError, TypeError) as e:
            print(f"Error processing API response ({api_url}): {str(e)}")
            continue  

        except Exception as e:
            print(f"Unexpected error with API {api_url}: {str(e)}")
            continue  
    
    return all_processed_data
def extract_api_data_1():
    """
    Obtiene los datos de múltiples APIs externas y los procesa.
    """
    all_processed_data = []
    api_ips = []

    for api_url in API_URLS:
        try:
            ip = api_url.split('/')[2]
            api_ips.append(ip)
            
            response = requests.get(api_url)
            response.raise_for_status() 

            data = response.json()

            if data.get('retCode') != 0:
                error_message = data.get('retMsg', 'Unknown error')
                print(f"API request failed for {api_url}. Message: {error_message}")
                continue 

            main_data = data.get('data', {})
            processed_data = process_device_data(main_data,label_filter='1')

            for device_data in processed_data:
                device_data['api_ip'] = ip

            all_processed_data.extend(processed_data)

        except requests.RequestException as e:
            print(f"Error fetching data from API ({api_url}): {str(e)}")
            continue  

        except (KeyError, TypeError) as e:
            print(f"Error processing API response ({api_url}): {str(e)}")
            continue  

        except Exception as e:
            print(f"Unexpected error with API {api_url}: {str(e)}")
            continue  
    
    return all_processed_data
def extract_api_data_2():
    """
    Obtiene los datos de múltiples APIs externas y los procesa.
    """
    all_processed_data = []
    api_ips = []

    for api_url in API_URLS:
        try:
            ip = api_url.split('/')[2]
            api_ips.append(ip)
            
            response = requests.get(api_url)
            response.raise_for_status() 

            data = response.json()

            if data.get('retCode') != 0:
                error_message = data.get('retMsg', 'Unknown error')
                print(f"API request failed for {api_url}. Message: {error_message}")
                continue 

            main_data = data.get('data', {})
            processed_data = process_device_data(main_data,label_filter='2')

            for device_data in processed_data:
                device_data['api_ip'] = ip

            all_processed_data.extend(processed_data)

        except requests.RequestException as e:
            print(f"Error fetching data from API ({api_url}): {str(e)}")
            continue  

        except (KeyError, TypeError) as e:
            print(f"Error processing API response ({api_url}): {str(e)}")
            continue  

        except Exception as e:
            print(f"Unexpected error with API {api_url}: {str(e)}")
            continue  
    
    return all_processed_data
def extract_api_data_3():
    """
    Obtiene los datos de múltiples APIs externas y los procesa.
    """
    all_processed_data = []
    api_ips = []

    for api_url in API_URLS:
        try:
            ip = api_url.split('/')[2]
            api_ips.append(ip)
            
            response = requests.get(api_url)
            response.raise_for_status() 

            data = response.json()

            if data.get('retCode') != 0:
                error_message = data.get('retMsg', 'Unknown error')
                print(f"API request failed for {api_url}. Message: {error_message}")
                continue 

            main_data = data.get('data', {})
            processed_data = process_device_data(main_data,label_filter='3')

            for device_data in processed_data:
                device_data['api_ip'] = ip

            all_processed_data.extend(processed_data)

        except requests.RequestException as e:
            print(f"Error fetching data from API ({api_url}): {str(e)}")
            continue  

        except (KeyError, TypeError) as e:
            print(f"Error processing API response ({api_url}): {str(e)}")
            continue  

        except Exception as e:
            print(f"Unexpected error with API {api_url}: {str(e)}")
            continue  
    
    return all_processed_data
def extract_api_data_4():
    """
    Obtiene los datos de múltiples APIs externas y los procesa.
    """
    all_processed_data = []
    api_ips = []

    for api_url in API_URLS:
        try:
            ip = api_url.split('/')[2]
            api_ips.append(ip)
            
            response = requests.get(api_url)
            response.raise_for_status() 

            data = response.json()

            if data.get('retCode') != 0:
                error_message = data.get('retMsg', 'Unknown error')
                print(f"API request failed for {api_url}. Message: {error_message}")
                continue 

            main_data = data.get('data', {})
            processed_data = process_device_data(main_data,label_filter='4')

            for device_data in processed_data:
                device_data['api_ip'] = ip

            all_processed_data.extend(processed_data)

        except requests.RequestException as e:
            print(f"Error fetching data from API ({api_url}): {str(e)}")
            continue  

        except (KeyError, TypeError) as e:
            print(f"Error processing API response ({api_url}): {str(e)}")
            continue  

        except Exception as e:
            print(f"Unexpected error with API {api_url}: {str(e)}")
            continue  
    
    return all_processed_data
def extract_api_data_5():
    """
    Obtiene los datos de múltiples APIs externas y los procesa.
    """
    all_processed_data = []
    api_ips = []

    for api_url in API_URLS:
        try:
            ip = api_url.split('/')[2]
            api_ips.append(ip)
            
            response = requests.get(api_url)
            response.raise_for_status() 

            data = response.json()

            if data.get('retCode') != 0:
                error_message = data.get('retMsg', 'Unknown error')
                print(f"API request failed for {api_url}. Message: {error_message}")
                continue 

            main_data = data.get('data', {})
            processed_data = process_device_data(main_data,label_filter='5')

            for device_data in processed_data:
                device_data['api_ip'] = ip

            all_processed_data.extend(processed_data)

        except requests.RequestException as e:
            print(f"Error fetching data from API ({api_url}): {str(e)}")
            continue  

        except (KeyError, TypeError) as e:
            print(f"Error processing API response ({api_url}): {str(e)}")
            continue  

        except Exception as e:
            print(f"Unexpected error with API {api_url}: {str(e)}")
            continue  
    
    return all_processed_data
def extract_api_data_6():
    """
    Obtiene los datos de múltiples APIs externas y los procesa.
    """
    all_processed_data = []
    api_ips = []

    for api_url in API_URLS:
        try:
            ip = api_url.split('/')[2]
            api_ips.append(ip)
            
            response = requests.get(api_url)
            response.raise_for_status() 

            data = response.json()

            if data.get('retCode') != 0:
                error_message = data.get('retMsg', 'Unknown error')
                print(f"API request failed for {api_url}. Message: {error_message}")
                continue 

            main_data = data.get('data', {})
            processed_data = process_device_data(main_data,label_filter='6')

            for device_data in processed_data:
                device_data['api_ip'] = ip

            all_processed_data.extend(processed_data)

        except requests.RequestException as e:
            print(f"Error fetching data from API ({api_url}): {str(e)}")
            continue  

        except (KeyError, TypeError) as e:
            print(f"Error processing API response ({api_url}): {str(e)}")
            continue  

        except Exception as e:
            print(f"Unexpected error with API {api_url}: {str(e)}")
            continue  
    
    return all_processed_data
@api_view(['GET'])
def get_device_data(request):
    """
    Vista para devolver los datos de los dispositivos en formato JSON.
    """
    data = extract_api_data()
    return JsonResponse(data, safe=False)
def obtener_dispositivos_0(request):
    try:
        
        dispositivos = extract_api_data_0()
        
        return JsonResponse(dispositivos, safe=False)  
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
def obtener_dispositivos_1(request):
    try:
        
        dispositivos = extract_api_data_1()
        
        return JsonResponse(dispositivos, safe=False)  
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
def obtener_dispositivos_2(request):
    try:
        
        dispositivos = extract_api_data_2()
        
        return JsonResponse(dispositivos, safe=False)  
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
def obtener_dispositivos_3(request):
    try:
        
        dispositivos = extract_api_data_3()
        
        return JsonResponse(dispositivos, safe=False)  
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
def obtener_dispositivos_4(request):
    try:
        
        dispositivos = extract_api_data_4()
        
        return JsonResponse(dispositivos, safe=False)  
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
def obtener_dispositivos_5(request):
    try:
        
        dispositivos = extract_api_data_5()
        
        return JsonResponse(dispositivos, safe=False)  
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
def obtener_dispositivos_6(request):
    try:
        
        dispositivos = extract_api_data_6()
        
        return JsonResponse(dispositivos, safe=False)  
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
def obtener_mediciones(request):
    # Obtén todas las mediciones
    measurements = Measurement.objects.all()

    # Convierte las mediciones a formato JSON
    measurements_data = []
    for measurement in measurements:
        measurements_data.append({
            'label': measurement.label,
            'value': measurement.value
        })

    # Retorna las mediciones como JSON
    return JsonResponse(measurements_data, safe=False)