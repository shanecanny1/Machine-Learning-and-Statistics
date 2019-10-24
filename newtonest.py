## Example of getting a closer estimate ##
## Code Modified by Shane Canny ##
## Source: https://tour.golang.org/flowcontrol
## 25 Oct 2019 ##

val1 = int(input("Enter your inital estimate of the Square Root Value: ")) ##Added the functionality to input an initial sqrt guess ##
val2 = int(input("Enter the Value you want the Square Root of: "))  ## Added the functionality to input an initial value you want to get the sqrt of ## 

def sqrt(x): ## x here is the value that will be taken fron val2 on line 17, this value will be ise in the while loop ##
    z = val1
    while abs(z*z-x) >= 0.001:
        z-=(z*z-x)/(2*z)
    return z



z=sqrt(val2) ## Calling the function ##
print (z) ## Printing the sqrt result##
print (z*z) ## Confirming the calculation is correct by squaring the calculated sqrt ##
