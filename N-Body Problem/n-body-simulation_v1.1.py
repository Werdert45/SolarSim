import numpy as np

day = 60*60*24
# Constants
G = 6.67408e-11
au = 1.496e11

class CelBody(object):
    # Constants of nature
    # Universal constant of gravitation
    def __init__(self, id, name, x0, v0, mass, color, lw):
        # Name of the body (string)
        self.id = id
        self.name = name
        # Mass of the body (kg)
        self.M = mass
        # Initial position of the body (au)
        self.x0 = np.asarray(x0, dtype=float)
        # Position (au). Set to initial value.
        self.x = self.x0.copy()
        # Initial velocity of the body (au/s)
        self.v0 = np.asarray(v0, dtype=float)
        # Velocity (au/s). Set to initial value.
        self.v = self.v0.copy()
        self.a = np.zeros([3], dtype=float)
        self.color = color
        self.lw = lw

# All Celestial Bodies

t = 0
dt = 0.1*day

Bodies = [
    CelBody(0, 'Sun', [0, 0, 0], [0, 0, 0], 1.989e30, 'yellow', 10),
    CelBody(1, 'Earth', [-1*au, 0, 0], [0, 29783, 0], 5.9742e24, 'blue', 3),
    CelBody(2, 'Venus', [0, 0.723 * au, 0], [ 35020, 0, 0], 4.8685e24, 'red', 2),
    ]

paths = [ [ b.x[:2].copy() ] for b in Bodies]

# loop over ten astronomical years
v = 0
while t < 10*365.242*day:
    # compute forces/accelerations
    for body in Bodies:
        body.a *= 0
        for other in Bodies:
            # no force on itself
            if (body == other): continue # jump to next loop
            rx = body.x - other.x
            r3 = sum(rx**2)**1.5
            body.a += -G*other.M*rx/r3

    for n, planet in enumerate(Bodies):
        # use the symplectic Euler method for better conservation of the constants of motion
        planet.v += planet.a*dt
        planet.x += planet.v*dt
        paths[n].append( planet.x[:2].copy() )
        #print("%10s x:%53s v:%53s"%(planet.name,planet.x, planet.v))
    if t > v:
        print("t=%f"%t)
        for b in Bodies: print("%10s %s"%(b.name,b.x))
        v += 30.5*day
    t += dt

plt.figure(figsize=(8,8))
for n, planet in enumerate(Bodies): 
    px, py=np.array(paths[n]).T; 
    plt.plot(px, py, color=planet.color, lw=planet.lw)
plt.show()
