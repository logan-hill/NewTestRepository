#mesh = pymesh.load_mesh("wildrosebuilds_puzzlecube.stl")

#mesh = pymesh.form_mesh(vertices, faces)

#print(mesh.num_vertices, mesh.num_faces, mesh.num_voxels)


#numpy code
#base code with comments can be found on:
#https://pypi.org/project/numpy-stl/
import numpy
import stl
from stl import mesh

puzzle_cube = mesh.Mesh.from_file('wildrosebuilds_puzzlecube.stl')

print("Mesh Normals")
print(puzzle_cube.normals)
print("")

print("Mesh Verices")
print(puzzle_cube.v0, puzzle_cube.v1, puzzle_cube.v2)
print("")

volume = puzzle_cube.get_mass_properties()
print("Volume                                  = {0}".format(volume))
print("")

#assert (puzzle_cube.points[0][0:3] == puzzle_cube.v0[0]).all()
#assert (puzzle_cube.points[0][3:6] == puzzle_cube.v1[0]).all()
#assert (puzzle_cube.points[0][6:9] == puzzle_cube.v2[0]).all()
#assert (puzzle_cube.points[1][0:3] == puzzle_cube.v0[1]).all()

# find the max dimensions, so we can know the bounding box, getting the height,
# width, length (because these are the step size)...
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

# Using an existing stl file:
main_body = mesh.Mesh.from_file('wildrosebuilds_puzzlecube.stl')

minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(main_body)
w1 = maxx - minx
l1 = maxy - miny
h1 = maxz - minz

print("Width:	" + str(w1) + "mm")
print("Length:	" + str(l1) + "mm")
print("Height:	" + str(h1) + "mm")

def update_areas(self):
	areas = .5 * numpy.sqrt((self.normals ** 2).sum(axis=1)) 
	self.areas = areas.reshape((areas.size, 1)) 

print("Surface Area:	" + str(puzzle_cube.areas.sum()))
	
