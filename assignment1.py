# author: Jothiswarooban
'''In Python, the splitlines() method is used to split a string into a list of lines, breaking at line boundaries such as:

\n (newline)
\r (carriage return)
\r\n (Windows-style newline)'''
'''
text = "Hello\nWorld\r\nPython\rRocks"

# Without line breaks
lines_no_end = text.splitlines()
print(lines_no_end)  
# Output: ['Hello', 'World', 'Python', 'Rocks']

# Keeping line breaks
lines_with_end = text.splitlines(True)
print(lines_with_end)
'''

with open('D:/pytraining/box.stl', 'rb') as file:
   binary_data = file.read()
# binary to text
stl_text = binary_data.decode("utf-8")

triangles = []         
current_triangle = []  

for line in stl_text.splitlines():
    line = line.strip()
    # print('this is line:', line)

    if line.startswith("outer loop"):
        current_triangle = []

    if line.startswith("vertex"):
        vertex_Vals = line.split()

        if len(vertex_Vals) >= 4:
            current_triangle.append([float(vert) for vert in vertex_Vals[1:]])  

    elif line.startswith("endloop"):
        if len(current_triangle) == 3:
            triangles.append(current_triangle)

# RESULT
# print("Number of triangles:", len(triangles))
# print("First triangle:", triangles[0])\
total_area = 0
for n_tria in range(len(triangles)):
    (x1,y1,z1),(x2,y2,z2),(x3,y3,z3) = triangles[n_tria]
    AB = [x2-x1,y2-y1,z2-z1] 
    BC = [x3-x1,y3-y1,z3-z1] 
    i1,j1,k1 = AB ; i2,j2,k2 = BC ; 
    i = j1*k2 - k1*j2
    j = i1*k2 - i2*k1
    k = i1*j2 - i2*j1
    # cross_product = i-j+k
    # area = 0.5*cross_product
    cross_mag = (i*i + j*j + k*k) ** 0.5
    area = 0.5 * cross_mag
    total_area = area+total_area

print(total_area)
    