int pinI1=5;//定义I1接口
int pinI2=6;//定义I2接口
int speedpin=11;//定义EA(PWM调速)接口
void setup()
{
  pinMode(pinI1,OUTPUT);//定义该接口为输出接口
  pinMode(pinI2,OUTPUT);
  pinMode(speedpin,OUTPUT);
}
void loop()
{ 
  analogWrite(speedpin,100);//输入模拟值进行设定速度
  delay(2000);
  digitalWrite(pinI2,LOW);//使直流电机顺时针转，沉入水中
  digitalWrite(pinI1,HIGH);
  analogWrite(speedpin,100);
  delay(2000);
  
  digitalWrite(pinI1,LOW);//在水中游行时间，开启监视
  digitalWrite(pinI2,LOW);
  delay(2000);
  
  digitalWrite(pinI2,HIGH);//使直流电机逆时针转，浮出水面
  digitalWrite(pinI1,LOW);
  analogWrite(speedpin,100);
  delay(2000);
  
  digitalWrite(pinI1,LOW);//在水面上进行人脸扫描检测
  digitalWrite(pinI2,LOW);
  delay(2000);

}
