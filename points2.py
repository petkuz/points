import sys
def logout(function):
	def wrapper(a):
		print(function(a))
	return wrapper


class Error(Exception):
	"""class for handling exceptions"""
	def __init__(self, ErrorType):
		errorText = ["createFromCoords(wrong type).", 
					"checkType(wrong type)", 
					"checkType(not enough arguments)",
					"onLine(no arguments)",
					"onPlane(no arguments)",
					"PointCloud(no arguments)",
					"checkType(argument hasn't got attibute 'type')"]
		self.value = "Undefined error!"
		for i in range(0,len(errorText)):
			if(ErrorType==i): 
				self.value = "Error: "+errorText[i]
				break


class Do:
	"""class to work with geometry objects, such as point or vector"""
	

	def createFromCoords(self, x, y, z, t):
		if(isinstance(x,int) and isinstance(y,int) and isinstance(z,int) and 
			(t=='vector' or t=="point")):
			self.x = x
			self.y = y
			self.z = z
			self.type = t
		else: raise Error(0)

	def createPointCloud(self, points):
		if(self.checkType(self,"pointCloud")):
			j = 0
			for i in self:				
				self.points[j] = points[j]
				j+=1

	def checkType(*a):
		l = len(a)
		if(l<3):
			raise Error(2)
			return False
		for i in range(1, l-1):
			if hasattr(a[i],'type'):
				if(a[i].type!=a[l-1]): 
					raise Error(6)
					return False
			else:
				raise Error(1)
				return False
		return True
		
	@logout
	def define(self):
		"""function to define type of objects"""
		return(self.type)

	def write(self):
		"""function to print objects"""
		if(self.type=="point"):
			print("Object type: Point, with coordinates: ("+str(self.x)+","+str(self.y)+","+str(self.z)+")")
		elif(self.type=="vector"):
			print("Object type: Vector, with coordinates: {"+str(self.x)+","+str(self.y)+","+str(self.z)+"}")
		elif(self.type=="pointCloud"):
			points = ""
			for j in range(0,len(self.points)):
				points += " ("+str(self.points[j].x)+","+str(self.points[j].y)+","+str(self.points[j].z)+"),"
			points = points[:-1]
			print("Object type: PointCloud, with points: "+points)


class Point(Do):
	"""class to creating and working with points"""
	def __init__(self, x=0, y=0, z=0):
		try:
			super().createFromCoords(x, y, z, "point")
		except Error as e:
			print(e.value)	
			sys.exit()

	def onLine(*a):
		"""function to check points lying on a one line"""
		try:
			l = len(a)
			if(l==1):
				raise Error(3)
				return False
			for i in range(1,l):
				Do.checkType(a[0], a[i], "point")
			if(l==2):
				return True
			for i in range(2,l-1):
				A = Vector()
				A.fromPoints(a[1], a[i])
				B = Vector()
				B.fromPoints(a[1], a[l-1])
				if(A.collinearity(B)==False):return False
			return True
		except Error as e:
			print(e.value)	
			sys.exit()		

	def onPlane(*a):
		"""function to check points lying on a one plane"""
		try:
			l = len(a)
			if(l==1):
				raise Error(4)
				return False
			for i in range(1,l):
				Do.checkType(a[0], a[i], "point")
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
		except Error as e:
			print(e.value)	
			sys.exit()
		

class Vector(Do):
	"""class to create and work with vectors"""
	def __init__(self, x=0, y=0, z=0):
		try:
			super().createFromCoords(x, y, z, "vector")
		except Error as e:
			print(e.value)
			sys.exit()
		

	def fromPoints(self, a, b):
		"""function to creat vectors from points"""
		try:
			super().checkType(a, b, "point")
			super().createFromCoords(b.x-a.x, b.y-a.y, b.z-a.z, self.type)
		except Error as e:
			print(e.value)
			sys.exit()

	def collinearity(self, b):
		"""function to check vectors collinearity"""
		try:
			super().checkType(b, "vector")
			k1=self.x/b.x
			k2=self.y/b.y
			k3=self.z/b.z
			if(k1==k2 and k1==k3):return True
			return False
		except Error as e:
			print(e.value)
			sys.exit()


class PointCloud(Do):
	"""class to work with point clouds"""
	def __init__(self, *arg):
		try:
			l = len(arg)
			if(l==0):raise Error(5)
			for i in range(0,l):
				super().checkType(arg[i], "point")
			self.points = [0]*l
			self.current = 0
			self.max = l-1
			self.type = "pointCloud"
			super().createPointCloud(arg)
		except Error as e:
			print(e.value)
			sys.exit()

	def __iter__(self):
		return self

	def __next__(self):
		if(self.current > self.max):
			raise StopIteration
		else:
			self.current += 1
			return self.points[self.current-1]


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
		points.createFromCoords(x,y,z)
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
