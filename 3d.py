from scipy.special import binom
from random import uniform

from quad2d import quadTriangle

def runQuad(quad,f):
    xs,ws = quad
    return sum([f(x)*w for (x,w) in zip(xs,ws)])

def test_poly(p,quad):
    expected = sum([a * (1/(l+1))*sum([binom(l+1,i)*(-1)**i*(1/(k+i+1)) for i in range(l+2)]) for (k,p1) in enumerate(p) for (l,a) in enumerate(p1)])
    def f(v):
        return sum([a*v[0]**k*v[1]**l for (k,p1) in enumerate(p) for (l,a) in enumerate(p1)])
    q = runQuad(quad,f)
    return expected - q

# Generates a random polynomial of given total degree
def rand_poly(degree):
    return [[ uniform(-10,10) for l in range(degree - k + 1) ] for k in range(degree + 1) ]

n = 5

m = 2*n-2
z = np.array([[0, 0], [1, 0], [0, 1]])
quad = quadTriangle(n,z)

seed(11825373)

polys = [ rand_poly(m) for _ in range(10)]

print(max([abs(test_poly(p,quad)) for p in polys]))