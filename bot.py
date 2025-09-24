import meshtastic
import meshtastic.serial_interface
from pubsub import pub #this is the event/message bus system we snoop on

# even though it doesn't look like it, you need to make this connection, 
#the pubsub messages are a side effect of the interface

usb_connection = meshtastic.serial_interface.SerialInterface() #automatically tries to detect device and connect

def onReceiveText(packet, interface): 
    text = packet["decoded"]["text"]
    interface.sendText(f"echo: {text}")


pub.subscribe(onReceiveText, "meshtastic.receive.text") #tell the bus to use our callback whenever a packet is received

