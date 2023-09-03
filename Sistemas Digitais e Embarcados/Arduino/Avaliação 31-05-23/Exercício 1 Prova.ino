//Dando nomes as variáveis:
int led1 = 11;
int led2 = 12;
int botao1 = 2;
int botao2 = 3;
int estadobotao1 = 0;
int estadobotao2 = 0;

//Definindo a função de cada pino
void setup () {
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
}

//Botão 1 acende e 2 apaga. Botão 2 acende e 1 apaga
void loop () {
  estadobotao1 = digitalRead(botao1);
  estadobotao2 = digitalRead(botao2);
  
  if(estadobotao1 == HIGH) {
    digitalWrite(led1, HIGH);
    digitalWrite(led2, LOW);
  }
  
  if(estadobotao2 == HIGH) {
    digitalWrite(led2, HIGH);
    digitalWrite(led1, LOW);
  }
}
