class A:
    def f(self, k:int)->int:
        return k

class B(A):
    def f(self, k:int)->int:
        return k + 500

def cf(x:A, a:int)->int:
    return x.f(a)

print(cf(A(), 40), cf(B(), 40))
