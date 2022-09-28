import bluetooth

nearby_device=bluetooth.discover_devices()

for bdaddr in nearby_device:
    print(bdaddr)
    print(bluetooth.lookup_name(bdaddr))