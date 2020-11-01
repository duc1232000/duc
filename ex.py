import math
x = float (input("nhap gia tri x "))
y = float (input("nhap gia tri y ")) 
z = float (input("nhap gia tri z "))
f = (x+y+z)/(x**2+y**2+1)-abs(x*math.cos(y))
print ('Gia tri của F = '+str(f))
