int led1 = 13;
int led2 = 12;
int botao = 8;
int estadobotao = 0;
int contador = 0;

void setup () { 
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(8, INPUT);
}

void loop () {
  bool estadobotao = digitalRead(botao);
  
  if (estadobotao == 1) {
    contador ++;
  }
}

    
     