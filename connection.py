import sys
import meshtastic.ble_interface as ble
import io

devices = ble.BLEInterface.scan()
i=0
for d in devices:
    print(f"{i}) {d}")
    i+=1

choice = int(input("select by number: "))
print(devices[choice].address)

interface = ble.BLEInterface(devices[choice].address, debugOut=io.StringIO())
# interface.connect(devices[choice].address)
input()