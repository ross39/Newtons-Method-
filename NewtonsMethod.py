#This code uses Newtons method to calculate the square root of a number
#The way this works is that we guess a number for z and then keep getting 
#better and better guesses for what the square root of the number is 
#Each time we iterate over the while loop the guess gets better 
#We can tell the computer when to stop by using the the greater than or equals sign

def sqrt(x):
    z = 1.0

    while abs(z * z - x) >= 0.01:
        z-= (z * z - x) / (2*z)
    
    return z

z = sqrt(9)
print(z)

print(z * z)


