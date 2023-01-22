from machine import SPI, Pin
import ssd1306
import utime

DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9

# Initialise le bus SPI
spi = SPI(id=1, sck=Pin(SCK), miso=None, mosi=Pin(MOSI))

# Initialise l'écran OLED
oled = ssd1306.SSD1306_SPI(128, 64, spi, dc=Pin(DC), res=Pin(RST), cs=Pin(CS))

while True:
    # Get current time
    current_time = utime.localtime()
    # Format the time to be displayed
    time_string = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])
    # Clear the OLED screen
    oled.fill(0)
    # Draw the time string on the OLED screen
    oled.text(time_string, 0, 0)
    oled.show()
    # Sleep for 1 second
    utime.sleep(1)