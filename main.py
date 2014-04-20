import array
import sys
import usb.core
import usb.util

#Logitech mouse
VID = 0x046d
PID = 0xc05a
DATA_SIZE = 4

def takePhoto():
  pass

def mainloop(device,endpoint):
  #data = array.array('B',(0,)*4)
  #data[0] is mouse button data:
  # 0: mouseup
  # 1: L mouse down
  # 2: R mouse down
  # 4: middle mouse down
  while 1
    try:
      data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
      print data
      if data[0] in [1,2,4]: #A mouse click event was fired
        takePhoto()
    except usb.core.USBError as e:
      if e.args == ('Operation timed out',):
        print 'timeout'
        continue

def main():
  device = usb.core.find(idVendor = VID, idProduct = PID)
  if device is None:
    sys.exit("Could not find Logitech USB mouse.")

  # make sure the hiddev kernel driver is not active
  if device.is_kernel_driver_active(0):
    try:
      device.detach_kernel_driver(0)
    except usb.core.USBError as e:
      sys.exit("Could not detatch kernel driver: %s" % str(e))

  # set configuration
  try:
    device.reset()
    device.set_configuration()
  except usb.core.USBError as e:
    sys.exit("Could not set configuration: %s" % str(e))

  endpoint = device[0][(0,0)][0]

  mainloop(device,endpoint)

if __name__ == '__main__':
  main()