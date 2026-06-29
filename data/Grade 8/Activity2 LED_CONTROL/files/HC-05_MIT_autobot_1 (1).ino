#include <SoftwareSerial.h>

SoftwareSerial BT(10, 11); // 10: txd, 11:rxd

char Incoming_value = 0;

void setup()
{
  Serial.begin(9600);   // For debugging
  BT.begin(9600);       // HC-05 communication

  pinMode(13, OUTPUT);  // LED
}

void loop()
{
  if (BT.available())
  {
    Incoming_value = BT.read();

    Serial.print("Received: ");
    Serial.println(Incoming_value);

    if (Incoming_value == '1')
    {
      digitalWrite(13, HIGH);
      Serial.println("LED ON");
    }

    else if (Incoming_value == '0')
    {
      digitalWrite(13, LOW);
      Serial.println("LED OFF");
    }
  }
}                                                                                                                                 