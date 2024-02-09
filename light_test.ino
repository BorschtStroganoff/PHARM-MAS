#include <Adafruit_NeoPixel.h>

#define PIN            6  // The pin to which the Din of the RGB strip is connected
#define NUMPIXELS      16 // Number of pixels in the RGB strip

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600); // Initialize serial communication
  strip.begin();
  delay(100);
  strip.show(); // Initialize all pixels to 'off'
  Serial.println("Ready to accept inputs");
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      // Turn on the RGB strip
      Serial.println("Turning on lights");
      turnOnStrip();
    } else if (command == '0') {
      // Turn off the RGB strip
      Serial.println("Turning off lights");
      turnOffStrip();
    }
  }
}

void turnOnStrip() {
  strip.setBrightness(100);
  for (int i = 0; i < NUMPIXELS; i++) {
    strip.setPixelColor(i, 0, 255, 0); // Set color to red (adjust values for your desired color)
  }
  strip.show();
}

void turnOffStrip() {
  // for (int i = 0; i < NUMPIXELS; i++) {
  //   strip.setPixelColor(i, 0, 0, 0); // Set color to off
  // }
  strip.clear();
  strip.show();
  delay(10);
}
