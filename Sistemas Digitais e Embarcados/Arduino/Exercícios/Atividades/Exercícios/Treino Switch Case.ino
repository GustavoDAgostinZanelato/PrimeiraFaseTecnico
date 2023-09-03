int led1 = 12;
int led2 = 11;
int led3 = 10;

void setup () {
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  Serial.begin(115200);
}

void loop () {
  
  char comando = Serial.read ();
  
  switch(comando) {
    case '1':
    digitalWrite(led1, HIGH);
    break;
    
    case '2':
    digitalWrite(led2, HIGH);
    break;
    
    case '3': 
    digitalWrite(led3, HIGH);
    break;
    
    case 'A':
    digitalWrite(led1, LOW);
    break;
    
    case 'B':
    digitalWrite(led2, LOW);
    break;
    
    case 'C':
    digitalWrite(led3, LOW);
    break;
  }
}