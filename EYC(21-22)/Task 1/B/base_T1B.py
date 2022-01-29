import cv2
import numpy as np
from pyzbar.pyzbar import decode

import sim

# close all opened connections
sim.simxFinish(-1) 
# Connect to CoppeliaSim
client_id = sim.simxStart('127.0.0.1',19997,True,True,5000,5) 

# Start simulation
return_code = sim.simxStartSimulation(client_id, sim.simx_opmode_oneshot_wait) 
# Wait for last commnad send to arrive
sim.simxGetPingTime(client_id) 

# Get vision sensor handler
re, v_sensor = sim.simxGetObjectHandle(client_id, 'vision_sensor', sim.simx_opmode_oneshot_wait) 
# Get image from vision sensor
return_code, image_resolution, vision_sensor_image = sim.simxGetVisionSensorImage(client_id, v_sensor, 0, sim.simx_opmode_blocking) 

print(f'RC: {return_code} IR: {image_resolution}')

# Process retrived image from sensor
transformed_image = np.array(vision_sensor_image, dtype=np.uint8)
transformed_image.resize([image_resolution[1], image_resolution[0], 3])
transformed_image = cv2.flip(transformed_image, 0)
transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_RGB2BGR)

# Detect QR codes
barcodes = decode(transformed_image)

# Display QRs
for barcode in barcodes:
    cv2.rectangle(transformed_image, barcode.polygon[0], barcode.polygon[2], (255, 0, 255), 2)
    data = barcode.data.decode("utf-8")
    c_x = barcode.rect.left + (barcode.rect.width//2)
    c_y = barcode.rect.top + (barcode.rect.height//2)
    cv2.circle(transformed_image, (c_x, c_y), 4, (0, 0, 255), 4)
    xp = barcode.rect.left + barcode.rect.width + 10
    cv2.putText(transformed_image, data, (xp, c_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 100, 0), 2)

cv2.imshow("img", transformed_image)    

cv2.waitKey(0)
cv2.destroyAllWindows()

# Stop simulation
return_code = sim.simxStopSimulation(client_id, sim.simx_opmode_oneshot_wait) 

sim.simxGetPingTime(client_id)
sim.simxFinish(client_id)


# [b'Greetings', b'e-Yantra', b'Team !!', b'from', b'Student !!', b'Hello']