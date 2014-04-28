import array
import sys
import datetime
import usb.core
import usb.util
from SimpleCV import Camera

#Logitech mouse
VID = 0x046d
PID = 0xc05a
DATA_SIZE = 4

def takePhoto(cam):
  img = cam.getImage()
  img.save('photos/%s.png' % datetime.datetime.now().isoformat())
  print img

def mainloop(device,endpoint):
  #data = array.array('B',(0,)*4)
  #data[0] is mouse button data:
  # 0: mouseup
  # 1: L mouse down
  # 2: R mouse down
  # 4: middle mouse down
  prop_set = {
    'brightness': 10,
    'contrast': 11,
    'exposure': 15,
    'gain': 14,
    'height': 720,
    'hue': 13,
    'saturation': 12,
    'width': 1280,
  }

  cam = Camera(prop_set=prop_set)

  while 1:
    try:
      data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
      if data[0] in [1,2,4]: #A mouse click event was fired
        takePhoto(cam)
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
  print "Entering mainloop"
  mainloop(device,endpoint)

if __name__ == '__main__':
  main()
