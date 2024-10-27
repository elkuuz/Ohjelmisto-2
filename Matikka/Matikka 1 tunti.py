import numpy as np

print("Tehtävä 1 osa 1")

a=2.493
b=0.911

print(np.degrees(a))
print(np.degrees(b))


print("Tehtävä 1 osa 2")

c=137.7
d=62.3

print(np.radians(c))
print(np.radians(d))

print("Tehtävä 1 osa 3")

degs=[30, 45, 60, 90, 120, 135, 150, 180, 270, 360 ]

rads=[]

for deg in degs:
    rads.append(np.radians(deg))

for rad in rads:
    print(rad)

print("Tehtävä 2 hypotenuusa juttu")

f=1.6
g=2.3

h=np.hypot(f,g)

print(h)

#monke