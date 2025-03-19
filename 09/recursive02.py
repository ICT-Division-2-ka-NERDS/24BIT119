# A positive integer is entered through the keyboard. Write a function to find its binary equivalent of this number.

def binary(n):
    if n == 0:
        return ""
    y = binary(n//2) + str(n%2)
    print(f"n: {n}, y: {y}, n//2: {n//2}, n%2: {n%2}")
    # return binary(n//2) + str(n%2)
    return y 

print(binary(int(input("Enter a number: "))))