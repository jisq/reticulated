def f()->Callable[[int], int]:
    @positional
    def g(x:int)->int:
        return x
    return g

def top(x:Any):
    f()(x)

top('a')
