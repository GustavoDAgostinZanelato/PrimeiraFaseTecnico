int led1 = 2;
int botao = 10;
int estadobotao = 0;

void setup (){
  pinMode(led1, OUTPUT);
  pinMode(botao, INPUT);
  Serial.begin (115200);
}

void loop () {
  estadobotao = digitalRead(botao);
  
  if(estadobotao == HIGH) {
    digitalWrite(led1, HIGH);
  }else{
    digitalWrite(led1, LOW);
     Serial.print("Botão Pressionado");
  }
}
