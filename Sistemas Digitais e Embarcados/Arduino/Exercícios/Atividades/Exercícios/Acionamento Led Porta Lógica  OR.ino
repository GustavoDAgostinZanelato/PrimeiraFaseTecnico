int led = 13;
int botao = 11;
int botao2 = 10;
int estadoBotao = 0;
int estadoBotao2 = 0;

void setup ()
{
pinMode (led, OUTPUT);
pinMode (botao, INPUT);
pinMode (botao2, INPUT);
}

void loop () 
{
  estadoBotao = digitalRead(botao);
  estadoBotao2 = digitalRead(botao2);
  
  if (estadoBotao == HIGH) {
    digitalWrite (led, HIGH);
  } else {
    digitalWrite (led,LOW);
  }
  
  if (estadoBotao2 == HIGH) {
    digitalWrite (led, HIGH);
  } else {
    digitalWrite (led,LOW);
  }
}