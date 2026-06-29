#include <SoftwareSerial.h>

SoftwareSerial BT(10, 11); // RX, TX

const int LED = 9; // PWM pin

void setup() {
  pinMode(LED, OUTPUT);

  Serial.begin(9600);
  BT.begin(9600);

  Serial.println("Bluetooth Slider LED Control");
  Serial.println("Waiting for values (0-255)...");
}

void loop() {
  if (BT.available()) {

    int brightness = BT.read(); // Read one byte (0-255)

    analogWrite(LED, brightness);

    Serial.print("Brightness = ");
    Serial.println(brightness);
  }
}
