int led1 = 13;
unsigned long tempo_anterior = 0;
const unsigned long intervalo_tempo = 1000; //de quanto em quanto tempo o led vai ligar e desligar

void setup () {
  pinMode(13, OUTPUT);
}

void loop () {
  
  unsigned long var_tempo = millis(); //atribuindo valor de millis a uma variável
  
  if(var_tempo - tempo_anterior > intervalo_tempo){  //quando der 1000ms ele vai ligar o led
    digitalWrite(led1, HIGH); 
    tempo_anterior = var_tempo; //agora como o tempo_anteiro é mil, somente quando bater 2000ms que o led vai ligar novamente
  }else{
    digitalWrite(led1,LOW);
  }
}

//a partir do momento que eu executo o programa, o contador do millis inicia contado de 1ms em 1 ms