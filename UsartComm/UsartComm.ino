void setup() {
  // put your setup code here, to run once:
  Serial.begin(19200);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    String data = Serial.readStringUntil('\n');
    if(data == "close"){
    digitalWrite(8,HIGH);
    delay(7000);
    digitalWrite(8,LOW);
    Serial.println("closed");
    //Serial.flush();
    }
    else if(data == "open") {
      digitalWrite(7,HIGH);
      delay(7000);
      digitalWrite(7,LOW);
      Serial.println("opened");
      //Serial.flush();
    }
  }
  
 // Serial.println("Hello from arduino!");
  //delay(3000);

}
