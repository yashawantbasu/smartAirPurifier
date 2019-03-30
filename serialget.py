import time
import serial

      
ser = serial.Serial(              
               port='/dev/ttyACM0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )
counter=0
          
def get_x():
        y=ser.readline()
        x=y.decode("utf-8")
        #print(type(x))
        #print(x)
        #time.sleep(1)
        return x

        
        
