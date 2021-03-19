t=True
while(t):
    A=int(input('Enter first side of the triangle:'))
    B=int(input('Enter second side of the triangle:'))
    C=int(input('Enter third side of the triangle:'))
    if(A+B>C and B+C>A and A+C>B):
        print("It is a triangle")
        if(A==B==C):
            print('It is an equailateral triangle')
            break
        elif(A==B!=C or A==C!=B or B==C!=A):
            print('It is isosceles triangle')
            break
        elif(A!=B!=C):
            print('It is scalene triangle')
            break
    else:
        print("It is not a triangle")
        print('input correct inputs')
        #t=True

