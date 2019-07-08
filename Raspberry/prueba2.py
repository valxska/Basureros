from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import sys
import RPi.GPIO as GPIO
#!/usr/bin/python3
from hx711 import HX711

pesoTemp = 0

class rasp_context():
    
    def get_w(self):
        hx711 = HX711(
        dout_pin=5,
        pd_sck_pin=6,
        channel='A',
        gain=64)
        hx711.reset()   
        measures = hx711.get_raw_data(times=20)
        prom=0

        for i in measures:
          prom=prom+i
          
        prom=prom/len(measures)
        
        peso= (prom*0.15)/-60411
                           
        GPIO.cleanup()  
        return peso
    
 
class MyServer(BaseHTTPRequestHandler):
    
    def set_peso(self,x):
        self._peso = x

    def get_peso(self):
        return self._peso
        
    def do_GET(self):
        
        serviceName = self.path
        print(serviceName)
        
        
        if serviceName == "initialize"
        
            myRasp = rasp_context()
            pesoTemp = myRasp.get_w()
            
            response = bytes("El peso actual es 0 kg","utf-8")
            self.wfile.write(response)

        
        
        elif serviceName == "get_w"

            a = rasp_context()
            b= a.get_w()
            eco = b*10
            print (b)
           
            val = '%.3f'%(b)
            va = '%.3f'%(eco)

            self.send_response(200)
            self.end_headers()
            self.send_header('Content-type','text/html')
            response = bytes("Peso: " +str(val),"utf-8")
            respons = bytes("Ecolon: " +str(va),"utf-8")
            respon = bytes("  \n","utf-8")
            self.wfile.write(response)
            self.wfile.write(respon)
            self.wfile.write(respons)
            
        else
            
            response = bytes("Error de conexión","utf-8")
            self.wfile.write(response)


hostName = ""
hostPort = 3001
myServer = HTTPServer((hostName,hostPort),MyServer)
#a = rasp_context()
#b= a.get_w()
#print (b)


try:
 
    myServer.serve_forever()
except:
    print(":(")
    