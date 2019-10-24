## Example of getting a closer estimate ##

val1 = int(input("Enter your inital estimate of the Square Root Value: ")) 

def sqrt(x):
    z = val1
    while abs(z*z-x) >= 0.001:
        z-=(z*z-x)/(2*z)
    return z



z=sqrt(4)
print (z)

