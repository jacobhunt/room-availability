# Room-Availability
A system that allows for users to find out if a given room is vacant utilizing sensors and a web app.
## Navigation
**HARDWARE-APP:** contains source code for the hardware portion of the project.   
**UI-APP:** contains source code for the server and client portion of the project.

## Build Guide    

### Web App
Coming Soon   
### Hardware Device
Materials needed: 
* Raspberry Pi 
* Passive Infrared (PIR) Sensor
* Jumper Wires (Female-to-female wires are the easiest option. male-to-female wires will also work)
* Breadboard (if using male-to-female wires)

If you flip the PIR Sensor upside-down and look at the pins sticking out, you should see VCC, GND, and OUT printed on the circuit board.
These represent the Voltage, Ground, and Input/Output respectively. Connect these pins to the Raspberry Pi GPIO Pins.
I used Pin #'s 2, 6, and 16 for my implementation.

After that, you're all hooked up! load PIR-model.py onto your Pi and then run it!
