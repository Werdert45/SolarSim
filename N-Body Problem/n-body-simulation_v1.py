day = 60*60*24
# Constants
G = 6.67408e-11
dt = 0.1*day
au = 1.496e11
t = 0


class CelBody:
    def __init__(self, id, name, x0, y0, z0, vx0, vy0, vz0, mass, vector, ax0, ay0, az0, totalforcex, totalforcey, totalforcez):
        self.ax0 = ax0
        self.ay0 = ay0
        self.az0 = az0

        self.ax = self.ax0
        self.ay = self.ay0
        self.az = self.az0

        # Constants of nature
        # Universal constant of gravitation
        self.G = 6.67408e-11
        # Name of the body (string)
        self.id = id
        self.name = name
        # Initial position of the body (au)
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        # Position (au). Set to initial value.
        self.x = self.x0
        self.y = self.y0
        self.z = self.z0
        # Initial velocity of the body (au/s)
        self.vx0 = vx0
        self.vy0 = vy0
        self.vz0 = vz0
        # Velocity (au/s). Set to initial value.
        self.vx = self.vx0
        self.vy = self.vy0
        self.vz = self.vz0
        # Mass of the body (kg)
        self.M = mass
        # Short name
        self.vector = vector

        self.totalforcex = totalforcex
        self.totalforcey = totalforcey
        self.totalforcez = totalforcez


def force(planet1, planet2):
    totalforcex = []
    totalforcey = []
    totalforcez = []

    rx = planet1.x - planet2.x
    ry = planet1.y - planet2.y
    rz = planet1.z - planet2.z

    r3 = (rx ** 2 + ry ** 2 + rz ** 2) ** 1.5
    gravCons = G * planet1.M * planet2.M

    fx = -gravCons * rx / r3
    fy = -gravCons * ry / r3
    fz = -gravCons * rz / r3
    totalforcex.append(fx)
    totalforcey.append(fy)
    totalforcez.append(fz)

    forcex = sum(totalforcex)
    forcey = sum(totalforcey)
    forcez = sum(totalforcez)

    return forcex, forcey, forcez


def compute_one_body(planet1, planet2):
    ftot = force(planet1, planet2)
    ax = ftot[0]/planet1.M
    ay = ftot[1]/planet1.M
    az = ftot[2]/planet1.M

    vx = planet1.vx + ax*dt
    vy = planet1.vy + ay*dt
    vz = planet1.vz + az*dt

    planet1.x += vx*dt
    planet1.y += vy*dt
    planet1.z += vz*dt

    return planet1


# Change this part
def compute(bodies):
    new_bodies = []
    new_bodies.append(compute_one_body(bodies[0], bodies[1]))
    new_bodies.append(compute_one_body(bodies[1], bodies[0]))
    return new_bodies


# pretty format body
def pp(body):
    return '''%s
    x:%.6f
    y:%.6f
    z:%.6f''' % (body.name, body.x, body.y, body.z)

# MAIN
bodies = [
    CelBody(0, 'Sun', 1, 1, 1, 0, 0, 0, 1.989e30, 'sun', 0, 0, 0, 0, 0, 0),
    CelBody(1, 'Mercury', 1*au, 1, 1, 0, 29780, 0, 3.3e23, 'earth', 0, 0, 0, 0, 0, 0),
    ]

print("--- Start positions")
for body in bodies:
    print(pp(body))

for _ in range(365245):
    bodies = compute(bodies)

print("\n")
print("--- End positions")
for body in bodies:
    print(pp(body))
