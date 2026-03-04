# Triangle point Generator. author: Jothiswarooban k 
import random
def triagen(p1, p2, p3):
    while True:
        X_new = random.random()
        alpha = 1-X_new
        y_new = random.random()
        beta = y_new*alpha
        gamma = 1-alpha-beta
        # newpoint = [X_new,y_new]
        newpoint = [alpha,beta,gamma]
    
        triangle_area = ((p2[1] - p3[1]) * (p1[0] - p3[0]) +(p3[0] - p2[0]) * (p1[1] - p3[1]))
        
        a = ((p2[1] - p3[1]) * (newpoint[0] - p3[0]) +(p3[0] - p2[0]) * (newpoint[1] - p3[1])) / triangle_area
        b = ((p3[1] - p1[1]) * (newpoint[0] - p3[0]) +(p1[0] - p3[0]) * (newpoint[1] - p3[1])) / triangle_area
        c = 1 - a - b

        yield a,b,c
 
t1 = triagen([0,0,0], [1,0,0], [1,1,0])
with open('triapointgen.csv', 'w') as f:
    for i in range(1000):
        pt = next(t1)
        print('t1:',pt)
        f.write(str(pt[0])+','+str(pt[1])+','+str(pt[2])+'\n')

def triangle_area(p1,p2,p3):
    triangle_area = ((p2[1] - p3[1]) * (p1[0] - p3[0]) +(p3[0] - p2[0]) * (p1[1] - p3[1]))
    return triangle_area

'''Quad point generator'''
import random
def triagen(p1, p2, p3):
    while True:
        alpha = random.random()
        beta = random.random()*(1-alpha)
        gamma = 1-alpha-beta
        newpoint = [alpha,beta,gamma]

        a = alpha*p1[0]+beta*p2[0]+gamma*p3[0]
        b = alpha*p1[1]+beta*p2[1]+gamma*p3[1]
        c = alpha*p1[2]+beta*p2[2]+gamma*p3[2]
        yield a,b,c

def quadgen(p1,p2,p3,p4):
    
    area1 = triangle_area(p1,p2,p3)
    area2 = triangle_area(p1,p2,p4)
    area3 = triangle_area(p2,p3,p4)
    area4 = triangle_area(p3,p1,p4)
    
    print(area1)
    print(area2,area3,area4)

    total_area = area2+area3+area4
    if area1 == total_area:
        t1 = triagen(p1,p2,p4)
        t2 = triagen(p2,p3,p4)

    while True:
        yield next(t1)
        yield next(t2)

q1 = quadgen( [1,0,0], [1,1,0],[0,1,0],[0,0,0])
with open('quadpointgen.csv', 'w') as f:
    for i in range(100000):
        pt = next(q1)
        f.write(str(pt[0])+','+str(pt[1])+','+str(pt[2])+'\n')