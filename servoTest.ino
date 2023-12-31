/*
 * This file was used in testing openining and closing the box lid using a servo
 * This simply opens and closes the box over and over again
 * 
 * Note: This program only works on standard servos (angled shaft servos)
 *       Rotation servos will only keep spinning.
 */

#include <Servo.h>

#define CLOSE_ANGLE 0
#define OPEN_ANGLE 90

Servo servo1;  // represents the servo in box 1
int x;

// Function to open the lid of the box. Argument is the servo we wish to move.
void open_lid(Servo servo);
// Function to close the lid of the box. Argument is the servo we wish to move.
void close_lid(Servo servo);



void setup() {
  servo1.attach(9);  // attaches servo1 to pin 9
  Serial.begin(9600);
}


void loop() {
  while(Serial.available() ==0){
    delay(10);
  }

  x = Serial.readString().toInt();

  if (x == 1) {
    open_lid(servo1);
  }

  if (x == 0) {
    close_lid(servo1);
  }
  
  delay(2000);
}

void open_lid(Servo servo)
{
  servo.write(OPEN_ANGLE);
}

void close_lid(Servo servo)
{
  servo.write(CLOSE_ANGLE);
}
