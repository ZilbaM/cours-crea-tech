from machine import Pin, I2C
from bme680 import *
import utime
from pico_i2c_lcd import I2cLcd
from rotary_irq_rp2 import RotaryIRQ
import urequests
import network

i2c= I2C(0, sda=Pin(20), scl=Pin(21), freq=400000)    #initializing the I2C method 
bme = BME680_I2C(i2c=i2c)
lcd_i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
I2C_ADDR = lcd_i2c.scan()[0]
lcd = I2cLcd(lcd_i2c, I2C_ADDR, 2, 16)

r = RotaryIRQ(
    pin_num_clk=10,
    pin_num_dt=13,
    reverse=False,
    min_val=0,
    max_val=6,
    incr=1,
    range_mode=RotaryIRQ.RANGE_WRAP,
    pull_up=True,
    half_step=False,
)
lcd.move_to(0,0)
lcd.putstr("Loading...")
def temperature():
    return str(round(bme.temperature, 2)) + ' C'

def pressure():
    return str(round(bme.pressure)) + ' Pa'

def gas():
    return str(round(bme.gas)) + ' Ohms'

def humidity():
    return str(round(bme.humidity, 2)) + ' %'

def valueToGauge(value, min, max, unitSize):
    gauge = '['
    fillSize = int(round(float(float(value[:-unitSize]) / (abs(min) + abs(max))) * 14))
    for i in range(fillSize):
        gauge += '='
    for i in range(14 - fillSize):
        gauge += ' '
    gauge += ']'
    return gauge

def displayMetric(metric, value, min, max, unitSize):
    firstLine = metric + ': ' + value + ' ' * (16 - len(metric + ': ' + value))
    lcd.move_to(0, 0)
    lcd.putstr(firstLine)
    lcd.move_to(0, 1)
    lcd.putstr(valueToGauge(value, min, max, unitSize))
    
def displayApi(metric = "time"):
    if metric == "time":
        lcd.move_to(0,0)
        (year, month, mday, hour, minute, second, weekday, yearday) = utime.localtime()
        datestr = 'Date :' + str(year) + '/' + str(month) + '/' + str(mday) 
        lcd.putstr(datestr + (' ' * (16 - len(datestr) ) ) )
        lcd.move_to(0, 1)
        timestr = 'Time :' + str(hour) + ':' + str(minute)
        lcd.putstr(timestr + (' ' * (16 - len(timestr) ) ))
    else:
        if metric == 'sunrise':
            lines = sunrise
            lines = [lines[0] + (' ' * (16 - len(lines[0]) ) ), lines[1] + (' ' * (16 - len(lines[1]) ) )]
        elif metric == 'sunset':
            lines = sunset
            lines = [lines[0] + (' ' * (16 - len(lines[0]) ) ), lines[1] + (' ' * (16 - len(lines[1]) ) )]
        lcd.move_to(0, 0)
        lcd.putstr(lines[0])
        lcd.move_to(0, 1)
        lcd.putstr(lines[1])
    
def callApi():
    json = None
    while json is None:
        try:
            request = urequests.get(apiURL) # lance une requete sur l'url
            json = request.json()  # traite sa reponse en Json
            request.close()
        except Exception as e:
            print(e)
            utime.sleep(1)
    return json

def parseApiResult(metric, data):
    if metric == 'sunset':
        return ["Sunset at:", data["daily"]["sunset"][0][-5:]] 
    elif metric == 'sunrise':
        return ["Sunrise at:", data["daily"]["sunrise"][0][-5:]]

ssid = 'iPhone de Zoé'
password = 'laStreet'
apiURL = 'https://api.open-meteo.com/v1/meteofrance?latitude=48.89&longitude=2.22&daily=sunrise,sunset&timezone=Europe%2FBerlin'

wlan = network.WLAN(network.STA_IF) # création d'un objet wifi
wlan.active(True) # active le wifi

wlan.connect(ssid, password) # connecte la raspi au réseau
while not wlan.isconnected(): # tant que la raspi n'est pas connecté
    print("Waiting for connection")
    utime.sleep(1)
    
apiData = callApi()
sunset = parseApiResult("sunset", apiData)
sunrise = parseApiResult("sunrise", apiData)

displayedMetric = 0
while True:
    try:
        val_new = r.value()
        if val_new != displayedMetric:
            displayedMetric = val_new
        if displayedMetric == 0:
            displayMetric('Temp.', temperature(), -20, 50, 2)
        elif displayedMetric == 1:
            displayMetric('Pres.', pressure(), 300, 1100, 3)
        elif displayedMetric == 2:
            displayMetric('Gas', gas(), 90000, 150000, 4)
        elif displayedMetric == 3:
            displayMetric('Hum.', humidity(), 0, 100, 2)
        elif displayedMetric == 4:
            displayApi("time")
        elif displayedMetric == 5:
            displayApi('sunrise')
        elif displayedMetric == 6:
            displayApi('sunset')
        
    except Exception as e:
        print(e)

    utime.sleep_ms(50)
