# A function that returns true if the number is Prime, else
# returns false

def pr(num):
    if num > 1:
        for i in range(2,int(num/2)+1):
            if (num % i == 0):
                print(num, "is not a Prime Number")
                break
        else:
            print(num,"is a Prime number")
# Numbers less than 1 can't be Prime
    else:
        print(num,"is not a Prime number")

#Testing pr() function
pr(56)
pr(23)
