int led_esteiraM1 = 9;
int led_esteiraM2 = 8;
int led_limite  = 12;
int led_ligado = 13;
int botao_start = 7;
int botao_stop = 6;
int botaoS1 = 5;
int botaoS2 = 4;
int botaoS3 = 3;
int start = 0;
int stop = 0;
int stop2 = 0;
int S1 = 0;
int S2 = 0;
int S3 = 0;
int aux = 0;
int aux2 = 0;
int contador = 0;


void setup(){

  pinMode(led_esteiraM1, OUTPUT);
  pinMode(led_esteiraM2, OUTPUT);
  pinMode(led_limite, OUTPUT);
  pinMode(led_ligado, OUTPUT);
  pinMode(botao_start, INPUT);
  pinMode(botao_stop, INPUT);
  pinMode(botaoS1, INPUT);
  pinMode(botaoS2, INPUT);
  pinMode(botaoS3, INPUT);
  Serial.begin(9600);
}

void loop(){
  
  start = digitalRead(botao_start);
  stop = digitalRead(botao_stop);
  S1 = digitalRead(botaoS1);
  S2 = digitalRead(botaoS2);
  S3 = digitalRead(botaoS3);
  
  if ((start == 1) || (aux == 1)) {
    digitalWrite(led_ligado, HIGH);
  }
  
  if(S1 == HIGH){
    digitalWrite(led_esteiraM1, HIGH);
  }
  
  if(S2 == HIGH){
    digitalWrite(led_esteiraM2, HIGH);
    digitalWrite(led_esteiraM1, LOW);
  }
  
  if(S3 == HIGH){
    if(aux2 == 0){
    	digitalWrite(led_esteiraM2, LOW);
    	contador++;
      	aux2 = 1;
    }
  }
  else{
    aux2 = 0;
  
 while (contador >= 1) {
      digitalWrite(led_limite, HIGH);
      stop2 = digitalRead(botao_stop);
      if (stop2 == 1) {
        digitalWrite(led_ligado, 0);
        digitalWrite(led_limite, 0);
        aux = 0;
        contador = 0;
      }
    }
    
  if(stop == HIGH){
    digitalWrite(led_ligado, LOW);
    digitalWrite(led_limite, LOW);
    digitalWrite(led_esteiraM1, LOW);
    digitalWrite(led_esteiraM2, LOW);
  }
}
}
    
