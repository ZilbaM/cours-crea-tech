import utime
from machine import Pin

pinNumber = 17
pin2Number = 22
led = Pin(pinNumber, mode=Pin.OUT) #signifie que la pin 17 est une sortie, on sort du courant
led2 = Pin(pin2Number, mode=Pin.OUT) #signifie que la pin 22 est une sortie, on sort du courant


while True:
    led.toggle()
    led2.toggle()
    utime.sleep(1)
