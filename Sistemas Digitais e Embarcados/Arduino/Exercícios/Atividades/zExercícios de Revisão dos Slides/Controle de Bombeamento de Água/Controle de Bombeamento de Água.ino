int led1 = 13;
int botao1 = 9;
int botao2 = 8;
int estadoBotao1 = 0;
int estadoBotao2 = 0;

void setup () {
  pinMode (led1, OUTPUT);
  pinMode (botao1, INPUT);
  pinMode (botao2, INPUT);
}

void loop () {
  bool a = digitalRead(botao1);
  bool b = digitalRead(botao2);
    
  if ((a == 1) or (b == 1)) {
    digitalWrite (led1, LOW);
  } else {
    digitalWrite (led1, HIGH);
  }
}