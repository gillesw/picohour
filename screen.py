from waveshare_oled import SSD1306_I2C
from datetime import datetime
import time

def main():
    # Initialize the OLED display
    oled = SSD1306_I2C(128, 64, i2c)
    oled.init()

    while True:
        # Get the current time
        current_time = datetime.now().strftime("%H:%M:%S")

        # Clear the display
        oled.clear()

        # Set the font size
        oled.set_font(20)

        # Display the time
        oled.draw_text(0, 0, current_time)

        # Update the display
        oled.display()

        # Wait one second
        time.sleep(1)

if __name__ == "__main__":
    main()