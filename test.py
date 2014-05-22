#import packages
import points2 as p
import random
# set points
A = p.Point(3, -7, 8)
B = p.Point(-5, 4, 1)
C = p.Point(27, -40, 29)
d = random.sample(range(-100, 100), 3)
D = p.Point(d[0], d[1], d[2])
E = p.Point(1, 2, -1)
F = p.Point(0, 1, 5)
G = p.Point(-1, 2, 1)
H = p.Point(2, 1, 3)
# set vectors
X = p.Vector(-23, 43, 11)
AB = p.Vector()
AB.fromPoints(A, B)
AC = p.Vector()
AC.fromPoints(A, C)
# create point cloud
Cl = p.PointCloud(A, B, C, D, E, F, G, H)
# check all functions
p.help()
print("---------------------------Write point A------------------------")
A.write()
print("---------------------------Write vector AB---------------------")
AB.write()
print("---------------------------Define point A------------------------")
A.define()
print("----------------------------AB is collinear to AC---------------")
print(AB.collinearity(AC))
print("---------------------------A,B,C,D are not on the one line----------")
print(A.onLine(B, C, D))
print("---------------------------E,F,G,H are on the one plane----------")
print(E.onPlane(F, G, H))
print("---------------------------Write point cloud Cl----------")
Cl.write()
print("---------------------------Define point cloud Cl------------------------")
Cl.define()
