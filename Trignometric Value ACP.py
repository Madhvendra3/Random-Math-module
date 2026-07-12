import math

angle = float(input("Enter the angle in degrees: "))

radian = math.radians(angle)

sin_value = math.sin(radian)
cos_value = math.cos(radian)
tan_value = math.tan(radian)

print("Sin =", sin_value)
print("Cos =", cos_value)
print("Tan =", tan_value)