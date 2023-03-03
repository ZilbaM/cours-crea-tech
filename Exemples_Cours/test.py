# Importer les bibliothèques utilisées
import machine

# Créer le périphérique I2C
sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

# Scanner le bus I2C
print('Scan du bus i2c...')
devices = i2c.scan()

if len(devices) == 0:
    print("Aucun composant détecté !")
else:
    print('Composant(s) détectés :',len(devices))

for device in devices:
    print("Adresse en décimal : ",device," | Adresse en Hexadécimal : ",hex(device))