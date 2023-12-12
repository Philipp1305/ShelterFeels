const int love = 22;
const int fear = 25;
const int anger = 28;
const int sadness = 31;
const int happiness = 34;
const int surprise = 37;
const int disgust = 40;


/*int loveButtonLastState = HIGH;
int loveButtonActState = HIGH;*/
const int loveButton = 44;
int loveButtonState = 0;
int loveCounter = 0;

const int fearButton = 45;
int fearButtonState = 0;
int fearCounter = 0;


void countEmo(int& counter, int& buttonState, int buttonKind, int emotion){
  buttonState = digitalRead(buttonKind);

  if (buttonState == HIGH){
    counter += 1;
    Serial.println(counter);
    if (counter == 4){
      counter = 0;
    }
    delay(200);
  }

  switch (counter)
  {
    case 1:
      digitalWrite(emotion, HIGH);
      break;
    case 2:
      digitalWrite(emotion+1, HIGH);
      break;
    case 3:
      digitalWrite(emotion+2, HIGH);
      break;
    default:
      digitalWrite(emotion, LOW);
      digitalWrite(emotion+1, LOW);
      digitalWrite(emotion+2, LOW);
      break;
  }  
}

void setup() {
  Serial.begin(9600);
  for (int i = 22; i < 43; i++){
    pinMode(i, OUTPUT);
  };

  for (int i = 44; i <= 51; i++){
    pinMode(i,INPUT);
  };
  
}

void loop() {
  countEmo(loveCounter, loveButtonState, loveButton, love);
  countEmo(fearCounter, fearButtonState, fearButton, fear);
  /*
  countEmo(angerCounter, angerButtonState, angerButton, anger);
  countEmo(sadnessCounter, sadnessButtonState, sadnessButton, sadness);
  countEmo(happinessCounter, happinessButtonState, happinessButton, happiness);
  countEmo(surpriseCounter, surpriseButtonState, surpriseButton, surprise);
  countEmo(disgustCounter, disgustButtonState, disgustButton, disgust);
  */
}