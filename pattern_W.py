def pattern(xa):
    x = int(xa/2)
    for a in range(x):
        print("*"+x*2*" "+"*")
    for a in range(x):
            print("*"+int(x-a-1)*" "+"*"+" "*a*2+"*"+int(x-a-1)*" "+"*")
if __name__=="__main__":
    while True:
        j = input().split()
        for a in j:
            pattern(a)
