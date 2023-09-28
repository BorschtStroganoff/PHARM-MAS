/*
 * Note: This code requires the Adafruit Neopixel library
 * Note: Associated with a tinkercad file https://www.tinkercad.com/things/geZed6catwZ?sharecode=e85x4xt01RLKJn0-JfepLQIl7uWGnyHJw1_Cbc8NIvM
 * 
 * This is the code for a digital prototype for the shelf system
 */

#include <Adafruit_NeoPixel.h>
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

// These variables define which pins are connected to the RGB strips
#define BOX1_PIN 12
#define BOX2_PIN 2
#define BOX3_PIN 3
#define BOX4_PIN 4

#define DRAWER1_PIN 8
#define DRAWER2_PIN 9

// This number represents how many pixels are on the strips.
// In the actual project, this value would be closer to 30 or so
// TODO: change value of NUMPIXELS to number of pixels being used in the boxes
#define NUMPIXELS 4

//Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
//#define DELAYVAL 500

Adafruit_NeoPixel box1(NUMPIXELS, BOX1_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel box2(NUMPIXELS, BOX2_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel box3(NUMPIXELS, BOX3_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel box4(NUMPIXELS, BOX4_PIN, NEO_GRB + NEO_KHZ800);

int box;
int drawer;

void setup() {
  Serial.begin(9600);
  
  #if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
  #endif

  // TODO change this to the four boxes
  box1.begin();
  box2.begin();
  box3.begin();
  box4.begin();
}

void loop() {

  while(Serial.available() <= 0) {
    delay(10);
  }

  // read from the UI which box to open
  box = Serial.readString().toInt();
  Serial.println(box);

  int is_close = 0;
  if (box < 0) {
    is_close = 1;
    box *= -1;
  }
  // determine which drawer the box is in.
  switch(box) {
    case 1:
    case 2:
      drawer = 1;
      break;

    case 3:
    case 4:
      drawer = 2;
      break;

    default:
      drawer = 0;
      break;
    }

    if (is_close) {
      darkenBox(box);
    }
    else {
      openDrawer(drawer);
      lightBox(box);
      delay (5000);
      box2.clear();
    }
  }

  //TODO: write UDFs for

  void openDrawer(int drawer)
  {
    switch (drawer){
      case(1):
        digitalWrite(DRAWER1_PIN ,HIGH);
        delay(1000);
        digitalWrite(DRAWER1_PIN, LOW);
        break;

      case(2):
        digitalWrite(DRAWER2_PIN, HIGH);
        delay(1000);
        digitalWrite(DRAWER2_PIN, LOW);
        break;
    }
  }

  void lightBox(int box)
  {
    Adafruit_NeoPixel box_rgb;
    
    switch(box){
      case 1:
        box_rgb = box1;
        break;
      case 2:
        box_rgb = box2;
        break;
      case 3:
        box_rgb = box3;
        break;
      case 4:
        box_rgb = box4;
        break;
    }
    
    int i;
    for (i=0; i < NUMPIXELS; i++) {
      box_rgb.setPixelColor(i, box_rgb.Color(0, 150, 0));
      box_rgb.show();
  }
  }

  void darkenBox(int num)
  {
    Adafruit_NeoPixel box_rgb;
    
    switch(box){
      case 1:
        box_rgb = box1;
        break;
      case 2:
        box_rgb = box2;
        break;
      case 3:
        box_rgb = box3;
        break;
      case 4:
        box_rgb = box4;
        break;
    }

    box_rgb.clear();
    box_rgb.show();
  }
