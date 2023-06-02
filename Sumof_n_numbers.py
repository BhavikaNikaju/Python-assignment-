ques-Python Program for Sum of squares of first n natural numbers

N = int(input("Enter value of N: "))

sumVal = 0

for i in range(1, N+1):

    sumVal += (i*i)

print("Sum of squares = ", sumVal)

output

RUN 1:

Enter value of N: 10

Sum of squares =  385

RUN 2:

Enter value of N: 12

Sum of squares =  650
