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
            w = w_1d[x_i]*w_1d[y_i]*(1-(x_1d[x_i]+1)*0.5)*abs(np.linalg.det(A(z)))*0.25
            x_2d[x_i + y_i * n] = v
            w_2d[x_i + y_i * n] = w

    return (x_2d, w_2d)

def phi(s, t):
    return np.array([s, (1-s)*t])

def psi(z, v):
    return A(z) @ v + z[2,:] 

z = np.array([[0, 0], [1, 0], [0, 1]])

def runQuad(quad,f):
    xs,ws = quad
    return sum([f(x)*w for (x,w) in zip(xs,ws)])

def test_poly(p,quad):
    expected = sum([a*(1/(l+1))*sum([binom(l+1,i)*(-1)**i*(1/(k+i+1)) for i in range(l+2)]) for (k,p1) in enumerate(p) for (l,a) in enumerate(p1)])
    def f(v):
        return sum([a*v[0]**k*v[1]**l for (k,p1) in enumerate(p) for (l,a) in enumerate(p1)])
    q = runQuad(quad,f)
    return expected - q

p = [[2,4,3],[7,1],[3]]
test_poly(p,quadTriangle(4,z))

def f(v):
    return np.exp(v[0]+v[1])
def g(v):
    return np.sqrt(v[0]+v[1])

expected = 1
for n in range(1,20):
    quad = quadTriangle(n,z)
    q = runQuad(quad, f)
    print("n: ",n,", q: ",q,", diff:", q-expected)

expected = 6/15
for n in range(1,40):
    quad = quadTriangle(n,z)
    q = runQuad(quad, g)
    print("n: ",n,", q: ",q,", diff:", q-expected)
# print(A(z))
# print(A(z)@np.array([0.5, 0.5]))

print(quadTriangle(2, z))