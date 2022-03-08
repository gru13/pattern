def pattern(x):
    for a in range(x):
        print("*"+a*" "+"*"+(x-a-1)*" "+"*")
if __name__=="__main__":
    while True:
        j=eval(input())
        pattern(j)
