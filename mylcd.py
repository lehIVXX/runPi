from subprocess import check_output
from time import sleep
from datetime import datetime
from rpi_lcd import LCD
lcd = LCD()
lcd.clear()
def get_ip():
    cmd = "hostname -I | cut -d\' \' -f1"
    return check_output(cmd, shell=True).decode("utf-8").strip()
while True:
    lcd_line_1 = datetime.now().strftime('%b %d - %H:%M')
    lcd_line_2 = "IP " + get_ip()
    lcd_line_3 = "Web octopi.local"
    lcd.clear()
    lcd.text(lcd_line_3,1)
    lcd.text(lcd_line_1,2)
    sleep(15)
    lcd.text(lcd_line_2,2)
    sleep(45)

