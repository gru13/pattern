def pattern(x):
    for a in range(x):
        if a==x//2:
            print("|"+(x+x)*"-"+'|')
        else:
            print("|"+(x+x)*" "+"|")
if __name__=="__main__":
    while True:
        j = input().split()
        for a in j:
            pattern(int(a))
