#use information on the stl to find the shipping label of the object when it is packaged
import numpy
import math
import stl
from stl import mesh

object1 = mesh.Mesh.from_file('wildrosebuilds_puzzlecube.stl')
object2 = mesh.Mesh.from_file('Air_Spinner_2_-_Hollow.stl')
#list of box sizes in inches
boxes = [[6.25,2,9],[9,3,12],[12,6,12],[12,12,12],[14,13,3]]
#list of same boxes as above, but using a for loop, is instantiated with the same sizes, but in metric (millimeters)
metricBoxes = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for x in range(len(boxes)):
	for y in range(len(boxes[x])):
		metricBoxes[x][y] = round((boxes[x][y] * 25.4), 2)
density = 0.00
mass = 0.00

#finds min and max coordinates
def find_mins_maxs(obj):
    minx = maxx = miny = maxy = minz = maxz = None
    for p in obj.points:
        # p contains (x, y, z)
        if minx is None:
            minx = p[stl.Dimension.X]
            maxx = p[stl.Dimension.X]
            miny = p[stl.Dimension.Y]
            maxy = p[stl.Dimension.Y]
            minz = p[stl.Dimension.Z]
            maxz = p[stl.Dimension.Z]
        else:
            maxx = max(p[stl.Dimension.X], maxx)
            minx = min(p[stl.Dimension.X], minx)
            maxy = max(p[stl.Dimension.Y], maxy)
            miny = min(p[stl.Dimension.Y], miny)
            maxz = max(p[stl.Dimension.Z], maxz)
            minz = min(p[stl.Dimension.Z], minz)
    return minx, maxx, miny, maxy, minz, maxz

#updates the areas of the object so that the surface area can be found
def update_areas(self):
	areas = .5 * numpy.sqrt((self.normals ** 2).sum(axis=1)) 
	self.areas = areas.reshape((areas.size, 1))

#changes a millimeter length to inches
def mm_to_inch(metric):
	imperial = metric / 25.4
	return imperial

#changes an inches length to millimeters
def inch_to_mm(imperial):
	metric = imperial * 25.4
	return metric

#checks to see what boxes an object can fit into, using the metric system
def box_fit(width, length, height):
	for x in range(len(metricBoxes)):
		if (width+13<=metricBoxes[x][0] and length+13<=metricBoxes[x][1] and height+13<=metricBoxes[x][2]):
			#print("It fits")
			return x
			break
		elif (width+13<=metricBoxes[x][0] and length+13<=metricBoxes[x][2] and height+13<=metricBoxes[x][1]):
			#print("It fits")
			return x
			break
		elif (width+13<=metricBoxes[x][1] and length+13<=metricBoxes[x][2] and height+13<=metricBoxes[x][0]):
			#print("It fits")
			return x
			break
		elif (width+13<=metricBoxes[x][1] and length+13<=metricBoxes[x][0] and height+13<=metricBoxes[x][2]):
			#print("It fits")
			return x
			break
		elif (width+13<=metricBoxes[x][2] and length+13<=metricBoxes[x][0] and height+13<=metricBoxes[x][1]):
			#print("It fits")
			return x
			break
		elif (width+13<=metricBoxes[x][2] and length+13<=metricBoxes[x][1] and height+13<=metricBoxes[x][0]):
			#print("It fits")
			return x
			break
		else:
			#print("Does not fit")
			pass
	else:
		print("No Compatible Size Found!")

#moves an object, code found from https://numpy-stl.readthedocs.io/en/latest/usage.html#quickstart
def translate(_solid, step, padding, multiplier, axis):
    if 'x' == axis:
        items = 0, 3, 6
    elif 'y' == axis:
        items = 1, 4, 7
    elif 'z' == axis:
        items = 2, 5, 8
    else:
        raise RuntimeError('Unknown axis %r, expected x, y or z' % axis)

    # _solid.points.shape == [:, ((x, y, z), (x, y, z), (x, y, z))]
    _solid.points[:, items] += (step * multiplier) + (padding * multiplier)

