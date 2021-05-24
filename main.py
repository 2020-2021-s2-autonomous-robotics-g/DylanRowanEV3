#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()
US = UltrasonicSensor(Port.S1)
LeftMotor = Motor(Port.A, positive_direction=Direction.CLOCKWISE, gears=None)
RightMotor = Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=None)
SpinMotor = Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)
drive = DriveBase(LeftMotor,RightMotor, 55, 203)

var = 1
escape_dist = 800
escape_ang = 360
while var > 0:
    if US.distance() < 500:
        drive.stop()
        while US.distance() < escape_dist:
            drive.drive(100,180)
            wait(10)
#            ev3.screen.print(US.distance())
#            print(US.distance(),',',drive.angle())
            SpinMotor.run(1080)
            ev3.speaker.beep()
#            if drive.angle() > escape_ang:
#                escape_dist = escape_dist - 200
#                escape_ang = escape_ang + 360
#                ev3.speaker.say('adjusting parameters')
        SpinMotor.stop()
#        escape_dist = 800
#        reset_angle
#        ev3.speaker.play_notes('C5/4_','C6/4')
    drive.drive(500, 0)
    print(US.distance())
