#/usr/bin/python

# importing usb from PYUSB
import usb

#get busses
busses = usb.busses()


for bus in busses:
    devices = bus.devices
    for dev in devices:
        print "Device:", dev.filename
        print "  vendor id: %d (0x%05x)" % (dev.idVendor, dev.idVendor)
        print "  product id: %d (0x%05x)" % (dev.idProduct, dev.idProduct)
