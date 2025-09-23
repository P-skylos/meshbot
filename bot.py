import meshtastic
import meshtastic.serial_interface
from pubsub import pub #this is the event/message bus system we snoop on

# usb_connection = meshtastic.serial_interface.SerialInterface() #automatically tries to detect device and connect

def onReceiveText(packet, interface): 
    print(packet)

def onReceivePacket(packet, interface): #for testing
    print(packet)

# pub.subscribe(onReceiveText, "meshtastic.receive.text") #tell the bus to use our callback whenever a packet is received

pub.subscribe(onReceivePacket, "meshtastic.receive")