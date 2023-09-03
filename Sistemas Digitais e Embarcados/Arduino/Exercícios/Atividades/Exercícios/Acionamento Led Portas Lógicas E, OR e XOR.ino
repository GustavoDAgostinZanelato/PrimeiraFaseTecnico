int led1 = 13;
int led2 = 12;
int led3 = 11;
int botao1 = 9;
int botao2 = 8;
int estadoBotao1 = 0;
int estadoBotao2 = 0;

void setup () {
  pinMode (led1, OUTPUT);
  pinMode (led2, OUTPUT);
  pinMode (led3, OUTPUT);
  pinMode (botao1, INPUT);
  pinMode (botao2, INPUT);
}

void loop () {
  bool a = digitalRead(botao1);
  bool b = digitalRead(botao2);
  
  if ((a == 1) && (b == 1)) {
    digitalWrite (led1, HIGH);
  } else {
  digitalWrite (led1, LOW);
  }

  if ((a == 1) || (b == 1)) {
    digitalWrite (led2, HIGH);
  } else {
  digitalWrite (led2, LOW);
  }

  if ((a == 1) ^ (b == 1)) {
    digitalWrite (led3, HIGH);
  } else {
  digitalWrite (led3, LOW);
  }
}