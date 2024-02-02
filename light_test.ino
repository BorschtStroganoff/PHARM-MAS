#include <Adafruit_NeoPixel.h>

#define PIN            6  // The pin to which the Din of the RGB strip is connected
#define NUMPIXELS      16 // Number of NeoPixels in the strip

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600); // Initialize serial communication
  Serial.println("Setup started");
  
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}

void loop() {
  Serial.println("Loop started");

  // Turn on the RGB strip
  turnOnStrip();

  delay(2000); // Wait for 2 seconds

  // Turn off the RGB strip
  turnOffStrip();

  delay(2000); // Wait for 2 seconds
}


void turnOnStrip() {
  strip.fill(strip.Color(0,0, 255));
  strip.show();
}

void turnOffStrip() {
  strip.clear();
  strip.show();
}
