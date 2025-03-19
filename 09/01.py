# Write a program that defines a function count_lower_upper() that accepts a string and calculates the number of uppercase and lowercase alphabets in it. It should return these values as a dictionary. Call this function for some sample string.
def q1():
    def count_lower_upper(string:str):
        upperCase=0
        lowerCase=0
        for i in string:
            if (i.isupper()):
                upperCase+=1
            elif(i.islower()):
                lowerCase+=1
            else:
                pass
        return {"UpperCase":upperCase,"LowerCase":lowerCase}
    s1=input("Enter the name: ")
    print(count_lower_upper(s1))
q1()