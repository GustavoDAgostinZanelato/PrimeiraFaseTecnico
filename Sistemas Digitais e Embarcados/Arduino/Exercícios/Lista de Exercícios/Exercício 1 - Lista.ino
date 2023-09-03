const int pin_led1 = 10;
const int pin_led2 = 11;
const int pin_botao1 = 2;
const int pin_botao2 = 3;
const int pin_botao3 = 4;

int conta = 0;
bool auxi = 0;
bool auxi2 = 0;

void setup() {

pinMode(pin_led1, OUTPUT);
pinMode(pin_led2, OUTPUT);
pinMode(pin_botao1, INPUT_PULLUP);
pinMode(pin_botao2, INPUT_PULLUP);
pinMode(pin_botao3, INPUT_PULLUP);
Serial.begin(9600);
}

void loop() {
//declaracao de pinos dentro do loop
bool botao1 = digitalRead(pin_botao1);
bool botao2 = digitalRead(pin_botao2);
bool botao3 = digitalRead(pin_botao3);

if(botao1 == false){
  if(auxi == 0){
  conta ++;
  auxi = 1;
  Serial.print("Vagas = ");
  Serial.println(conta);
  }
}
else{
  auxi = 0;
}
if(botao2 == false){
  if(auxi2 == 0){
  conta --;
  auxi2 = 1;
  Serial.print("Vagas = ");
  Serial.println(conta);
  }
}
else{
  auxi2 = 0;
}
if(conta<0){
  conta = 0;
}
if(conta>50){
  conta=50;
}
if(conta == 50){
  digitalWrite(pin_led2,1);
  digitalWrite(pin_led1,0);
}
if(conta<50){
  digitalWrite(pin_led2,0);
  digitalWrite(pin_led1,1);
}
if(botao3 == false){
  conta = 0;
}
}

