# Write a program that defines a function sum_avg() to accept marks of five subjects and calculates total and average. It should return directly both values.
def sum_avg(n=5):
    marks = [int(input(f"Enter the marks of subject-{i+1}: ")) for i in range(n)]
    total = sum(marks)
    avg = total/len(marks)
    print(f"Total: {total}, Average: {round(avg,2)}")

n = int(input("Enter the number subject: "))
sum_avg(n)