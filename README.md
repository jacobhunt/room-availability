# Room-Availability
A system that allows for users to find out if a given room is vacant utilizing sensors and a web app.
## Navigation
**HARDWARE-APP:** contains source code for the hardware portion of the project.   
**UI-APP:** contains source code for the server and client portion of the project.

## Build Guide    

### Web App
The first thing to do is upload the contents of the "UI-APP" folder to a web host that supports server-side Python scripting. I used pythonanywhere.com, as it is free for small apps that don't use a lot of CPU power or get a lot of web traffic (Heroku would probably be another good option). If you're using pythonanywhere.com, then you'll want to unpack the folder's contents into the "/mysite" directory on the pythonanywhere computer.

Next, you want to make sure that your Python host has all of the necessary dependencies installed (see "import" statements at the top of "flask-app.py"). For pythonanywhere.com, you can use a browser-based BASH terminal from inside your account to run "pip install".

Now, you want to configure your web-host to run "flask_app.py" as the main web-app. Different hosts have different processes for this; for pythonanywhere, you go to the "web" tab in your account dashboard and click on the "add a new web app" button. When it asks you to pick a Python web framework, click on "flask." Then, it will ask you which version of Python to use (it may or may not matter for this app, but I selected version 3.5).

At this point, you may need to reupload "flask_app.py", as pythonanywhere may have deleted it and replaced it with its own "hello world" type app. After you do this, go to the web tab and click the "reload" button.

At this point, things should be up and running! If you have any server errors, the "error log" file will be very helpful for debugging (uninstalled dependencies was the main issue I ran into when trying to get the app up and running).

The room-status list may be updated via HTTP requests to the "http://{WEBSITE_ROOT_URL}/setRoomStatus" URL using the parameters "name" (string to represent the name of room) and "isOccupied" (a "1" or a "0" for "occupied" or "vacant", respectively). The hardware app (for the Raspberry-PI sensor machines) already has the code to make these requests built into it.

As this was a short-deadline hackathon project for demonstration/proof-of-concept purposes, the app is IN NO WAY SECURE in its present form. Perhaps the most obvious security vulnerability is the lack of authentication for setting a room's status. In the app's current form, it is not difficult to alter the text of the room-status table via the address-bar of a web-browser (which could potentially include injecting links to malicious scripts into the HTML file which gets sent to end-users). If the app were to be deployed for practical use, this vulnerability (and possibly others) would need to be fixed first (see "issues" page of GitHub repository).

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
