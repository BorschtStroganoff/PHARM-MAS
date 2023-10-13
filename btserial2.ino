/*
 * This program follows the program found in "Arduino Cookbook" very closely.
 * This is simply used for testing the HC-05 bluetooth module.
 * This program works with "btserial2.py"
 * This program alongside "btserial2.py" simply sends a message from the python program to the arduino.
 * Then, the arduino reads the message and sends it back to the Python program
 */

#include <SoftwareSerial.h>
const int rxpin = 10;
const int txpin = 11;
SoftwareSerial mySerial(rxpin,txpin);
#define BTSERIAL mySerial
#define BUFFER_SIZE 128

//String string = "";
char character_buffer[BUFFER_SIZE];
char myString[] = "Hello, Python!"; // Character array to send

void setup() {
  // put your setup code here, to run once:
  Serial.begin(38400);
  BTSERIAL.begin(38400);
  Serial.println("Serial Ready");
}

void loop() {
    String string = "";
    string = read_from_python();
    Serial.print(string);
    delay(1000);
    write_to_python(string);
    delay(500);
    

}

String read_from_python() {
    String string_buffer = "";
    while (BTSERIAL.available() <= 0) {
      delay(10);
    }

    while(1) {
      char c = (char) BTSERIAL.read();
//      Serial.println(c);
      if (c == '\n') {
        string_buffer += String('\n');
//        Serial.print(string_buffer);
        return string_buffer;
      }
      string_buffer += String(c);
    }
}

void write_to_python(String string_buffer) {
    string_buffer.toCharArray(character_buffer, BUFFER_SIZE);
//    Serial.println(character_buffer);

    BTSERIAL.write(character_buffer);
}
