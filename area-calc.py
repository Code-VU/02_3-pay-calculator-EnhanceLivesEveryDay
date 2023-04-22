# write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output:
# r = 1.1
# Area = 3.8013271108436504
# Use the following formula to calculate circle area: A = πr². 

my_pi = 3.141592653589793
my_radius = float(input("What is the radius of the circle: "))
my_radius = my_radius*my_radius

my_area = my_pi * my_radius

print (my_area)

# end assignment
