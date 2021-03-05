# finding acceleration formula when intial velocity,final velocity,time taken is given.


def acceleration(final_velocity,intial_velocity,time):
    acceleration_formula=(final_velocity-intial_velocity)/time
    return acceleration_formula


# finding density


def density(mass,volume):
    density_formula=mass/volume
    return density_formula


# finding newton second law force=mass *acceleration.


def newton_second_law(mass,acceleration):
    force=mass*acceleration
    return force


# finding kinetic energy when mass of the body and velocity in which body is travelling is given.


def kinetic_energy(mass,velocity):
    kinetic=0.5*mass*velocity*velocity
    return kinetic


# finding average speed  when total distance travelled and total time taken is given.


def average_speed(distance,time):
    speed=distance/time
    return speed

# finding power when  work done and  time taken is given.


def power(work_done,time_taken):
    p=work_done/time_taken
    return p

# finding Ohms Law.


def Ohms_law(current,resistance):
    v=current*resistance
    return v

# finding gravitational force .m1 = mass of object1,m2 = mass of object 2,r = distance between objects.
# distance should be in meter and mass should be in kg


def gravitational_force(mass_of_object_1,mass_of_object_2,distance_between_objects):
    fg=((6.673*(10**-11))*mass_of_object_1*mass_of_object_2)/(distance_between_objects**2)
    return fg


# finding orbital velocity.
# G = gravitational constant= 6.673*(10**-11)


def orbital_velocity(gravitational_constant,mass,radius):
    orbit=((gravitational_constant*mass)/radius)**0.5
    return orbit


# finding acceleration due to gravity.
# M = mass of body , r = distance from the center of mass of body.
# G = gravitational constant = 6.673*(10**-11)


def acceleration_due_to_gravity(gravitational_constant,mass,distance):
    g=(gravitational_constant*mass)/(distance*distance)
    return g






