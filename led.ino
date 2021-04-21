#include <GSM.h>
int data;

void setup() {
  Serial.begin(9600);//initialize serial
  pinMode(LED_BUILTIN, OUTPUT);//make the led pin(13) as the output
  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("hi");

}

void loop() {
  while (Serial.available()){
    data =Serial.read();
    
  }
  if (data=='1')
  digitalWrite(LED_BUILTIN,HIGH);

  else if (data=='0')
  digitalWrite(LED_BUILTIN,LOW);
  Serial.println("AT+CMGF=1");    //To send SMS in Text Mode
  delay(1000);
  Serial.println("AT+CMGS=\"Mobile Number\"\r"); //Change to destination phone number 
  delay(5000);
  Serial.println("ALERT!unknown person");//the content of the message
  delay(200);
  Serial.println((char)26); //the stopping character Ctrl+Z
  delay(1000); 
  break; 
/
}
