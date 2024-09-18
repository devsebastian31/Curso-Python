from geopy.geocoders import Nominatim

def obtener_longitud_latitud(): # Creamos la funcion
    geolocator = Nominatim(user_agent="mi_aplicacion") # Nombre de la aplicacion
    location = geolocator.geocode(input("Ingresa la ubicacion: ")) ## 1600 Amphitheatre Parkway, Mountain View, CA
    if location:
        latitud = location.latitude # Obtenemos la latitud
        longitud = location.longitude # Obtenemos la longitud
        print(f"Latitud: {latitud}")
        print(f"Longitud: {longitud}")
        print(location.address)

    else:
        print("No se puedo obtener las coordenadas")

obtener_longitud_latitud()