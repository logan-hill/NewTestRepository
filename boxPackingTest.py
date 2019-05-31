#Attempts to effeciently pack two preset rectangular objects into a rectangular box
theBox = [5,5,6]
boxWidth = theBox[0]
boxLength = theBox[1]
boxHeight = theBox[2]

object1 = [2,1,2]
w1 = object1[0]
l1 = object1[1]
h1 = object1[2]
object1Volume = object1[0] * object1[1] * object1[2]

object2 = [3,1,1]
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

def canLargestObjectFit(width, length, height):
    canFit = False
	for x in range(1) and canFit == False:
		if (width<metricBoxes[0] and length<metricBoxes[1] and height<metricBoxes[2]):
			print("It fits when at normal orientation")
			canFit = True
		if (width<metricBoxes[0] and length<metricBoxes[2] and height<metricBoxes[1]):
			print("It fits when pitched +90 degrees")
			canFit = True
		if (width<metricBoxes[2] and length<metricBoxes[1] and height<metricBoxes[0]):
			print("It fits when rolled +90 degrees")
			canFit = True
		if (width<metricBoxes[1] and length<metricBoxes[0] and height<metricBoxes[2]):
			print("It fits when yawed +90 degrees")
			canFit = True
		if (width<metricBoxes[1] and length<metricBoxes[2] and height<metricBoxes[0]):
			print("It fits when yawed +90 degrees and pitched 90+ degrees, or pitched +90 degrees and rolled +90 degrees, or rolled +90 degrees and yawed +90 degrees")
			canFit = True
		if (width<metricBoxes[2] and length<metricBoxes[0] and height<metricBoxes[1]):
			print("It fits, when rolled +90 degrees and pitched +90 degrees, or yawed +90 degrees and rolled +90 degrees, or pitched +90 degrees and yawed +90 degrees")
			canFit = True
	else:
		print("Does not fit")
		pass

largestObjectName = findLargestObject(object1, object2)
print("The largest object is " + largestObjectName)
print(largestObject)
print(smallestObject)

canLargestObjectFit(largestObject[0],largestObject[1],largestObject[2])














