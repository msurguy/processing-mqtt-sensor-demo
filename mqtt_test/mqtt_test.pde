// This sketch displays a circle with the size corresponding to the value of the 
// resistor reading that's coming from MQTT channel called "a0"

// By Maksim Surguy
// May 2018

import mqtt.*;

MQTTClient client;
int a0; // this variable will store the sensor readings from MQTT

void setup() {
  size(400,400);
  background(255);
  fill(0);

  client = new MQTTClient(this);
  client.connect("mqtt://localhost", "processing");
  client.subscribe("a0");
}

void draw() {
  background(255);
  // Draw a circle in the middle of the screen, reducing the dimensions by factor of 20
  ellipse(width/2, height/2, a0/20, a0/20);
}

void messageReceived(String topic, byte[] payload) {
  println("new message: " + topic + " - " + new String(payload));

  // Update the value in a0 with the integer value of the sensor reading within MQTT packet
  a0 = Integer.parseInt(new String(payload));
}