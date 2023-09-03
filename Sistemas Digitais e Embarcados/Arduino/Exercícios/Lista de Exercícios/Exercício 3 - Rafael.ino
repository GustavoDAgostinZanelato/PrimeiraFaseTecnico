/* ************************************************************************

Colégio SATC
Curso Técnico em Informática
Disciplina: Sistemas Embarcados
Turma: 1190
Professor: Marcos Antonio Jeremias Coelho

Programa: Exercício 1 - Esteira de montagem

Autor: Rafael Teixeira Serafim e Rafael Avila Benincá
Data: 21/06/2023
Versão: 1.0

************************************************************************ */

// Definindo variáveis
const int pin_botao1 = 7; // Botão start
const int pin_botao2 = 6; // Botão S1
const int pin_botao3 = 5; // Botão S2
const int pin_botao4 = 4; // Botão S3
const int pin_botao5 = 3; // Botão stop
const int pin_led1 = 13; // led ligado
const int pin_led2 = 12; // led M1
const int pin_led3 = 11; // led M2
const int pin_led4 = 10; // led limite
bool start = false;
bool s1 = false;
bool s2 = false;
bool s3 = false;
bool stop = false;
bool stop2 = false; // Lê botão stop dentro do while
bool aux = 0; // Auxiliar para botão start
bool aux2 = 0; // Auxiliar para contador
int contador = 0; // Contador do limite

void setup() {
  // Definindo entradas e saídas
  pinMode(pin_botao1, INPUT_PULLUP);			
  pinMode(pin_botao2, INPUT_PULLUP);			
  pinMode(pin_botao3, INPUT_PULLUP);			
  pinMode(pin_botao4, INPUT_PULLUP);			
  pinMode(pin_botao5, INPUT_PULLUP);
  pinMode(pin_led1, OUTPUT);
  pinMode(pin_led2, OUTPUT);
  pinMode(pin_led3, OUTPUT);
  pinMode(pin_led4, OUTPUT);
}

void loop() {
  // Lê o estado dos botões
  start = !digitalRead(pin_botao1);
  s1 = !digitalRead(pin_botao2);
  s2 = !digitalRead(pin_botao3);
  s3 = !digitalRead(pin_botao4);
  stop = !digitalRead(pin_botao5);

  // Verifica se start foi pressionado
  if ((start == 1) || (aux == 1)) {  // || significa or 
    aux = 1;
    // Liga o led "ligado"
    digitalWrite(pin_led1, 1);

    // Verifica se S1 foi pressionado
    if (s1 == 1) {
      // Liga M1
      digitalWrite(pin_led2, 1);
    }
    // Verifica se S2 foi pressionado
    if (s2 == 1) {
      // Liga M2 e desliga M1
      digitalWrite(pin_led2, 0);
      digitalWrite(pin_led3, 1);
    }
    // Verifica se S3 foi pressionado
    if (s3 == 1) {
      if (aux2 == 0) {
        // Desliga M2 e adiciona 1 ao contador
        digitalWrite(pin_led3, 0);
        contador++;
        aux2 = 1;
      }
    }
    else {
      aux2 = 0;
    }
    // Se chegar ao limite, liga o led "limite", lê somente o botão stop e verifica se foi pressionado
    while (contador >= 5) {
      digitalWrite(pin_led4, 1);
      stop2 = !digitalRead(pin_botao5);
      if (stop2 == 1) {
        digitalWrite(pin_led1, 0);
        digitalWrite(pin_led4, 0);
        aux = 0;
        contador = 0;
      }
    }
    // Verifica se stop foi pressionado. Se foi: desliga os leds e reseta as variáveis
    if (stop == 1) {
      digitalWrite(pin_led1, 0);
      digitalWrite(pin_led2, 0);
      digitalWrite(pin_led3, 0);
      digitalWrite(pin_led4, 0);
      contador = 0;
      aux = 0;
    }
  }
}
