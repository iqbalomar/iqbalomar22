num=int(input('Enter the number to check it out:'))
if num>1:
    for i in range(2,num):
        if (num%i) == 0:
            print(num,"It is not a prime number")
            print(i,"Times",num//i,"is",num)
            break
    else:
        print(num,"It is a prime")


else:
    print(num," It is not a prime number")
