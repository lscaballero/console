from math import*
def f(x):
    return  (-0.95675445*x**4 + 6.7183238*x**3 -16.80697368*x**2 +15.01534076*x -2.90357588)
    
   
def biseccion(f, a, b, tol, n):
    i=1
    while i<=n:
        p=a+(b-a)/2.0
        print ("Iter=", "%03d" % i, " ; p=", "%.14f" % p)
        if abs(f(p))<= 1e-15 or (b-a)/2.0 < tol:
            return p
        i+=1
        if f(a)*f(p) > 0:
            a=p
        else:
            b=p
    print("Iteraciones agotadas: Error")
    return
print("\n"+r"Método de la bisección:"+"\n")
biseccion(f, 1, 1.5, 1e-4, 20)