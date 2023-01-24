import numpy as np
from scipy.special import p_roots

from quad2d import quadTriangle

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