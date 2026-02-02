# Find area and volume. author: Jothiswarooban
with open('D:/pytraining/box.stl', 'rb') as file:
   binary_data = file.read()

stl_text = binary_data.decode("utf-8")
triangles = []  ; current_triangle = []  ; normals = []
current_normal = None

for line in stl_text.splitlines():
    line = line.strip()
    
    if line.startswith("facet normal"):
        facetnormal = line.split()
        current_normal = [float(facetnormal[-3]), float(facetnormal[-2]), float(facetnormal[-1])]
    
    if line.startswith("outer loop"):
        current_triangle = []

    if line.startswith("vertex"):
        vertex_Vals = line.split()

        if len(vertex_Vals) >= 4:
            current_triangle.append([float(vert) for vert in vertex_Vals[1:]])  

    elif line.startswith("endloop"):
        if len(current_triangle) == 3:
            triangles.append(current_triangle)
            normals.append(current_normal)

total_area = 0 ;  total_volume = 0.0; 
for i in range(len(triangles)):

    (x1,y1,z1),(x2,y2,z2),(x3,y3,z3) = triangles[i]
    
    nx = normals[i][0]
    ny = normals[i][1]
    nz = normals[i][2]

    cx = (x1 + x2 + x3) / 3.0
    cy = (y1 + y2 + y3) / 3.0
    cz = (z1 + z2 + z3) / 3.0

    AB = [x2-x1,y2-y1,z2-z1] 
    BC = [x3-x1,y3-y1,z3-z1] 
    i1,j1,k1 = AB ; i2,j2,k2 = BC ; 
    i = j1*k2 - k1*j2
    j = i1*k2 - i2*k1
    k = i1*j2 - i2*j1

    cross_mag = (i*i + j*j + k*k) ** 0.5
    area = 0.5 * cross_mag
    total_area = area+total_area
    total_volume = total_volume + (cx*nx + cy*ny + cz*nz) * area
if total_volume < 0:
    total_volume = -total_volume

total_volume = total_volume / 3.0
print("Total volume:",total_volume)
print("Total area:",total_area)
    