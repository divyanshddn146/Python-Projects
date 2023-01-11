def prime_checker(number):
    if(n==0 or n==1):
        print("It's not a prime number.")
        return False
    for i in range(2,n):
        if(n%i==0):
            print("It's not a prime number.")
            return False
            break
    print("It's a prime number")
    
n = int(input("Check this number: "))
prime_checker(number=n)