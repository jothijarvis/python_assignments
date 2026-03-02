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