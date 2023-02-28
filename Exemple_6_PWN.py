from machine import Pin, PWM #importation de la librairie machine, on importe la classe Pin et PWM
import time #importation de la librairie time

pwm_led = PWM(Pin(17, mode=Pin.OUT)) #on crée un objet pwm_led qui est une instance de la classe PWM, on lui passe en paramètre un objet de la classe Pin, on lui dit que la pin 17 est une sortie, on sort du courant
pwm_led.freq(1_000) #on définit la fréquence de la pin 17 à 1000 Hz
pwm_led.duty_u16(5000) #on définit le rapport cyclique de la pin 17 à 13000/65535 soit 20%