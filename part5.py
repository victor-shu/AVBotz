import time;


def get_height(n):
    desiredHeight = n
    return desiredHeight


ticks = time.time()
currentHeight = ticks*thrust

kp = 1.0
ki = 1.0
kd = 1.0

error = desiredHeight-currentHeight
lasterror = error
totalerror = 0
while (height != desiredHeight):
    totalerror += error
    d = error - lasterror

    proportional = error*kp
    integral = totalerror*ki
    derivative = d*kd

    height = proportional + integral + derivative
    lasterror = error

    def set_thrust(thrust):
        thrust = height

