import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
from machine import Pin, PWM	#import des fonction lier à la pin

print('Waiting for pins...')

blue = PWM(Pin(16, mode=Pin.OUT)) #création d'un objet PWM sur la pin 15
green = PWM(Pin(17, mode=Pin.OUT)) #création d'un objet PWM sur la pin 15
red = PWM(Pin(18, mode=Pin.OUT)) #création d'un objet PWM sur la pin 15

print('Pins connected')

leds = [blue, green, red] #création d'une liste contenant les 3 objets PWM

for led in leds :
    led.freq(1000)
    led.duty_u16(5000) #duty cycle de 50%

pokemon_types = {
    'Normal': [230, 230, 230],
    'Feu': [255, 50, 0],
    'Eau': [0, 125, 255],
    'Électrik': [255, 220, 0],
    'Plante': [0, 175, 0],
    'Glace': [165, 255, 255],
    'Combat': [204, 85, 68],
    'Poison': [160, 64, 160],
    'Sol': [219, 184, 96],
    'Vol': [153, 153, 255],
    'Psy': [250, 97, 161],
    'Insecte': [166, 185, 26],
    'Roche': [184, 160, 56],
    'Spectre': [112, 88, 152],
    'Dragon': [102, 68, 221],
    'Ténèbres': [40, 40, 72],
    'Acier': [184, 184, 208],
    'Fée': [240, 182, 214]
}

def set_color(color):
    for i in range(3):
        leds[i].duty_u16(color[i] * 5000)

ssid = 'iPhone de Zoé'
password = 'laStreet'
url = "https://api-pokemon-fr.vercel.app/api/v1/pokemon/25"

wlan = network.WLAN(network.STA_IF) # création d'un objet wifi
wlan.active(True) # active le wifi


wlan.connect(ssid, password) # connecte la raspi au réseau
while not wlan.isconnected(): # tant que la raspi n'est pas connecté
    print("Waiting for connection")
    utime.sleep(1)

json = None
while json is None:
    try:
        print("GET Pokemon")
        request = urequests.get(url) # lance une requete sur l'url
        json = request.json()  # traite sa reponse en Json
        request.close()
    except Exception as e:
        print(e)
        utime.sleep(1)

typeValue = json['types'][0]['name']
if typeValue is not None: 
    color = pokemon_types[typeValue]
    print(typeValue)
    set_color(color)
    



# while(True):
#     try:
#         print("GET")
#         r = urequests.get(url) # lance une requete sur l'url
#         print(r.json()) # traite sa reponse en Json
#         r.close() # ferme la demande
#         utime.sleep(1)  
#     except Exception as e:
#         print(e)
    