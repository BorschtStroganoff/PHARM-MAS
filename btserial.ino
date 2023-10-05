/*
 * This program follows the program found in "Arduino Cookbook" very closely.
 * This is simply used for testing the HC-05 bluetooth module.
 * This program works with "btserial.py"
 */

#include <SoftwareSerial.h>
const int rxpin = 10;
const int txpin = 11;
SoftwareSerial mySerial(rxpin,txpin);
#define BTSERIAL mySerial

void setup() {
  // put your setup code here, to run once:
  Serial.begin(38400);
  BTSERIAL.begin(38400);
  Serial.println("Serial Ready");
  BTSERIAL.println("Bluetooth ready");

  pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (BTSERIAL.available())
  {
    char c = (char)BTSERIAL.read();
    Serial.println(c);
  }
//  if (Serial.available())
//  {
//    char c = (char)Serial.read();
//    BTSERIAL.write(c);
//  }
}
