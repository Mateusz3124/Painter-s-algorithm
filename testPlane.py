def calc_plane(a, b, c):
    abx = b[0] - a[0]
    aby = b[1] - a[1]
    abz = b[2] - a[2]
    acx = c[0] - a[0]
    acy = c[1] - a[1]
    acz = c[2] - a[2]
    nx = aby * acz - abz * acy
    ny = abz * acx - abx * acz
    nz = abx * acy - aby * acx
    if nx==0 and ny==0 and nz==0:
        return None                
    return (nx, ny, nz, -nx*a[0]-ny*a[1]-nz*a[2])

var = calc_plane([0,0,0], [10,0,0], [0,10,0])
value = [10,10,-1]
sum = 0
for i in range(len(value)):
    sum += value[i] * var[i]
sum += var[3]
print(sum)