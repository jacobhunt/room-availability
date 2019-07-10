// URL for getting room data
var ROOM_DATA_URL = "./getRooms"

// how often to check for updates (in units of milliseconds)
var CHECK_SERVER_INTERVAL = 10000;

// update the room availability table
function updateTable()
{
  $("#roomList").find("tr:gt(0)").remove();
  $.getJSON("./getRooms", function(data) {
      var roomStatusString = "";
      for(var i = 0; i < data.roomsArray.length; i++)
      {
        if(data.roomsArray[i].isOccupied)
        {
          roomStatusString = "<span class='redText'>OCCUPIED</span>"
        }
        else
        {
          roomStatusString = "<span class='greenText'>VACANT</span>"
        }

        $("#roomList tr:last").after(
          "<tr><td>" + data.roomsArray[i].name + "</td>" 
          + "<td>" + roomStatusString + "</td>" + "</tr>"
        );
        console.log(data);
      }

  }
)}

// once the document has loaded, regularly check the server for updates
// on the room status and update the table accordingly
$(document).ready(function()
{
  setInterval(updateTable, CHECK_SERVER_INTERVAL);
});
