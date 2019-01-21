from math import ceil

day = 60*60*24
# Constants
G = 6.67408e-11
dt = 0.00001*day
au = 1.496e8
t = 0

class CelBody:
    def __init__(self, id, name, x0, y0, vx0, vy0, mass, vector, ax0, ay0):
        # Constants of nature
        # Universal constant of gravitation
        self.G = 6.67408e-11
        # Name of the body (string)
        self.id = id
        self.name = name
        # Initial position of the body (au)
        self.x0 = x0
        self.y0 = y0

        # Position (au). Set to initial value.
        self.x = self.x0
        self.y = self.y0

        # Initial velocity of the body (au/s)
        self.vx0 = vx0
        self.vy0 = vy0

        # Velocity (au/s). Set to initial value.
        self.vx = self.vx0
        self.vy = self.vy0

        # Mass of the body (kg)
        self.M = mass
        # Short name
        self.vector = vector

        self.ax0 = ax0
        self.ay0 = ay0


        self.ax = self.ax0
        self.ay = self.ay0

# id, name, x0, y0, vx0, vy0, mass, vector,ax0,ay0
Bodies = [
    CelBody(0,'Sun',0,0*au,0,0,1.989e30,'sun',0,0),
    CelBody(1,'Mercury',0,0.39*au,47870,0,3.3e23,'merc',0,0),
    CelBody(2,'Venus',0,0.723*au,35.02,0,4.87e24,'venu',0,0),
    ]

leftover = []

time = 10

for t in range(time):
    # Define all of the positions beforehand
    for planet in range(len(Bodies)):
        name = str(Bodies[planet].name)


    for n in range(len(Bodies)):
        planetinit = Bodies[n]
        templistx = []
        templisty = []

        # first get all of the objects because otherwise it is calculated with the next values

        for x in range(len(Bodies)):
            if planetinit != Bodies[x]:
                r2 = ((Bodies[x].x - Bodies[n].x)*au + (Bodies[x].y - Bodies[n].y)*au)**2
                gravconst = G*Bodies[n].M*Bodies[x].M
                rx = (Bodies[x].x - Bodies[n].x)
                ry = (Bodies[x].y - Bodies[n].y)
                fx = (gravconst/r2)*rx
                fy = (gravconst/r2)*ry
                templistx.append(fx)
                templisty.append(fy)

        forcex = sum(templistx)
        forcey = sum(templisty)

        templistx.clear()
        templisty.clear()

        ax = forcex/planetinit.M
        ay = forcey/planetinit.M

        vx = planetinit.vx + ax*dt
        vy = planetinit.vy + ay*dt

        x = planetinit.x + vx*dt
        y = planetinit.y + vy*dt

        # Adding this information to the class
        planetinit.x = x
        planetinit.y = y
        planetinit.vx = vx
        planetinit.vy = vy
        planetinit.ax = ax
        planetinit.ay = ay

time = (time*dt)/3153600
time = str(round(time, 3))

for output in range(len(Bodies)):
    print("The planet %s is at position (%s,%s) at time %s years" % (Bodies[output].name, Bodies[output].x, Bodies[output].y, time))
