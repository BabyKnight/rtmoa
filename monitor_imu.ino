#include "LSM6DS3.h"
#include "Wire.h"

//Create a instance of class LSM6DS3
LSM6DS3 myIMU(I2C_MODE, 0x6A);    //I2C device address 0x6A

void setup() {
    // Customize code, to run once:
    Serial.begin(9600);
    while (!Serial);
    //Call .begin() to configure the IMUs
    if (myIMU.begin() != 0) {
        Serial.println("[m] Device error");
    } else {
        Serial.println("[m] Device OK!");
    }
}

void loop() {
    //Accelerometer
    Serial.print("\n[m] Accelerometer(X,Y,Z):\n");
    Serial.print("[a]");

    Serial.print(myIMU.readFloatAccelX(), 4);
    Serial.print(",");
    Serial.print(myIMU.readFloatAccelY(), 4);
    Serial.print(",");
    Serial.print(myIMU.readFloatAccelZ(), 4);

    //Gyroscope
    Serial.print("\n[m] Gyroscope(X,Y,Z):\n");
    Serial.print("[g]");
    Serial.print(myIMU.readFloatGyroX(), 4);
    Serial.print(",");
    Serial.print(myIMU.readFloatGyroY(), 4);
    Serial.print(",");
    Serial.print(myIMU.readFloatGyroZ(), 4);

    delay(1000);
}
