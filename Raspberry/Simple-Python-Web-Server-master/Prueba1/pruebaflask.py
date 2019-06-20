import time
import sys
import RPi.GPIO as GPIO
#!/usr/bin/python3
from hx711 import HX711

    
def funcion_medida():
   
    try:
        hx711 = HX711(
            dout_pin=5,
            pd_sck_pin=6,
            channel='A',
            gain=64
        )

        hx711.reset()   # Before we start, reset the HX711 (not obligate)
        measures = hx711.get_raw_data(times=20)
    finally:
        GPIO.cleanup()  # always do a GPIO cleanup in your scripts!
    
    prom=0
    
    for i in measures:
      prom=prom+i
      
    prom=prom/len(measures)
    
    peso= (prom*0.15)/-60411
    #print (peso)
  
    return peso
            

if __name__=="__main__":
    
    app.run(port = 3000, debug=True)
    





