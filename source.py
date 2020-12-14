import math

Manning_number = dict([
                       ('Asphalt', 0.016),
                       ('Brass',	0.011),
                       ('Brick', 0.015),
                       ('Ductile Iron', 0.012),
                       ('Clay Tile', 0.014),
                       ('Concrete', 0.013),
                       ('Copper', 0.011),
                       ('Corrugated Metal', 0.022),
                       ('Galvanized Iron', 0.016),
                       ('Glass', 0.010),
                       ('Gravel', 0.023),
                       ('Lead', 0.011),
                       ('Masonry', 0.025),
                       ('Plastic', 0.009),
                       ('Steel', 0.012),
                       ('Wood', 0.012)
])

Units = input('Units US or SI: ')
if Units == 'US':
    Conversion_factor = float(1.49)
elif Units == 'SI':
    print('Convert units to US')
else:
    raise ValueError('Invalid Input! Units must be US')

Design_flowrate = float(input('Storm Drain Design Flowrate in cfs: '))

Slope = input('Slope Based on Topographic Conditions (N/A if not given): ')
if Slope == 'N/A':
    Length = float(input('Length of pipe: '))
    Head_loss = float(input('Headloss: '))
    Slope = Head_loss / Length
    print(Slope)
else:
    Slope = float(Slope)

Pipe_material = input('Pipe Material: ')
if Pipe_material not in Manning_number:
  raise ValueError("Invalid Input! Material not found")

Friction_factor = Manning_number[Pipe_material]

def calc_diameter(Q, k, S, n):
    """ Returns the pipe diameter given the 
    units, design flowrate, slope, and Manning's number.
    """
    return ((Q * n * (4 ** (5/3))) / (math.pi * k * (S  ** (1/2)))) ** (3/8)

Calcualted_diameter = calc_diameter(float(Design_flowrate), Conversion_factor, Slope, Friction_factor)
Diameter_inches = Calcualted_diameter * 12

print('The calculated diameter is:', Calcualted_diameter, 'ft')
print('The calculated diameter is:', Diameter_inches, 'inches')

def pipe_diameter(d):
    """ Returns the required pipe diameter that would used for the storm drain
     given the calculated diameter in inches.
    """
    if d <= 4:
      d =  4 
    elif d > 4 and d <= 6:
      d = 6
    elif d > 6 and d <= 8:
      d = 8
    elif d > 8 and d <= 10:
      d = 10
    elif d > 10 and d <=12:
      d = 12
    elif d > 12 and d <= 15:
      d = 15
    elif d > 15 and d <= 18:
      d = 18
    elif d > 18 and d <= 21:
      d = 21
    elif d > 21 and d <= 24:
      d = 24
    elif d > 24 and d <= 27:
      d = 27
    elif d > 27 and d <= 30:
      d = 30
    elif d > 30 and d <= 36:
      d = 36
    elif d > 36 and d <= 42:
      d = 42
    elif d > 42 and d <= 48:
      d = 48
    elif d > 48 and d <= 54:
      d = 54
    elif d > 54 and d <= 60:
      d = 60
    elif d > 60 and d <= 66:
      d = 66
    elif d > 66 and d <= 72:
      d = 72
    elif d > 72 and d <= 84:
      d = 84
    elif d > 84 and d <= 90:
      d = 90     
    return d

Required_diameter = pipe_diameter(Diameter_inches)
print('For this storm drain a pipe of', Required_diameter, 'inches should be purchased')


def max_flowrate(d, k, S, n):
    """ Returns the maximum flowrate of the pipe purchased
    """
    return (k / n) * (math. pi * (((d / 12) ** 2) / 4)) * (((d / 12) / 4) ** (2 / 3)) * (S ** (1 / 2))

Qmax = max_flowrate(Required_diameter, Conversion_factor, Slope, Friction_factor)

print('The maximum flowrate of the pipe is', Qmax, 'cfs')

def max_velocity(Q, d):
    """ Returns the maximum velocity given the maximum flowrate 
    and pipe diameter
    """
    return Q / (math. pi * (((d / 12) ** 2) / 4))

Vmax = max_velocity(Qmax, Required_diameter)

print('The maximum velocity of the pipe is', Vmax, 'ft/s')
