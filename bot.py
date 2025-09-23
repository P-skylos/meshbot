import meshtastic
import meshtastic.serial_interface
from pubsub import pub #this is the event/message bus system we snoop on

usb_connection = meshtastic.serial_interface.SerialInterface() #automatically tries to detect device and connect

def onReceive(packet): 
    print(packet)

pub.subscribe(onReceive, "meshtastic.receive.text") #tell the bus to use our callback whenever a packet is received