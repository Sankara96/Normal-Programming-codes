import itertools
import math

def cross(a, b):
    c = [a[1] * b[2] - a[2] * b[1],
         a[2] * b[0] - a[0] * b[2],
         a[0] * b[1] - a[1] * b[0]]

    return c

if __name__ == '__main__':
    no_triangles = input()
    no_ships = input()
    co_ordinates = raw_input().split()
    [x0,y0,z0] = [float(x) for x in co_ordinates]
    triangles = {}
    triangles_equation = {}
    ships = {}
    distances = []
    for i in xrange(no_triangles):
        temp = raw_input().split()
        temp = [int(x) for x in temp]
        triangles[i] = temp
    for i in xrange(no_ships):
        temp = raw_input().split()
        temp = [float(x) for x in temp]
        ships[i] = temp
    for keys in triangles:
        temp = triangles[keys]
        temp1 = ships[temp[0]]
        temp2 = ships[temp[1]]
        temp3 = ships[temp[2]]
        a =[B-A for A, B in zip(temp1, temp2)]
        b = [B-C for C,B in zip(temp1, temp3)]
        pd = cross(a,b)
        d = sum([A*B for A,B in zip(temp1,pd)])
        point = pd
        #C = (d-(pd[0]**2+pd[1]**2+pd[2]**2))/((pd[0]*x0)+(y0*pd[1])+(pd[2]*z0))
        #de = [x*C for x in pd]
        #point = [A+B for A,B in zip([x0,y0,z0],de)]
        #Distance =  math.sqrt((point[0]-x0)**2+(point[1]-y0)**2+(point[2]-z0)**2)
        Distance = math.sqrt((point[0]*x0)**2+(point[1]*y0)**2+(point[2]*z0)**2+(d)**2)/(math.sqrt(point[0]**2+(point[1])**2+point[2]**2))


        distances.append([keys,Distance])
    distances = sorted(distances, key=lambda x: x[1])
    #print distances
    print '{0}'.format(format(distances[0][1],'.2f'))
    print distances[0][0]



