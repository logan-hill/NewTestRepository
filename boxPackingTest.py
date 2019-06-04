#Attempts to effeciently pack two preset rectangular objects into a rectangular box
theBox = [5,5,6]
boxWidth = theBox[0]
boxLength = theBox[1]
boxHeight = theBox[2]

object1 = [3,2,2]
w1 = object1[0]
l1 = object1[1]
h1 = object1[2]
object1Volume = object1[0] * object1[1] * object1[2]

object2 = [3,3,3]
w2 = object2[0]
l2 = object2[1]
h2 = object2[2]
object2Volume = object2[0] * object2[1] * object2[2]

largestObject = [0,0,0]
smallestObject = [0,0,0]

def findLargestObject(obj1, obj2):
	global largestObject
	global smallestObject
	if (object1Volume >= object2Volume):
		largestObject = object1
		smallestObject = object2
		return "Object 1"
	else:
		largestObject = object2
		smallestObject = object1
		return "Object 2"
	print(object1Volume)
	print(object2Volume)

#checks to see if the largest object can fit in a box in six different orientations
def canLargestObjectFit(width, length, height, rotation = 0):
	for x in range(1):
		if (width<theBox[0] and length<theBox[1] and height<theBox[2] and rotation == 0):
			print("It fits when at normal orientation")
			break
		if (width<theBox[0] and length<theBox[2] and height<theBox[1] and rotation == 1):
			print("It fits when pitched +90 degrees")
			break
		if (width<theBox[2] and length<theBox[1] and height<theBox[0] and rotation == 2):
			print("It fits when rolled +90 degrees")
			break
		if (width<theBox[1] and length<theBox[0] and height<theBox[2] and rotation == 3):
			print("It fits when yawed +90 degrees")
			break
		if (width<theBox[1] and length<theBox[2] and height<theBox[0] and rotation == 4):
			print("It fits when yawed +90 degrees and pitched 90+ degrees, or pitched +90 degrees and rolled +90 degrees, or rolled +90 degrees and yawed +90 degrees")
			break
		if (width<theBox[2] and length<theBox[0] and height<theBox[1] and rotation == 5):
			print("It fits when rolled +90 degrees and pitched +90 degrees, or yawed +90 degrees and rolled +90 degrees, or pitched +90 degrees and yawed +90 degrees")
			break
	else:
		print("The large box does not fit using rotation " + str(rotation))
		pass

