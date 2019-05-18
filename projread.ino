#include "MQ135.h"
MQ135 gasSensor = MQ135(A1);
void setup() {
  pinMode(A1, INPUT); 
  Serial.begin(9600);

}

void loop() {
  delay(3000);
  int svCO = analogRead(A0);  
  float sensorValueCO=(float)(3.027*exp(1.0698*(svCO*5.0/1023.0)))-2.0;
  float Co2ppm = gasSensor.getPPM()*100+100; 
  if(Co2ppm>900)
    delay(2000);
  if(sensorValueCO>9)
    delay(2000);
  
  String svC = String(sensorValueCO,2);
  String svA = String(Co2ppm,2);
  String val = svC + " " + Co2ppm;

  Serial.println(val);

}
