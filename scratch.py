def pattern(x):
    '''
    for a in range(x):
        print("*"*(x-a)+(a)*" "+"*")
    for a in range (1,x+1):
        print("*"*a+(x-a)*' '+"*")
pattern(10)'''
    for a in range(x):
        print((x-a)*"*"+(a)*str(a)+"*")
        

pattern(10)
