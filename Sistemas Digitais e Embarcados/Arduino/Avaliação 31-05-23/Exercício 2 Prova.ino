//Dando nomes as variáveis:
int led1 = 11;
int botao = 2;
int estadobotao = 0;
int ultimoestado = 0;
int contador = 0;

//Definindo a função de cada pino + valor serial
void setup (){
  pinMode(11, OUTPUT);
  pinMode(2, OUTPUT);
  Serial.begin(115200);
}

//Caso o valor seja par, o led apaga. Se for impar, acende
void loop() {
  
  estadobotao = digitalRead(botao);
  
  if(estadobotao != ultimoestado) {
    if(estadobotao == HIGH){
    }else{
      contador++;
      
      Serial.print("Contador: ");
      Serial.print(contador);
    }
    
    ultimoestado = estadobotao;
    
    if((contador % 2)==0){
      digitalWrite(led1, LOW);
    }else{
      digitalWrite(led1, HIGH);
    }
  }
}