#makes a copy of a specified object, code used from https://numpy-stl.readthedocs.io/en/latest/usage.html#quickstart
def copy_obj(obj, dims, num_rows, num_cols, num_layers):
    w, l, h = dims
    copies = []
    for layer in range(num_layers):
        for row in range(num_rows):
            for col in range(num_cols):
                # skip the position where original being copied is
                if row == 0 and col == 0 and layer == 0:
                    continue
                _copy = mesh.Mesh(obj.data.copy())
                # pad the space between objects by 10% of the dimension being
                # translated
                if col != 0:
                    translate(_copy, w, w / 10., col, 'x')
                if row != 0:
                    translate(_copy, l, l / 10., row, 'y')
                if layer != 0:
                    translate(_copy, h, h / 10., layer, 'z')
                copies.append(_copy)
    return copies

#uses min and max coordinates to find the width, length, and height of an object (bounding box)
minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(object1)
w1 = round((maxx - minx), 2)
l1 = round((maxy - miny), 2)
h1 = round((maxz - minz), 2)
minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(object2)
w2 = round((maxx - minx), 2)
l2 = round((maxy - miny), 2)
h2 = round((maxz - minz), 2)
#creates a copy of an object
copy1 = copy_obj(object1, (w1, l1, h1), 2, 2, 1)
translate(object2, w1, w1 / 10., 3, 'x')
copy2 = copy_obj(object2, (w1, l1, h1), 2, 2, 1)
combined = mesh.Mesh(numpy.concatenate([object1.data, object2.data] +
                                    [copy.data for copy in copy1] +
                                    [copy.data for copy in copy2]))

minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(combined)
w3 = round((maxx - minx), 2)
l3 = round((maxy - miny), 2)
h3 = round((maxz - minz), 2)

#finds volume
volume = object1.get_mass_properties()
#converts the result of the previous function into a more readable form
simpleVolume = round(volume[0], 2)

#these new values are here in case you want to use calculations with imperial form instead of metric
#newVolume = round(mm_to_inch(volume[0]), 2)
#newSurface = round(mm_to_inch(object1.areas.sum()), 2)
#newWidth = round(mm_to_inch(w1), 2)
#newLength = round(mm_to_inch(l1), 2)
#newHeight = round(mm_to_inch(h1), 2)

#calls the box_fit function using the bounding box of the selected stl file as parameters, first one is for imperial, second one is for metric
#smallest_box = box_fit(newWidth, newLength, newHeight)
smallest_box = box_fit(w1, l1, h1)

#prints info about the object that was found
print("Volume:	" + str(simpleVolume) + " mm^3")
print("")
print("Surface Area:	" + str(round(object1.areas.sum(), 2)) + " mm^2")
print("")
print("Width:	" + str(w1) + " mm")
print("")
print("Length:	" + str(l1) + " mm")
print("")
print("Height:	" + str(h1) + " mm")

print("The recommended box size to use is box #" + str((smallest_box + 1)) + ", with the dimensions of: " + str(metricBoxes[smallest_box][0]) + " mm by " + str(metricBoxes[smallest_box][1]) + " mm by " + str(metricBoxes[smallest_box][2]) + " mm.")

while True:
	material = input("What material are you using?	")
	if material.upper() == "ABS":
		density = 1.05
		break
	else:
		print("This material is not available!\nMore may be added soon!")

#finds mass using density of chosen matrial and the volume of object, metric
mass = round((density * simpleVolume), 2)

print("The mass is:	" + str(mass) + " mg")

print("")
print("Width:	" + str(w2) + " mm")
print("")
print("Length:	" + str(l2) + " mm")
print("")
print("Height:	" + str(h2) + " mm")
print("")
print("Width:	" + str(w3) + " mm")
print("")
print("Length:	" + str(l3) + " mm")
print("")
print("Height:	" + str(h3) + " mm")







