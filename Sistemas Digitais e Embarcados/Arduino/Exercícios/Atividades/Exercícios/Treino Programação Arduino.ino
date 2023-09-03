int led1 = 13;
int led2 = 12;
int led3 = 11;
int led4 = 10;
int botao = 9;
int botao2 = 8; 
int estadobotao = 0;
int estadobotao2 = 0;

void setup () {
 pinMode(13, OUTPUT);
 pinMode(12, OUTPUT);
 pinMode(11, OUTPUT);
 pinMode(10, OUTPUT);
 pinMode(9, INPUT);
 pinMode(8, INPUT);
 
}
  
void loop () {
  estadobotao = digitalRead(botao);
  estadobotao2 = digitalRead(botao2);
  
  if (estadobotao == HIGH){
    digitalWrite (led1, HIGH);
    delay (200);
    digitalWrite (led2, HIGH);
    delay (200);
    digitalWrite (led3, HIGH);
    delay (200);
    digitalWrite (led4, LOW);
  } else {
    digitalWrite (led1, LOW);
    delay (200);
    digitalWrite (led2, LOW);
    delay (200);
    digitalWrite (led3, LOW);
    delay (200);
    digitalWrite (led4, HIGH);
  }
  
  if (estadobotao2 == HIGH) {
    digitalWrite (led4, HIGH);
    delay (50);
    digitalWrite (led4, LOW);
    delay (50);
  }
}