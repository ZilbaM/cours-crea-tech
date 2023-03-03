from machine import Pin, PWM #importation de la librairie machine, on importe la classe Pin et PWM
import utime #importation de la librairie time


blue = PWM(Pin(16, mode=Pin.OUT)) #création d'un objet PWM sur la pin 15
green = PWM(Pin(17, mode=Pin.OUT)) #création d'un objet PWM sur la pin 15
red = PWM(Pin(18, mode=Pin.OUT)) #création d'un objet PWM sur la pin 15

leds = [blue, green, red] #création d'une liste contenant les 3 objets PWM

for led in leds :
    led.freq(1000)
    led.duty_u16(5000) #duty cycle de 50%

while True:
    # Turn the rgb led blue
    blue.duty_u16(5000)
    green.duty_u16(0)
    red.duty_u16(0)
    utime.sleep(1)
    
