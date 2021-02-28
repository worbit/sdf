from sdf import *
import numpy as np
from skimage import measure

nx,ny,nz = 20,20,20
x = np.linspace(-1,1,nx)
y = np.linspace(-1,1,ny)
z = np.linspace(-1,1,nz)

xx,yy,zz = np.meshgrid(x, y, z, sparse=False)

m = np.empty((nx*ny*nz,3))
m[:,0] = xx.reshape(-1)
m[:,1] = yy.reshape(-1)
m[:,2] = zz.reshape(-1)

s = sphere(0.9)
v = s(m).reshape(nx,ny,nz)

verts, faces, _, _ = measure.marching_cubes(v, 0)
print(verts.shape, faces.shape)
