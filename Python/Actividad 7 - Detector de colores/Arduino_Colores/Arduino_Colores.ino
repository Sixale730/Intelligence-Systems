int R = 7;
int G = 6;
int B = 5;
int A0_in = A0;

int R_val = 0, G_val = 0, B_val = 0, RGB_val = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(R, OUTPUT);
  pinMode(G, OUTPUT); 
  pinMode(B, OUTPUT); 

  digitalWrite(R, LOW);
  digitalWrite(G, LOW);
  digitalWrite(B, LOW);
  
  Serial.begin(9600);
  while(!Serial){}
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(R, HIGH);
  delay(40);
  R_val = analogRead(A0_in);
  delay(10);
  digitalWrite(R, LOW);
  
  digitalWrite(G, HIGH);
  delay(40);
  G_val = analogRead(A0_in);
  delay(10);
  digitalWrite(G, LOW);

  digitalWrite(B, HIGH);
  delay(40);
  B_val = analogRead(A0_in);
  delay(10);
  digitalWrite(B, LOW);

  digitalWrite(R, HIGH);
  digitalWrite(G, HIGH);
  digitalWrite(B, HIGH);
  delay(40);
  RGB_val = analogRead(A0_in);
  delay(10);
  digitalWrite(R, LOW);
  digitalWrite(G, LOW);
  digitalWrite(B, LOW);

  String s = ",";
  Serial.println(R_val + s + G_val + s + B_val + s + RGB_val + s);
  
  delay(100);
}
