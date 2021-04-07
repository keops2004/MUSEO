//******************************************************************
// Programas desarrolados para el Museo de Ciencias y Tecnologia
// (MUCYT). Dicha entidad se reserva el derecho de reproducir, modificar
// y autorizar el uso de dichos programas para cualquier fin distinto
// al educativo y que sea en beneficio cientifico-tecnologico de la nacion
// venezolana.
// De igual forma se prohibe la comercializacion de dicho producto al ser
// de origen softwarelibre y hardwarelibre. 
//
//                      copyleft  INTEDAS  Venezuela-2014
//*******************************************************************
#include <Keypad.h>

const byte ROWS = 4; //four rows
const byte COLS = 4; //three columns
char keys[ROWS][COLS] = {
  {'A','B','C','W'},
  {'D','E','F','X'},
  {'G','H','I','Y'},
  {'*','J','#','Z'}
};
byte rowPins[ROWS] = {13, 12, 11, 10}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {9, 8, 3, 2}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

// Pines de conexion de los LED

int LedWebc_Pro = 4; // WEBCAM
int LedSemR_Pro = 6; //************************
int LedSemA_Pro = 5; // SEMAFORO
int LedSemV_Pro = 7; //************************

// Pines de conexion analogicos e inicializacion de valores 


const int PinPres = 0;
int ValorPres = 0;

const int PinoLumi = 1;
int ValorLumi = 0;

const int PinTemp = 2;
int ValorTemp = 0;

const int PinSoni = 3;
int ValorSoni = 0;

// Inicializacion de valores del cronometro (semaforo)
   // colores de 1 a 9   posiciones de 1 a 3
int rojo = 0;
int amarillo = 0;
int verde = 0;
int posi = 0;
int i = 0;
int j = 0;
char key = '#';

void setup() {
  Serial.begin(9600);
  pinMode(LedWebc_Pro, OUTPUT); 
  pinMode(LedSemR_Pro, OUTPUT); 
  pinMode(LedSemA_Pro, OUTPUT); 
  pinMode(LedSemV_Pro, OUTPUT); 

}

void loop() {
  
 char keypack = keypad.getKey();
      

    
     if (keypack){
         
         if (keypack == 'A' || 'B' || 'C' || 'D' || 'E' || 'F' && key != '#'){
         key = '#';
         //break;
         }
  
         if (keypack == 'G' || 'H' || 'I' || 'J' || '*' && key == 'G' || 'H' || 'I' || 'J' || 'D'){
         key = keypack;
        // break;
         }

         if (keypack == 'A' || 'B' || 'C' || 'D' || 'E' || 'F' && key == '#'){        
         key = keypack;
        // break;
         }

         if (keypack == '#' && key == 'A' || 'B' || 'C' || 'D' || 'E' || 'F' ||'G' || 'H' || 'I' || 'J' || '*'){        
         key = keypack;
        // break;
         }

     }
  
    


 switch (key) {
  case  'A':  
   if (j ==0 ){ 
    Serial.println('A');
    j = 1; }
    
    delay(400);
    ValorTemp = map(analogRead(PinTemp), 0, 1023, 0, 255); 
    Serial.println(ValorTemp);
    break;

  case  'B':  
   if (j ==0 ){
    Serial.println('B');
    j = 1;}
    
    delay(400);  
    digitalWrite(LedWebc_Pro, HIGH);
    break;

  case  'C': 
   if (j ==0 ){
    Serial.println('C'); 
    j = 1;}
    
    delay(400);
    ValorPres = map(analogRead(PinPres), 0, 1023, 0, 255); 
    Serial.println(ValorPres);
    break;

  case  'D':  
   if (j ==0 ){ 
    Serial.println('D'); 
    j = 1;}
    
    delay(400);

    rojo = 0;
    amarillo = 0;
    verde = 0;
    posi = 0;
    i = 1;
    break;

  case  'E':    
   if (j ==0 ){
    Serial.println('E'); 
    j = 1;}
    
    delay(400);
    ValorLumi =  map(analogRead(PinoLumi), 0, 1023, 0, 255); 
    Serial.println(ValorLumi);
    break;

  case  'F':  
   if (j ==0 ){
    Serial.println('F'); 
    j = 1;}
    
    delay(400);
    ValorSoni = map(analogRead( PinSoni), 0, 1023, 0, 255);
    Serial.println(ValorSoni);
    break;

  case  'G':    
     if (posi == 1) {
       rojo = rojo - 1;

       if(rojo < 1) {
        rojo = 1;}
       Serial.println(rojo); }

     if (posi == 2) {
       amarillo = amarillo - 1;
       if(amarillo < 1){
        amarillo = 1;}
       Serial.println(amarillo); }

     if (posi == 3) {
       verde = verde - 1;
       if(verde < 1){
        verde = 1;}
       Serial.println(verde); }
       
    delay(100);
    break;

  case  'H':    
    posi = posi + 1;
    if(posi > 3){
        posi = 1;}
    Serial.println(posi);
    break;

  case  'I':    
    if (posi == 1) {
       rojo = rojo + 1;
       if(rojo > 9) {
        rojo = 9; }
       Serial.println(rojo); }

     if (posi == 2) {
       amarillo = amarillo + 1;
       if(amarillo > 9){
        amarillo = 9;}
       Serial.println(amarillo); }

     if (posi == 3) {
       verde = verde + 1;
       if(verde > 9) {
        verde = 9;}
       Serial.println(verde); }
    delay(100);   
    break;

  case  'J':    
    posi = posi - 1;
    if(posi < 1) {
        posi = 3;}    
    Serial.println(posi);
    delay(100);
    break;

  case  '*':    
 if (i = 1) {
    digitalWrite(LedSemR_Pro, HIGH);   
    delay(rojo*1000);               
    digitalWrite(LedSemR_Pro, LOW); 
    delay(100);

    digitalWrite(LedSemA_Pro, HIGH);   
    delay(amarillo*1000);      
    digitalWrite(LedSemA_Pro, LOW);    
    delay(100); 
    
    digitalWrite(LedSemV_Pro, HIGH);   
    delay(verde*1000);               
    digitalWrite(LedSemV_Pro, LOW); 
           }
    break;

  case  '#':    
    Serial.println('#');

    digitalWrite(LedSemR_Pro, LOW); 
    digitalWrite(LedSemA_Pro, LOW);              
    digitalWrite(LedSemV_Pro, LOW); 
    digitalWrite(LedWebc_Pro, LOW);
    rojo = 0;
    amarillo = 0;
    verde = 0;
    i = 0;
    j = 0;
    break;
  
  } 

delay(10);
  
}
