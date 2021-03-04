# finding acceleration formula when intial velocity,final velocity,time taken is given.
# In this formula v=final velocity u=intial velocity t=time


def acceleration(v,u,t):
    acceleration_formula=(v-u)/t
    return acceleration_formula


# finding density formula when mass of the body and volume of the body given. m=mass and v=volume.


def density(m,v):
    density_formula=m/v
    return density_formula


# finding newton second law force=mass *acceleration.


def newton_second_law(m,a):
    f=m*a
    return f


# finding kinetic energy when mass of the body and velocity in which body is travelling is given. m=mass and v=velocity.


def kinetic_energy(m,v):
    ke=0.5*m*v*v
    return ke


# finding average speed  when total distance travelled and total time taken is given. d=distance and t=time.


def average_speed(d,t):
    S=d/t
    return S

# finding power when  work done and  time taken is given. W=work done and t=time taken.


def power(W,t):
    P=W/t
    return P

# finding Ohms Law.I=Current flowing through conductor and R=resistance


def Ohms_law(I,R):
    V=I*R
    return V

# finding gravitational force .m1 = mass of object1,m2 = mass of object 2,r = distance between objects.
# r should be in meter and m1 and m2 should be in kg


def gravitational_force(m1,m2,r):
    fg=((6.673*(10**-11))*m1*m2)/(r**2)
    return fg


# finding orbital velocity.M = mass of the body at center and in most cases M is the weight of the earth
# R = radius of orbit
# G = gravitational constant= 6.673*(10**-11)


def orbital_velocity(G,M,R):
    Vorbit=((G*M)/R)**0.5
    return Vorbit


# finding acceleration due to gravity.
# M = mass of body , r = distance from the center of mass of body.
# G = gravitational constant = 6.673*(10**-11)


def acceleration_due_to_gravity(G,M,r):
    g=(G*M)/(r*r)
    return g







