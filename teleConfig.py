#User input float.

a = float(input("Enter Stroke: "))
b = float(input("Enter Closed Length: "))
c = float(input("Enter Extended Length: "))
d = float(input("Enter Base Width: "))
e = float(input("Enter Base Pin Diameter: "))
f = float(input("Enter Rod Eye Width: "))
g = float(input("Enter Rod Pin Diameter: "))

#Conditional for MH100-53-84p
if (83 <= a <= 85 and 38 <= b <= 40) or (83 <= a <= 85 and 121 <= c <= 123) or (38 <= b <= 40 and 121 <= c <= 123) and d == 7 and e == 2 and f == 2 and g == 2:
    print('Order Part#MH100-53-84p')
else:
    print('No Match')


