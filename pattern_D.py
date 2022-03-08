def pattern(x):
        for a in range(int(x)):
            print("*"+(a)*" "+"*")
        for a in range(int(x)):
            print("*"+(int(x))*" "+"*")
        for a in range(int(x)):
            print("*"+(int(x)-a-1)*" "+"*")


if __name__=="__main__":
    while True:
        j=eval(input())
        pattern(j)

