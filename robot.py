from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
from threading import Timer
import math
#add another motor
hub = MSHub()
motor = Motor('A')

paper_scanner = ColorSensor('F')

color = paper_scanner.get_ambient_light()*10


def darkMode():
    while True:
        if color > 100: 
         color = paper_scanner.get_ambient_light()*10
         motor.run_to_position(50, 'clockwise', 100)
         motor.run_to_position(0, 'counterclockwise', 100)
         motor.run_to_position(5, 'shortest path', 100)
d = Timer(60.0, darkMode)
 
d.start()
while True:
    
    color = paper_scanner.get_ambient_light()*10
    print(color)
    
    if color < 130:
       motor.run_to_position(50, 'clockwise', 100)
       motor.run_to_position(0, 'counterclockwise', 100)

       #motor.run_to_position(27, 'shortest path', 100)
       #motor.run_to_position(5, 'shortest path', 100)
       #motor.run_to_degrees_counted(1, 100)
  
    

