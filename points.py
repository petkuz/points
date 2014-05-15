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

def create(x,y,z):
	"""function to creat the point objects"""
	return([x,y,z,"point"])

def vector(a,b):
	"""function to creat vectors from points"""
	if(check(a,b,"point")==False):
		print("Type error!")
		return False
	return([b[0]-a[0],b[1]-a[1],b[2]-a[2],"vector"])

def define(a):
	"""function to define type of objects"""
	return(a[3])

def write(a):
	"""function to print objects"""
	if(a[3]=="point"):s="()"
	elif(a[3]=="vector"):s="{}"
	coords = s[0]+str(a[0])+","+str(a[1])+","+str(a[2])+s[1];
	print("Object type: "+a[3]+", with coordinates: "+coords)

def check(*a):
	l = len(a)
	if(l<2):
		print("Argument error!")
		return False
	for i in range(0,l-1):
		if(a[i][3]!=a[l-1]):return False
	return True

def collinearity(a,b):
	"""function to check vectors collinearity"""
	if(check(a,b,"vector")):
		k1=a[0]/b[0]
		k2=a[1]/b[1]
		k3=a[2]/b[2]
		if(k1==k2 and k1==k3):return True
		return False
	else:
		print("Type error")
		return False

def onLine(*a):
	"""function to check points lying on a one line"""
	l = len(a)
	if(l==0):
		print("No points error!")
		return False
	if(l==1):
		print("Not enough points error!")
		return False
	for i in range(0,l):
		if(check(a[i],"point")==False):
			print("Type error")
			return  False
	for i in range(1,l-1):
		if(collinearity(vector(a[0],a[i]),vector(a[0],a[l-1]))==False):return False
	return True
	
