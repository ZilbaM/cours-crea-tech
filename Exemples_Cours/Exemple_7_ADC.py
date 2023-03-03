from machine import ADC, Pin #importation de la librairie machine
import time



adc = ADC(Pin(26, mode=Pin.IN))

while True:
    val = adc.read_u16()
    val = val * (3.3 / 65535)
    print(round(val, 2), "V")
    time.sleep_ms(100)