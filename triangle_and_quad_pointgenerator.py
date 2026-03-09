# Triangle and quad point Generator. author: Jothiswarooban k 
def triangle_area(p1,p2,p3):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    x3,y3,z3 = p3

    AB = [x2-x1,y2-y1,z2-z1] 
    BC = [x3-x1,y3-y1,z3-z1] 
    i1,j1,k1 = AB ; i2,j2,k2 = BC ; 
    i = j1*k2 - k1*j2
    j = i1*k2 - i2*k1
    k = i1*j2 - i2*j1

    cross_mag = (i*i + j*j + k*k) ** 0.5
    area = 0.5 * cross_mag
    return area

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


def point_is_inside(p1,p2,p3,p4):
    l_area = triangle_area(p1,p2,p3)
    area1 = triangle_area(p1,p2,p4)
    area2 = triangle_area(p2,p3,p4)
    area3 = triangle_area(p3,p1,p4)

    total_area = area2+area3+area1

    total_area = abs(total_area - l_area)
    if total_area > 1e-07:
        return False
    else:
        return True
def quadgen(p1,p2,p3,p4):
    '''This function generates a new point inside defined tria/quad quad points.
       q1 = quadgen( [1,1,0],[0,-1,0],[0,0,0],[-1,0,0]) '''
    if point_is_inside(p1,p2,p3,p4):
        t1 = triagen(p1,p2,p4)
        t2 = triagen(p2,p3,p4)

    elif point_is_inside(p1,p4,p2,p3):
        t1 = triagen(p1,p2,p3)
        t2 = triagen(p1,p3,p4)



    elif point_is_inside(p1,p3,p4,p2):
        t1 = triagen(p1,p2,p4)
        t2 = triagen(p2,p3,p4)


    else:
        t1 = triagen(p1,p3,p4)
        t2 = triagen(p1,p3,p2)

    while True:
        yield next(t1)
        yield next(t2)

q1 = quadgen( [1,1,0],[0,-1,0],[0,0,0],[-1,0,0])
with open('quadpointgen.csv', 'w') as f:
    for i in range(100000):
        pt = next(q1)

        f.write(str(pt[0])+','+str(pt[1])+','+str(pt[2])+'\n')
