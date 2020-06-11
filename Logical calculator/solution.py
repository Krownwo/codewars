def logical_calc(array,op):
    while len(array) > 1:
        inp1 = array.pop(0)
        inp2 = array.pop(0)
        if op == "AND":
            array.insert(0,a(inp1,inp2))
        
        elif op == "OR":
            array.insert(0,o(inp1,inp2))
        
        elif op == "XOR":
            array.insert(0,x(inp1,inp2))

    return array[0]

def a(a,b):
    return a == True and b == True

def o(a,b):
    return a == True or b == True

def x(a,b):
    if a == True and b == False:
        return True
    elif a == False and b == True:
        return True
    else:
        return False