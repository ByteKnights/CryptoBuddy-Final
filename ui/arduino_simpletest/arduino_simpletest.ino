#define butLeft A0
#define butRight A1
#define butOK A2

boolean butLeftLatched = false;
boolean butLReightLatched = false;
boolean butOKLatched = false;

int BUT_TOLERANCE = 512;


boolean pressedLeft() {
  if(analogRead(butLeft) >= BUT_TOLERANCE) {
    if(!butLeftLatched) {
      return true;
      butLeftLatched = true;
    } else {
      return false;
    }
  } else {
    butLeftLatched = false;
    return false;
  }
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(pressedLeft());
  delay(50);
}
