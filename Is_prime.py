def is_prime(n):

    s = 2

    check = 1

    while(s*s <= n):

        if n % s == 0:

            print("its not a prime number")

            check = 0

            break

        s+=1

    if check == 1:

        print("its a prime number")

is_prime(17)
