import sys
import meshtastic.ble_interface as ble

client = ble.BLEClient()
devices = client.discover()
i = 0
for d in devices:
   print(f"{i}) {d}")
   i+=1

choice = int(input("select device by number: "))

chosen = devices[choice].address
print(chosen)
client.address=chosen
client.connect()

# print(ble.BLEClient.scan()) #docs say static method but it doesnt seem to exist when i try it
