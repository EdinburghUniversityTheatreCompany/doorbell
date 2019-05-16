#include <ESP8266WiFi.h>
char ssid[] = "SSID";
char pass[] = "WIFI PASSWORD";
IPAddress doorbell_host(192,168,0,56);

WiFiClient client;

void setup() {
  Serial.begin(115200);
  Serial.println();
  Serial.println("hi");
  ring();
  Serial.println("sleeping");
  ESP.deepSleep(0); 
}

void ring(){
  Serial.print("Connecting");
  WiFi.begin(ssid, pass);
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());
  client.connect(doorbell_host,9001);
  client.print("ding");
}

void loop() {
}
