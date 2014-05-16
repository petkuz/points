#import packages
import points as p
import random
#set points
A = p.create(3,-7,8)
B = p.create(-5,4,1)
C = p.create(27,-40,29)
d = random.sample(range(-100,100), 3)
D = p.create(d[0],d[1],d[2])
E = p.create(1,2,-1)
F = p.create(0,1,5)
G = p.create(-1,2,1)
H = p.create(2,1,3)
#set vectors
AB = p.vector(A,B)
AC = p.vector(A,C)
#check all functions
p.help();
print("---------------------------Write point A------------------------")
p.write(A)
print("---------------------------Write vector AB---------------------")
p.write(AB)
print("---------------------------Define point A------------------------")
print(p.define(A))
print("----------------------------AB is collinear to AC---------------")
print(p.collinearity(AB,AC))
print("---------------------------A,B,C,D are not on the one line----------")
print(p.onLine(A,B,C,D))
print("---------------------------A,B,C,D are not on the one plane----------")
print(p.onPlane(E,F,G,H))
