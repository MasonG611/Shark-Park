void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(5, OUTPUT);
  pinMode(7, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(5, HIGH);
  Serial.println("5 High");
  delay(3000);
  digitalWrite(5, LOW);
  Serial.println("5 Low");
  digitalWrite(7, HIGH);
  Serial.println("7 High");
  delay(3000);
  digitalWrite(7, LOW);
}
