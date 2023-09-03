//Dando nomes as variáveis:
int led1 = 13;
int led2 = 12;
int led3 = 11;
int led4 = 10;
int botaoA = 7;
int botaoB = 6;
int botaoC = 5;
int botaoD = 4;
int estadobotaoA = 0;
int estadobotaoB = 0;
int estadobotaoC = 0;
int estadobotaoD = 0;

//Definindo a função de cada pino
void setup () {
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(7, INPUT);
  pinMode(6, INPUT);
  pinMode(5, INPUT);
  pinMode(4, INPUT);
}

void loop () {
  
  //variáveis dos botões
  estadobotaoA = digitalRead(botaoA);
  estadobotaoB = digitalRead(botaoB);
  estadobotaoC = digitalRead(botaoC);
  estadobotaoD = digitalRead(botaoD);
  
  //Funções botão A:
  if(estadobotaoA == HIGH) {
    digitalWrite(led4, HIGH);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, HIGH);
  }else{
    digitalWrite(led4, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
  }
  
  //Funções botão B:
  if(estadobotaoB == HIGH) {
    digitalWrite(led4, HIGH);
  }else{
    digitalWrite(led4, LOW);
  }
  
  //Funções botão C:
  if(estadobotaoC == HIGH) {
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
  }else{
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
  }
  
  //Funções botão D:
  if(estadobotaoD == HIGH) {
    digitalWrite(led1, HIGH);
    digitalWrite(led4, HIGH);
  }else{
    digitalWrite(led1, LOW);
    digitalWrite(led4, LOW);
  }
  
  //Função para o desligamento da bomba de enchimento
  if(estadobotaoB == HIGH && estadobotaoC == HIGH && estadobotaoD == HIGH) {
    digitalWrite(led1, LOW);
  }
  
  //Função para ativar o alarme
   if(estadobotaoA == HIGH && estadobotaoB == HIGH && estadobotaoC == HIGH) {
    digitalWrite(led4, LOW);
  }
}
    