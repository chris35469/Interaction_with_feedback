import cyberpi
import time

def touch_sensor_interaction():
    while True:
        touch_value = cyberpi.pocket.read_digital("s2")  
        if touch_value > 0.5:
            cyberpi.led.on('green') 
            cyberpi.console.println("Touched!")
           
        else:
            cyberpi.led.on('red')  
            cyberpi.console.println("Not Touched")

touch_sensor_interaction()
