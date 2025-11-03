
#include <Servo.h>
Servo arm;
int servoPin = 9;   // servo signal
int potPin = A0;    // potentiometer input
int ledPin = 11;     // LED to show cleaning
void setup() {
  Serial.begin(9600);
  arm.attach(servoPin);
  pinMode(ledPin, OUTPUT);
  arm.write(0);  // start at rest
  Serial.println("Solar Cleaner Robot Ready!");
}
void loop() {
  int dustLevel = analogRead(potPin);  // read simulated dust
  Serial.print("Dust Level: ");
  Serial.println(dustLevel);

  if (dustLevel > 600) {  // threshold for dirty panel
    Serial.println("Panel dirty! Starting cleaning...");
    digitalWrite(ledPin, HIGH);
    arm.write(90);   // move arm to clean
    delay(2000);     // cleaning time
    arm.write(0);    // back to rest
    digitalWrite(ledPin, LOW);
    Serial.println("Cleaning done!");
    delay(4000);     // short delay before checking again
  } else {
    Serial.println("Panel clean. No action.");
    delay(2000);
  }
}
