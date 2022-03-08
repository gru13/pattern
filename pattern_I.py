def pattern(x):
    for a in range(x+1):
        if a==0 or a==x:
            print(x*"* ")
        else:
            print((x)*" "+"*")
if __name__=="__main__":
    while True:
        j=eval(input())
        pattern(j)
