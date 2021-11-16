x = int(input("Enter the x-coordinate "))
y = int(input("Enter the y-coordinate "))
Area_of_main_triangle = 300
A1 = abs(10*y - 30*x)
A2 = abs(20*y)
A3 = abs(600 - 10*y - 30*x)
Area_of_minor_triangle = 1/2*(A1 + A2 + A3)
if Area_of_main_triangle == Area_of_minor_triangle:
    print("Inside")
else:
    print("Outside")
