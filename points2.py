class Do:
	"""class to work with geometry objects, such as point or vector"""
	def create(self, x, y, z, t):
		self.x = x
		self.y = y
		self.z = z
		self.t = t

	def setit(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def check(*a):
		l = len(a)
		if(l<3):
			print("Argument error!")
			return False
		for i in range(1, l-1):
			if(a[i].t!=a[l-1]):return False
		return True

	def define(self):
		"""function to define type of objects"""
		return(self.t)

	def write(self):
		"""function to print objects"""
		if(self.t=="point"):s="()"
		elif(self.t=="vector"):s="{}"
		coords = s[0]+str(self.x)+","+str(self.y)+","+str(self.z)+s[1];
		print("Object type: "+self.t+", with coordinates: "+coords)


class Point(Do):
	"""class to creating and working with points"""
	def __init__(self, x=0, y=0, z=0):
		super().create(x, y, z, "point")

	def onLine(*a):
		"""function to check points lying on a one line"""
		l = len(a)
		if(l==0):
			print("No points error!")
			return False
		for i in range(1,l-1):
			A = Vector()
			A.fromPoints(a[0], a[i])
			B = Vector()
			B.fromPoints(a[0], a[l-1])
			if(A.collinearity(B)):return True
		return False

	def onPlane(*a):
		"""function to check points lying on a one plane"""
		l = len(a)
		if(l<=3):
			return True
		x1 = a[0].x 
		y1 = a[0].y
		z1 = a[0].z
		p = a[1].x - x1
		b = a[1].y - y1
		c = a[1].z- z1
		d = a[2].x  - x1	
		e = a[2].y - y1
		f = a[2].z - z1
		for i in range(3,l):
			x = a[i].x
			y = a[i].y
			z = a[i].z
			if((x-x1)*(b*f-c*e)-(y-y1)*(p*f-c*d)+(z-z1)*(p*e-b*d)!=0):
				return False
		return True
		

class Vector(Do):
	"""class to creating and working with vectors"""
	def __init__(self, x=0, y=0, z=0):
		super().create(x, y, z, "vector")

	def fromPoints(self, a, b):
		"""function to creat vectors from points"""
		if(super().check(a, b, "point")==False):
			print("Type error!")
			return False
		super().setit(b.x-a.x, b.y-a.y, b.z-a.z)

	def collinearity(self, b):
		"""function to check vectors collinearity"""
		k1=self.x/b.x
		k2=self.y/b.y
		k3=self.z/b.z
		if(k1==k2 and k1==k3):return True
		return False


def help():
	"""function to help"""
	print(
	"""
	-------------------------HELP GUIDE-----------------------
	About: This is the module to work with points and vectors.
	How to connect: To connect this module to your program you 
		simply have to put module 'points.py' in  the same 
		directory as your program and write next code in the 
		begining of your code: import points
	Methods:
		points.create(x,y,z)
			Method to create the point with coordinates x,y,z.
		points.vector(a,b)
			Method to create the vector from two points a,b.
		points.define(a)
			Method returns type ('point' or 'vector') of 
			the object 'a'.
		points.write(a)
			Function to print object 'a'.
		points.collinearity(a,b)
			Method checks vectors 'a' and 'b' to collinearity.
		points.onLine(a,b,.....,n)
			Function to check multyple points lying on the 
			one line.
	""")
