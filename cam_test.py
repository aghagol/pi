import picamera
import time
import mover

camera = picamera.PiCamera()

# camera.capture('image1.jpg')
# sleep(5)
# camera.capture('image2.jpg')

# camera.sharpness = 0
# camera.contrast = 0
# camera.brightness = 50
# camera.saturation = 0
# camera.ISO = 0
# camera.video_stabilization = False
# camera.exposure_compensation = 0
# camera.exposure_mode = 'auto'
# camera.meter_mode = 'average'
# camera.awb_mode = 'auto'
# camera.image_effect = 'none'
# camera.color_effects = None
# camera.rotation = 0
# camera.hflip = False
# camera.vflip = False
# camera.crop = (0.0, 0.0, 1.0, 1.0)


camera.start_recording('out.h264')
time.sleep(1)
mover.forward(55)
time.sleep(1)
mover.rotate_right(50)
time.sleep(1)
mover.forward(55)
time.sleep(1)
mover.backward(55)
time.sleep(1)
mover.stop()
time.sleep(1)
camera.stop_recording()




