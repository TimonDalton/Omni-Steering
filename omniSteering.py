import math

def getMotorOutput(in_x,in_y,rot,joystickDeadzone = 0,rotationDeadzone = 0):

    if abs(in_x) > 1 or abs(in_y) > 1 or abs(rot) > 1:
        print('the getMotorOutput function only allows input values between -1 and 1')
        return (0,0,0,0)

    if abs(in_x) < joystickDeadzone and abs(in_y) < joystickDeadzone:
        in_x = 0
        in_y = 0

    if abs(rot) < rotationDeadzone:
        rot = 0

    in_rad = (math.atan2(in_y,in_x) + math.pi*2) % (math.pi * 2)
    changed_rad = in_rad - math.pi/4

    if abs(in_x) > abs(in_y):
        normalize_scalar = abs(math.cos(in_rad))
    else:
        normalize_scalar = abs(math.sin(in_rad))

    size_scalar = math.sqrt((in_x**2) + (in_y**2))*normalize_scalar

    if abs(math.cos(changed_rad)) > abs(math.sin(changed_rad)) :
        out_x = (math.cos(changed_rad) /abs(math.cos(changed_rad))) * size_scalar
        out_y = (math.sin(changed_rad) /abs(math.cos(changed_rad))) * size_scalar
    else:
        out_x = (math.cos(changed_rad) /abs(math.sin(changed_rad))) * size_scalar
        out_y = (math.sin(changed_rad) /abs(math.sin(changed_rad))) * size_scalar    
    #the values are > 1 when the float incorrectly rounds up
    if abs(out_x) > 1:
        out_x = round(out_x)
    if abs(out_y) > 1:
        out_y = round(out_y)
    
    if (abs(rot) + abs(out_y) > 1 and abs(out_y) > abs(out_x)):
        scalar = 1/(abs(rot) + abs(out_y))
    elif abs(rot) + abs(out_x) > 1:
        scalar = 1/(abs(rot) + abs(out_x))
    else:
        scalar = 1
    
    m1 = (out_x + rot) * scalar
    m2 = (out_y + rot) * scalar
    m3 = (-out_x + rot) * scalar
    m4 = (-out_y + rot) * scalar

    return (m1,m2,m3,m4)

