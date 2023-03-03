
# from luma.core.device import ssd1306
# from luma.core.interface.serial import i2c
# from luma.core.render import canvas
from luma.oled.device import ssd1306

# serial = i2c(port=1, address=0x3C)
# device = ssd1306(serial)

# with canvas(device) as draw:
#     draw.rectangle(device.bounding_box, outline="white", fill="black")
#     draw.text((30, 40), "Hello World", fill="white")



# # The pins are wired as follows : VCC = 3V3, GND = GND, SCL = GP1, SDA = GP0
# # Define the pins used for the I2C communication with the I2C func. Its arguments are the I2C bus number, the scl pin and the sda pin
# # i2c = I2C(0, scl=Pin(1), sda=Pin(0))

# # Define the oled display
# # oled = SSD1306_I2C(128, 64, i2c)

# # Display "Hello World" on the oled display
# # oled.fill(0)
# # oled.text("Hello World", 0, 0)
# # oled.show()

import ssd1306