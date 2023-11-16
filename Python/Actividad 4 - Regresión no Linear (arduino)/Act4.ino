void setup() {
  //double valor;
  
  Serial.begin(9600);
  while(!Serial){}
}

void loop() {
  double a0 = analogRead(A0);
  // Para simular las lecturas de algun sensor
  double data[5];
  
  for(int i=0; i<5; i++) {
    data[i] = a0;
  }

  // Para enviar datos
  String data2send = "", s = ",";

  for(int i=0; i<5; i++) {
    data[i] = data[i]*(0.0048875855327);
    data2send = data2send + data[i] + s;
  }
  
  Serial.println(data2send);
  
  delay(500);
}
