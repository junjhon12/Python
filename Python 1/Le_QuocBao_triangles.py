#Acquirw user's input for the length of the three sides of a triangle
side_A = int(input("Please enter the length of side A of the triangle (in meters): "))
side_B = int(input("Please enter the length of side B of the triangle (in meters): "))
side_C = int(input("Please enter the length of side C of the triangle (in meters): "))

#Calculate the perimeter and area of the triangle
semi_perimeter = (side_A + side_B + side_C) / 2
area = pow(semi_perimeter * (semi_perimeter - side_A) * (semi_perimeter - side_B) * (semi_perimeter - side_C), 0.5)
perimeter = side_A + side_B + side_C

#Print the perimeter and area of the triangle
print(f'The perimeter of the triangle is {perimeter}m.')
print(f'The area of the triangle is {round(area, 10)}m^2.')

#Determine the type of the triangle
if pow(side_A, 2) + pow(side_B, 2) == pow(side_C, 2):
    print("It is a Right triangle.")
elif pow(side_A, 2) + pow(side_B, 2) > pow(side_C, 2):
    print("It is an Acute triangle.")
else:
    print("It is an Obtuse triangle.")


