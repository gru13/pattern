def pattern(x):
    for a in range(x):
        if a == 0 or a==x-1:
            print(x*"* ")
        else:
            print("*")

if __name__=="__main__":
    while True:
        j = input().split()
        for a in j:
            pattern(int(a))