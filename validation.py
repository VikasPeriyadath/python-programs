def isBalanced(expr):
    if len(expr)%2!=0:
        print "Invalid"
        return False
    opening=set('(')
    match=set([ ('(',')') ])
    stack=[]
    c=0
    for char in expr:
        if char in opening:
            stack.append(char)
        else:
            if len(stack)==0:
                print "Invalid 2"
                return False
            lastOpen=stack.pop()
            if (lastOpen, char)  in match:
              c=c+1
            else :
                print "Invalid 3"
    if c==(len(expr)/2) :
        print "valid"
    else :
        print "Invalid"
    return len(stack)==0


isBalanced("())(")