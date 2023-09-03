int led1 = 9;
int led2 = 8;
int led3 = 7;

void setup () {
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  Serial.begin(9600);
}

void loop () {
  
  char comando = Serial.read ();
  
  switch (comando) {
    case "A":
    digitalWrite(led1, HIGH);
    break;
    
    case "B:
    digitalWrite(led2, HIGH);
    break;
    
    case 3:
    digitalWrite(led3, HIGH);
    break;
  }
}
  