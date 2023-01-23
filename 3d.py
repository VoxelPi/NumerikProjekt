import numpy as np
from scipy.special import p_roots

def A(z):
    return np.transpose(np.array([z[0,:] - z[2,:],z[1,:] - z[2,:]]))

def quadTriangle(n, z):
    (x_1d, w_1d) = p_roots(n, False)
    print(x_1d)
    print(w_1d)

    x_2d = np.zeros((n*n, 2))
    w_2d = np.zeros((n*n))

    for x_i in range(n):
        for y_i in range(n):
            v = psi(z, phi((x_1d[x_i]+1)*0.5, (x_1d[y_i]+1)*0.5))
            w = w_1d[x_i]*w_1d[y_i]*(1-v[0])*np.linalg.det(A(z))*0.25
            x_2d[x_i + y_i * n] = v
            w_2d[x_i + y_i * n] = w

    return (x_2d, w_2d)

def phi(s, t):
    return np.array([s, (1-s)*t])

def psi(z, v):
    return A(z) @ v + z[2,:] 

z = np.array([[0, 0], [1, 0], [0, 1]])

# print(A(z))
# print(A(z)@np.array([0.5, 0.5]))

print(quadTriangle(2, z))