#checks to see if the smallest object can fit in a box with the large object, checks for all possible orientations of both objects
#the smallest object is ALWAYS placed AFTER the largest is placed
def canSmallestObjectFit(width, length, height, rotation = 0):
	for x in range(1):
		#smallest object at normal orientation
		if (width<theBox[0] and length<theBox[1] and height<theBox[2] and rotation == 0):
			c = 0
			if ((smallestObject[2] + largestObject[2]) <= theBox[2]):
				print("It fits when both objects are at normal orientation, stacked on top of the largest object")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			if ((smallestObject[0] + largestObject[0]) <= theBox[0]):
				print("It fits when both objects are at normal orientation, placed beside each other, width-wise")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			if ((smallestObject[1] + largestObject[1]) <= theBox[1]):
				print("It fits when both objects are at normal orientation, placed beside each other, length-wise")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			#both objects have different rotations past here
			if ((smallestObject[2] + largestObject[1]) <= theBox[1]):
				print("It fits when the smallest object is normal, and the largest is pitched 90, stacked")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			if c > 0:
				break
		#smallest object pitched at +90 degrees
		if (width<theBox[0] and length<theBox[2] and height<theBox[1] and rotation == 1):
			c = 0
			if ((smallestObject[1] + largestObject[1]) <= theBox[2]):
				print("It fits when both objects are pitched +90 degrees, stacked on top of the largest object")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			if ((smallestObject[0] + largestObject[0]) <= theBox[0]):
				print("It fits when both objects are pitched +90 degrees, placed beside each other, width-wise")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			if ((smallestObject[2] + largestObject[2]) <= theBox[1]):
				print("It fits when both objects are pitched +90 degrees, placed beside each other, length-wise")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			#both objects have different rotations past here
			if c > 0:
				break
		#smallest object rolled at +90 degrees
		if (width<theBox[2] and length<theBox[1] and height<theBox[0] and rotation == 2):
			c = 0
			if ((smallestObject[0] + largestObject[0]) <= theBox[2]):
				print("It fits when both objects are rolled +90 degrees, stacked on top of the largest object")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			if ((smallestObject[2] + largestObject[2]) <= theBox[0]):
				print("It fits when both objects are rolled +90 degrees, placed beside each other, width-wise")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			if ((smallestObject[1] + largestObject[1]) <= theBox[1]):
				print("It fits when both objects are rolled +90 degrees, placed beside each other, length-wise")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			#both objects have different rotations past here
			if c > 0:
				break
		#smallest object yawed at +90 degrees
		if (width<theBox[1] and length<theBox[0] and height<theBox[2] and rotation == 3):
			c = 0
			if ((smallestObject[2] + largestObject[2]) <= theBox[2]):
				print("It fits when both objects are yawed +90 degrees, stacked on top of the largest object")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			if ((smallestObject[1] + largestObject[1]) <= theBox[0]):
				print("It fits when both objects are yawed +90 degrees, placed beside each other, width-wise")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			if ((smallestObject[0] + largestObject[0]) <= theBox[1]):
				print("It fits when both objects are yawed +90 degrees, placed beside each other, length-wise")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			#both objects have different rotations past here
			if c > 0:
				break
		#first combinations
		if (width<theBox[1] and length<theBox[2] and height<theBox[0] and rotation == 4):
			c = 0
			if ((smallestObject[0] + largestObject[0]) <= theBox[2]):
				print("It fits when both objects are yawed +90 degrees and pitched 90+ degrees, or pitched +90 degrees and rolled +90 degrees, or rolled +90 degrees and yawed +90 degrees, stacked on top of the largest object")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			if ((smallestObject[1] + largestObject[1]) <= theBox[0]):
				print("It fits when both objects are yawed +90 degrees and pitched 90+ degrees, or pitched +90 degrees and rolled +90 degrees, or rolled +90 degrees and yawed +90 degrees, placed beside each other, width-wise")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			if ((smallestObject[2] + largestObject[2]) <= theBox[1]):
				print("It fits when both objects are yawed +90 degrees and pitched 90+ degrees, or pitched +90 degrees and rolled +90 degrees, or rolled +90 degrees and yawed +90 degrees, placed beside each other, length-wise")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			#both objects have different rotations past here
			if c > 0:
				break
		#second combinations
		if (width<theBox[2] and length<theBox[0] and height<theBox[1] and rotation == 5):
			c = 0
			if ((smallestObject[1] + largestObject[1]) <= theBox[2]):
				print("It fits when both objects are rolled +90 degrees and pitched +90 degrees, or yawed +90 degrees and rolled +90 degrees, or pitched +90 degrees and yawed +90 degrees, stacked on top of the largest object")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			if ((smallestObject[2] + largestObject[2]) <= theBox[0]):
				print("It fits when both objects are rolled +90 degrees and pitched +90 degrees, or yawed +90 degrees and rolled +90 degrees, or pitched +90 degrees and yawed +90 degrees, placed beside each other, width-wise")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			if ((smallestObject[0] + largestObject[0]) <= theBox[1]):
				print("It fits when both objects are rolled +90 degrees and pitched +90 degrees, or yawed +90 degrees and rolled +90 degrees, or pitched +90 degrees and yawed +90 degrees, placed beside each other, length-wise")
				c += 1
			else:
				print("*****Does not fit in this orientation*****")
			#both objects have different rotations past here
			if c > 0:
				break
	else:
		print("The small box does not fit using rotation " + str(rotation))
		pass

largestObjectName = findLargestObject(object1, object2)
print("V~~~Basic Information~~~V")
print("The largest object by volume is " + largestObjectName)
print("Largest Object; Width, Length, Height:	" + str(largestObject))
print("Smallest Object; Width, Length, Height:	" + str(smallestObject))
print()

print("V~~~Can Large Object Fit?~~~V")
for x in range(6):
  canLargestObjectFit(largestObject[0],largestObject[1],largestObject[2], x)
print()

print("V~~~Can Small Object Fit With Large Object?~~~V")
for x in range(6):
  canSmallestObjectFit(smallestObject[0],smallestObject[1],smallestObject[2], x)
print()













