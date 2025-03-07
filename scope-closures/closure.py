def fn():
    x = 3
    def fn2():
        return x
    return fn2
    
f = fn()
print(f())


