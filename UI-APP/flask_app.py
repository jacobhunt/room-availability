import os
from flask import Flask, render_template, request, jsonify

# class to represent rooms
class Room:
    def __init__(self, name, isOccupied):
        self.name = str(name)
        self.isOccupied = bool(isOccupied)

    def serialize(self):
        return {
            'name': self.name,
            'isOccupied': self.isOccupied
        }

# array to contain room instances
rooms = []

# object for python server application
app = Flask(__name__)

# set the secret key
app.secret_key = "8975917845yhiWUEFHYDFU*(#@!$73RYUIAWGDF"

# root page
@app.route("/")
def index():
    return render_template(
        "index.html",
        rooms = [room.serialize() for room in rooms]
    )

# http route for setting status of a room (i.e. whether or not it is occupied) 
@app.route("/setRoomStatus")
def setRoomStatus():

    # get remote input from an HTTP "post" request
    if request.method == "POST":
        requestData = request.form
        req_name = str(request.form.get("name"))
        req_isOccupied = request.form.get("isOccupied")
    
    # get remote input from an HTTP "get" request
    if request.method == "GET":
        requestData = request.args
        req_name = str(request.args.get("name"))
        req_isOccupied = request.args.get("isOccupied")
    
    # parse the "isOccupied" portion of HTTP request
    try:
        if int(req_isOccupied) == 0:
            req_isOccupied = False
        elif int(req_isOccupied) == 1:
            req_isOccupied = True
        else:
            return(jsonify(
                success = False,
                returnMessage = "Invalid input in HTTP request: " + 
                                " isOccupied must be either '0' or '1' (no serverside exception)",
                HTTPRequestData = requestData
            ))
    except:
            return(jsonify(
                success = False,
                returnMessage = "Invalid input in HTTP request: " + 
                                " isOccupied must be either '0' or '1' (serverside exception)",
                HTTPRequestData = requestData
            ))

    # variable to indicate whether or not room already exists in "rooms" array
    isRoomAlreadyInArray = False
    
    # set the status for the room based on remote input if the room is already
    # in the "rooms" array
    for room in rooms:
        if room.name == req_name:
            room.isOccupied = req_isOccupied
            isRoomAlreadyInArray = True

    # add room and status to the "rooms" array if it is not already in array
    if not isRoomAlreadyInArray:
        rooms.append(Room(req_name, req_isOccupied))

    # construct mesasge to be returned in JSON package
    returnMessage = "Room " + req_name + " is now listed as "
    if req_isOccupied:
        returnMessage += "occupied"
    elif not req_isOccupied:
        returnMessage += "not occupied"
    else:
        # req_isOccupied should be either True of False; if not, 
        # something went wrong, so notify machine making HTTP request
        returnMessage = "Oh no! Something went wrong! Bad input?"
        return jsonify(
            success = False,
            returnMessage = returnMessage,
        )
    

    # send back a JSON object
    return(
        jsonify(
            # HTTP request was successful
            success = True,
            
            # message for the machine which made HTTP request
            returnMessage = returnMessage,

            # array of room data in memory
            roomsArray = [room.serialize() for room in rooms]
        )
    )


# configure server
server_address = "0.0.0.0"
port_number = 8080

# run server
if __name__ == "__main__":
    app.run(host = os.getenv('IP', server_address), 
            port = int(os.getenv('PORT', port_number)))
