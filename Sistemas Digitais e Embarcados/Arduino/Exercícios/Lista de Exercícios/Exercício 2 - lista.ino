int led_ligado = 13;
int led_esteira = 11;
int botao_start = 7;
int botao_stop = 6;
int sensorS4 = 5;
int sensorS3 = 4;
int sensorS2 = 3;
int sensorS1 = 2;
int start = 0;
int stop = 0;
int stop2 = 0;
int S1 = 0;
int S2 = 0;
int S3 = 0; //snesor baixo
int S4 = 0; //sensor alto
int aux = 0;
int aux2 = 0;

void setup (){
  pinMode(led_ligado, OUTPUT);
  pinMode(botao_start, INPUT);
  pinMode(botao_stop, INPUT);
  pinMode(sensorS1, INPUT);
  pinMode(sensorS2, INPUT);
  pinMode(sensorS3, INPUT);
  pinMode(sensorS4, INPUT);
}

void loop (){
  start = digitalRead(botao_start);
  stop = digitalRead(botao_stop);
  S1 = digitalRead(sensorS1);
  S2 = digitalRead(sensorS2);
  S3 = digitalRead(sensorS3); //baixo
  S4 = digitalRead(sensorS4); //alto
  
  if((start == HIGH) || (aux == 1)){
    digitalWrite(led_ligado, HIGH);
    delay(2000);
  }
  
  if(S4 == HIGH){
    digitalWrite(led_esteira, HIGH);
  }
  
  if(S1 == HIGH){
    digitalWrite(led_esteira, LOW);
  }
  if(S3 == HIGH){
    digitalWrite(led_esteira, HIGH);
  }
  
  if(S2 == HIGH){
    digitalWrite(led_esteira, LOW);
  }

  while(aux ==1) {
     digitalWrite(led_ligado, HIGH);
     stop2 = digitalRead(botao_stop);
     if (stop2 == 1) {
       digitalWrite(led_ligado, 0);
       aux = 0;
     }
  }
  if(stop == HIGH){
    digitalWrite(led_esteira, LOW);
    digitalWrite(led_ligado, LOW);
  }
}    
