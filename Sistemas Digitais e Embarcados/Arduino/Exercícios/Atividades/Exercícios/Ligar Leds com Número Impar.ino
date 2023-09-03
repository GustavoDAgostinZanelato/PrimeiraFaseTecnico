int led1 = 13;
int botao1 = 9;
int botao2 = 8;
int botao3 = 11;
int estadoBotao1 = 0;
int estadoBotao2 = 0;
int estadoBotao3 = 0;


void setup () {
  pinMode (led1, OUTPUT);
  pinMode (botao1, INPUT);
  pinMode (botao2, INPUT);
  pinMode (botao3, INPUT);
}

void loop () {
  bool a = digitalRead(botao1);
  bool b = digitalRead(botao2);
  bool c = digitalRead(botao3);

  if ((a == 1) && (b == 1) && (c == 1)) {
  digitalWrite (led1, HIGH);
  } else {
  digitalWrite (led1, LOW); 
  }

  if ((a == 1) && (b == 0) && (c == 0)) {
  digitalWrite (led1, HIGH);
  } else {
  digitalWrite (led1, LOW);
  }

  if ((a == 0) && (b == 1) && (c == 0)) {
  digitalWrite (led1, HIGH);
  } else {
  digitalWrite (led1, LOW);
  }

  if ((a == 0) && (b == 0) && (c == 1)) {
  digitalWrite (led1, HIGH);
  } else {
  digitalWrite (led1, LOW);
  }
}