from machine import Pin #importation de la librairie machine
import utime #importation de la librairie time

pin_button = Pin(15, mode=Pin.IN, pull=Pin.PULL_UP) #on crée un objet pin_button qui est une instance de la classe Pin, on lui dit que la pin 17 est une entrée, on rentre du courant, on active la résistance de tirage

while True:
    print(pin_button.value())
    utime.sleep(.1)