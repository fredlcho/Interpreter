def errorcase(stack,item1,item2):
    stack.append(item2)
    stack.append(item1)
    stack.append(":error:\n")

def dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,item):
    while countx<county:
        #print(dictionarylist)
        for i in dictionarylist[-1]:
            #countx = countx + 1
            #print(dictionarylist[-1])
            if item in i:
                answer = dictionarylist[-1][countx].get(item)
                inthedictionaryvalue = 1
            countx = countx + 1
            #print(countx,county)
    if inthedictionaryvalue == 0:
        pass
    else:
        return answer
    
def newadd(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue):
    if isinstance(a,int):
        if isinstance(b,int):
            x = a+b
            stacklist[-1].append(x)
        elif b[0].isalpha():
            answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
            if answer is not None and isinstance(answer,int):
                x = a + answer
                stacklist[-1].append(x)
            else:
                print('1')
                errorcase(stacklist[-1],a,b)
        else:
            print('2')
            errorcase(stacklist[-1],a,b)
    elif a[0].isalpha():
        if isinstance(b,int):
            answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
            if answer is not None and isinstance(answer,int):
                x = answer + b
                stacklist[-1].append(x)
            else:
                print('3')
                errorcase(stacklist[-1],a,b)
        elif b[0].isalpha():
            answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
            answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
            print(dictionarylist,"this is list i want")
            #print(a, "t i answer")
            #print(b, "t i answer1")
            if answer is not None and answer1 is not None and isinstance(answer,int) and isinstance(answer1,int):
                x = answer + answer1
                stacklist[-1].append(x)
            else:
                print('4yayay')
                errorcase(stacklist[-1],a,b)
        else:
            print('5')
            errorcase(stacklist[-1],a,b)
    else:
        print('6')
        errorcase(stacklist[-1],a,b)
        
def newsub(stacklist, a, b, dictionarylist,countx,county,inthedictionaryvalue):
    if isinstance(a,int):
        if isinstance(b,int):
            x = b-a
            stacklist[-1].append(x)
        elif b[0].isalpha():
            answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
            if answer is not None and isinstance(answer, int):
                x = answer - a
                stacklist[-1].append(x)
            else:
                errorcase(stacklist[-1],a,b)
        else:
            errorcase(stacklist[-1],a,b)
    elif a[0].isalpha():
        if isinstance(b,int):
            answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
            if answer is not None and isinstance(answer,int):
                x = b - answer
                stacklist[-1].append(x)
            else:
                errorcase(stacklist[-1],a,b)
        elif b[0].isalpha():
            answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
            answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
            if answer is not None and answer1 is not None and isinstance(answer, int) and isinstance(answer1,int):
                x = answer1 - answer
                stacklist[-1].append(x)
            else:
                errorcase(stacklist[-1],a,b)
        else:
            errorcase(stacklist[-1],a,b)
    else:
        errorcase(stacklist[-1],a,b)
def newmul(stacklist, a, b, dictionarylist,countx, county, inthedictionaryvalue):
    if isinstance(a,int):
        if isinstance(b,int):
            x = a*b
            stacklist[-1].append(x)
        elif b[0].isalpha():
            answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
            if answer is not None and isinstance(answer,int):
                x = a * answer
                stacklist[-1].append(x)
            else:
                errorcase(stacklist[-1],a,b)
        else:
            errorcase(stacklist[-1],a,b)
    elif a[0].isalpha():
        if isinstance(b,int):
            answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
            if answer is not None and isinstance(answer, int):
                x = answer * b
                stacklist[-1].append(x)
            else:
                errorcase(stacklist[-1],a,b)
        elif b[0].isalpha():
            answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
            answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
            if answer is not None and answer1 is not None and isinstance(answer,int) and isinstance(answer1,int):
                x = answer * answer1
                stacklist[-1].append(x)
            else:
                errorcase(stacklist[-1],a,b)
        else:
            errorcase(stacklist[-1],a,b)
    else:
        errorcase(stacklist[-1],a,b)
def newdiv(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue):
    if a == 0:
        errorcase(stacklist[-1],a,b)
    else:
        if isinstance(a,int):
            if isinstance(b,int):
                x = b/a
                ab = int(x)
                stacklist[-1].append(ab)
            elif b[0].isalpha():
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                if answer is not None and isinstance(answer, int):
                     x = answer / a
                     ab = int(x)
                     stacklist[-1].append(ab)
                else:
                    errorcase(stacklist[-1],a,b)
            else:
                errorcase(stacklist[-1],a,b)
        elif a[0].isalpha():
            if isinstance(b,int):
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
                if answer is not None and isinstance(answer, int):
                    if answer == 0:
                        errorcase(stacklist[-1],a,b)
                    else:
                        x = b / answer
                        ab = int(x)
                        stacklist[-1].append(ab)
                else:
                    errorcase(stacklist[-1],a,b)
            elif b[0].isalpha():
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
                answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                if answer is not None and answer1 is not None and isinstance(answer, int) and isinstance(answer1, int):
                    if answer == 0:
                        errorcase(stacklist[-1],a,b)
                    else:
                        x = answer1 / answer
                        ab = int(x)
                        stacklist[-1].append(ab)
                else:
                    errorcase(stacklist[-1],a,b)
            else:
                errorcase(stacklist[-1],a,b)
        else:
            errorcase(stacklist[-1],a,b)
def newrem(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue):
    if a == 0:
        errorcase(stacklist[-1],a,b)
    else:
        if isinstance(a,int):
            if isinstance(b,int):
                x = b%a
                ab = int(x)
                stacklist[-1].append(ab)
            elif b[0].isalpha():
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                if answer is not None and isinstance(answer, int):
                     x = answer % a
                     ab = int(x)
                     stacklist[-1].append(ab)
                else:
                    errorcase(stacklist[-1],a,b)
            else:
                errorcase(stacklist[-1],a,b)
        elif a[0].isalpha():
            if isinstance(b,int):
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
                if answer is not None and isinstance(answer, int):
                    if answer == 0:
                        errorcase(stacklist[-1],a,b)
                    else:
                        x = b % answer
                        ab = int(x)
                        stacklist[-1].append(ab)
                else:
                    errorcase(stacklist[-1],a,b)
            elif b[0].isalpha():
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
                answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                if answer is not None and answer1 is not None and isinstance(answer, int) and isinstance(answer1, int):
                    if answer == 0:
                        errorcase(stacklist[-1],a,b)
                    else:
                        x = answer1 % answer
                        ab = int(x)
                        stacklist[-1].append(ab)
                else:
                    errorcase(stacklist[-1],a,b)
            else:
                errorcase(stacklist[-1],a,b)
        else:
            errorcase(stacklist[-1],a,b)
def newneg(stacklist,a,dictionarylist,countx,county,inthedictionaryvalue):
    if isinstance(a, int):
        x = a * -1
        stacklist[-1].append(x)
    elif a[0].isalpha():
        answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
        if answer is not None:
            if isinstance(answer,int):
                x = answer * -1
                stacklist[-1].append(x)
            else:
                stacklist[-1].append(a)
                stacklist[-1].append(":error:\n")
        else:
            stacklist[-1].append(a)
            stacklist[-1].append(":error:\n")
    else:
        stacklist[-1].append(a)
        stacklist[-1].append(":error:\n")
def newand(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue):
    if isinstance(a,int) or isinstance(b,int) or a == ":error:\n" or b == ":error:\n":
        errorcase(stacklist[-1],a,b)
    else:
        if a[0].isalpha():
            if b[0].isalpha():
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
                answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                if answer is not None and answer1 is not None:
                    if answer == ":true:\n" and answer1 == ":true:\n":
                        stacklist[-1].append(":true:\n")
                    else:
                        stacklist[-1].append(":false:\n")
                else:
                    errorcase(stacklist[-1],a,b)
            elif b[0] == ':':
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
                if answer is not None:
                    if answer == ":true:\n" and b == ":true:\n":
                        stacklist[-1].append(":true:\n")
                    else:
                        stacklist[-1].append(":false:\n")
                else:
                    errorcase(stacklist[-1],a,b)
        elif a[0] == ':':
             if b[0].isalpha():
                answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                if answer1 is not None:
                    if a == ":true:\n" and answer1 == ":true:\n":
                        stacklist[-1].append(":true:\n")
                    else:
                        stacklist[-1].append(":false:\n")
                else:
                    errorcase(stacklist[-1],a,b)
             elif b[0] == ':':
                if a == ":true:\n" and b == ":true:\n":
                    stacklist[-1].append(":true:\n")
                else:
                    stacklist[-1].append(":false:\n")
        else:
            errorcase(stacklist[-1],a,b)

def newor(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue):
    if isinstance(a,int) or isinstance(b,int) or a == ":error:\n" or b == ":error:\n":
        errorcase(stacklist[-1],a,b)
    else:
        if a[0].isalpha():
            if b[0].isalpha():
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
                answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                if answer is not None and answer1 is not None:
                    if answer == ":false:\n" and answer1 == ":false:\n":
                        stacklist[-1].append(":false:\n")
                    else:
                        stacklist[-1].append(":true:\n")
                else:
                    errorcase(stacklist[-1],a,b)
            elif b[0] == ':':
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
                if answer is not None:
                    if answer == ":false:\n" and b == ":false:\n":
                        stacklist[-1].append(":false:\n")
                    else:
                        stacklist[-1].append(":true:\n")
                else:
                    errorcase(stacklist[-1],a,b)
        elif a[0] == ':':
             if b[0].isalpha():
                answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                if answer1 is not None:
                    if a == ":false:\n" and answer1 == ":false:\n":
                        stacklist[-1].append(":false:\n")
                    else:
                        stacklist[-1].append(":true:\n")
                else:
                    errorcase(stacklist[-1],a,b)
             elif b[0] == ':':
                if a == ":false:\n" and b == ":false:\n":
                    stacklist[-1].append(":false:\n")
                else:
                    stacklist[-1].append(":true:\n")
        else:
            errorcase(stacklist[-1],a,b)
            
def newnot(stacklist,a,dictionarylist,countx,county,inthedictionaryvalue):
    if isinstance(a,int) or a == ":error:\n":
        stacklist[-1].append(a)
        stacklist[-1].append(":error:\n")
    else:
        if a[0] == ":":
            if a == ":true:\n":
                stacklist[-1].append(":false:\n")
            elif a == ":false:\n":
                stacklist[-1].append(":true:\n")
        elif a[0].isalpha():
            answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
            if answer is not None:
                if answer == ":true:\n":
                    stacklist[-1].append(":false:\n")
                elif answer == ":false:\n":
                    stacklist[-1].append(":true:\n")
                else:
                    stacklist[-1].append(":error:\n")
            else:
                stacklist[-1].append(a)
                stacklist[-1].append(":error:\n")
        else:
            stacklist[-1].append(a)
            stacklist[-1].append(":error:\n")
def newequal(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue):
    if isinstance(a,int) and isinstance(b, int):
        if a == b:
            stacklist[-1].append(":true:\n")
        else:
            stacklist[-1].append(":false:\n")
    else:
        if isinstance(a,int) and not isinstance(b,int):
            if b[0].isalpha():
                answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                if answer1 is not None and isinstance(answer1,int):
                    if a == answer1:
                        stacklist[-1].append(":true:\n")
                    else:
                        stacklist[-1].append(":false:\n")
                else:
                    errorcase(stacklist[-1],a,b)
            else:
                errorcase(stacklist[-1],a,b)
        elif isinstance(b,int) and not isinstance(a,int):
            if a[0].isalpha():
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
                if answer is not None and isinstance(answer,int):
                    if answer == b:
                        stacklist[-1].append(":true:\n")
                    else:
                        stacklist[-1].append(":false:\n")
                else:
                    errorcase(stacklist[-1],a,b)
            else:
                errorcase(stacklist[-1],a,b)
        elif not isinstance(a,int) and not isinstance(b,int):
            if a[0].isalpha() and b[0].isalpha():
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
                answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                if answer is not None and isinstance(answer,int) and answer1 is not None and isinstance(answer1,int):
                    if answer == answer1:
                        stacklist[-1].append(":true:\n")
                    else:
                        stacklist[-1].append(":false:\n")
                else:
                    errorcase(stacklist[-1],a,b)
            else:
                errorcase(stacklist[-1],a,b)
        else:
            errorcase(stacklist[-1],a,b)
        
def newlessThan(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue):
    if isinstance(a,int) and isinstance(b, int):
        if a > b:
            stacklist[-1].append(":true:\n")
        else:
            stacklist[-1].append(":false:\n")
    else:
        if isinstance(a,int) and not isinstance(b,int):
            if b[0].isalpha():
                answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                if answer1 is not None and isinstance(answer1,int):
                    if a > answer1:
                        stacklist[-1].append(":true:\n")
                    else:
                        stacklist[-1].append(":false:\n")
                else:
                    errorcase(stacklist[-1],a,b)
            else:
                errorcase(stacklist[-1],a,b)
        elif isinstance(b,int) and not isinstance(a,int):
            if a[0].isalpha():
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
                if answer is not None and isinstance(answer,int):
                    if answer > b:
                        stacklist[-1].append(":true:\n")
                    else:
                        stacklist[-1].append(":false:\n")
                else:
                    errorcase(stacklist[-1],a,b)
            else:
                errorcase(stacklist[-1],a,b)
        elif not isinstance(a,int) and not isinstance(b,int):
            if a[0].isalpha() and b[0].isalpha():
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
                answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                if answer is not None and isinstance(answer,int) and answer1 is not None and isinstance(answer1,int):
                    if answer > answer1:
                        stacklist[-1].append(":true:\n")
                    else:
                        stacklist[-1].append(":false:\n")
                else:
                    errorcase(stacklist[-1],a,b)
            else:
                errorcase(stacklist[-1],a,b)
        else:
            errorcase(stacklist[-1],a,b)
def newbind(stacklist,a,b,dictionarylist):
    d = str(b) #the name
    c = str(a) #the value
    if d[0].isalpha():
        if c[0].isalpha():
            if c in dictionarylist[-1][-1]:
                f = dictionarylist[-1][-1].get(c)
                dictionarylist[-1][-1][d] = f
                stacklist[-1].append(":unit:\n")
            else:
                errorcase(stacklist[-1],a,b)
        elif c[0] == ':' or c[0] == '"':
            if c == ":error:\n":
                errorcase(stacklist[-1],a,b)
            else:
                dictionarylist[-1][-1][d] = c
                stacklist[-1].append(":unit:\n")
        else:
            e = int(c)
            dictionarylist[-1][-1][d] = e
            stacklist[-1].append(":unit:\n")
    else:
        errorcase(stacklist[-1],a,b)
def intorpreter(inputlist,stacklist,dictionarylist):
    import re
    import copy
    typeoffunclist = [] # 0 is regular function, 1 is inout function
    funlist = []
    fundictionarylist = []
    funparamlist = []
    funnamelist = []
    county = 1
    funcounty = 0
    countx = 0
    inthedictionaryvalue = 0
    for x in inputlist[-1]:
        if funcounty > 0:
            if x == "funEnd\n":
                stacklist[-1].append(x)
                a = stacklist.pop()
                b = fundictionarylist.pop()
                c = funparamlist.pop()
                d = funnamelist.pop()
                e = typeoffunclist.pop()
                dictionarylist[-1][-1][d] = (a,b,c,e)
                stacklist[-1].append(":unit:\n")
                funcounty = funcounty - 1
                print(dictionarylist)
            else:
                stacklist[-1].append(x)
        elif x == ":false:\n":
            stacklist[-1].append(":false:\n")
        elif x == ":error:\n":
            stacklist[-1].append(":error:\n")
        elif x == ":true:\n":
            stacklist[-1].append(":true:\n")
        elif x.split(' ',1)[0] == "push":
                a = x.split(" ",1)
                try:
                    b = int(a[1])
                    stacklist[-1].append(b)
                except ValueError:
                    if a[1][0] == '"':
                        firststring = re.findall(r'"([^"]*)"',a[1])
                        strong = firststring[0]
                        stacklist[-1].append('"' + strong + '"')
                    elif a[1][0].isalpha():
                        stacklist[-1].append(a[1])
                    else:
                        stacklist[-1].append(":error:\n")
        elif x == "add\n":
            if len(stacklist[-1]) <= 1:
                stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop()
                b = stacklist[-1].pop()
                newadd(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue)
        elif x == "pop\n":
            if len(stacklist[-1]) == 0:
                stacklist[-1].append(":error:\n")
            else:
                stacklist[-1].pop()
        elif x == "sub\n":
            if len(stacklist[-1]) <= 1:
                stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop()
                b = stacklist[-1].pop()
                newsub(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue)
        elif x == "mul\n":
            if len(stacklist[-1]) <= 1:
                stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop()
                b = stacklist[-1].pop()
                newmul(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue)
        elif x == "div\n":
            if len(stacklist[-1]) <= 1:
                stacklist[-1].append(":error:\n")
            else:
               a = stacklist[-1].pop()
               b = stacklist[-1].pop()
               newdiv(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue)
        elif x == "rem\n":
            if len(stacklist[-1]) <= 1:
                stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop()
                b = stacklist[-1].pop()
                newrem(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue)
        elif x == "neg\n":
            if len(stacklist[-1]) == 0:
                stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop()
                newneg(stacklist,a,dictionarylist,countx,county,inthedictionaryvalue)
        elif x == "swap\n":
            if len(stacklist[-1]) <= 1:
                stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop()
                b = stacklist[-1].pop()
                stacklist[-1].append(a)
                stacklist[-1].append(b)
        elif x == "bind\n":
            if len(stacklist[-1]) <= 1:
                stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop() #top item
                b = stacklist[-1].pop() #second item
                newbind(stacklist,a,b,dictionarylist)
        elif x == "if\n":
            if len(stacklist[-1]) <= 2:
                stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop()
                b = stacklist[-1].pop()
                c = stacklist[-1].pop()
                d = str(c)
                if c == ":true:\n":
                    stacklist[-1].append(a)
                elif c == ":false:\n":
                    stacklist[-1].append(b)
                elif d[0].isalpha():
                    answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,d)
                    if answer is not None:
                        if answer == ":true:\n":
                            stacklist[-1].append(a)
                        elif answer == ":false:\n":
                            stacklist[-1].append(b)
                        else:
                            stacklist[-1].append(c)
                            stacklist[-1].append(b)
                            stacklist[-1].append(a)
                            stacklist[-1].append(":error:\n")
                    else:
                        stacklist[-1].append(c)
                        stacklist[-1].append(b)
                        stacklist[-1].append(a)
                        stacklist[-1].append(":error:\n")
                else:
                    stacklist[-1].append(c)
                    stacklist[-1].append(b)
                    stacklist[-1].append(a)
                    stacklist[-1].append(":error:\n")
        elif x == "let\n":
            stacklist.append([])
            county = county + 1
            dictionarylist[-1].append({})
        elif x == "end\n":
            a = stacklist.pop()
            b = a.pop()
            stacklist[-1].append(b)
            dictionarylist[-1].pop()
            county = county - 1
        elif x == "and\n":
            if len(stacklist[-1]) <= 1:
                stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop()
                b = stacklist[-1].pop()
                newand(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue)
        elif x == "or\n":
            if len(stacklist[-1]) <= 1:
                stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop()
                b = stacklist[-1].pop()
                newor(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue)
        elif x == "not\n":
            if len(stacklist[-1]) == 0:
                   stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop()
                newnot(stacklist,a,dictionarylist,countx,county,inthedictionaryvalue)
        elif x == "equal\n":
            if len(stacklist[-1]) <= 1:
                stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop()
                b = stacklist[-1].pop()
                newequal(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue)
        elif x == "lessThan\n":
            if len(stacklist[-1]) <= 1:
                stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop()
                b = stacklist[-1].pop()
                newlessThan(stacklist,a,b,dictionarylist,countx,county,inthedictionaryvalue)
        elif x.split(' ',1)[0] == 'fun':
                c = x.split(' ',3)[2] #third item in tuple
                funparamlist.append(c)
                newdict = copy.deepcopy(dictionarylist) #second item in tuple
                fundictionarylist.append(newdict)
                typeoffunclist.append(0)
                a = x.split(' ',3)[1]
                #b = str(a)
               # print(a,"this is a")
                #print(b,"this is b")
                funnamelist.append(a) #NAME OF FUNCTION
                stacklist.append([])
                funcounty = funcounty + 1
        elif x.split(' ',1)[0] == 'inOutFun':
                c = x.split(' ',3)[2] #third item in tuple
                funparamlist.append(c)
                newdict = copy.deepcopy(dictionarylist) #second item in tuple
                fundictionarylist.append(newdict)
                typeoffunclist.append(1)
                a = x.split(' ',3)[1]
                #b = str(a)
               # print(a,"this is a")
                #print(b,"this is b")
                funnamelist.append(a) #NAME OF FUNCTION
                stacklist.append([])
                funcounty = funcounty + 1
        elif x == "call\n":
            if len(stacklist[-1])<2:
                stacklist[-1].append(":error:\n")
            else:
                a = stacklist[-1].pop()
                b = stacklist[-1].pop()
                if b == ':error:\n':
                    errorcase(stacklist[-1],a,b)
                else:
                    if isinstance(a,str):
                        a = a.strip()
                    answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,a)
                    #print(dictionarylist,"dictionarylist")
                    if answer is not None and isinstance(answer,tuple):
                        if answer[3] == 0:
                            if isinstance(b,int) or b[0] == ':':
                                #dictionarylist[0][0]['gogogo'] = 10
                                #print(dictionarylist[0][0],"dictionarylist")
                                answer[1][-1][-1][answer[2]] = b
                                inputlist.append(answer[0])
                                dictanswer = answer[1][0]
                                dictionarylist.append(dictanswer)
                                #print(dictionarylist,"dictionarylist")
                                #print(inputlist[-1],"inputlist,yayy")
                                stacklist.append([])
                                #print(stacklist,"stacklist")
                                intorpreter(inputlist,stacklist,dictionarylist)
                            elif b[0].isalpha():
                                #c = b.strip()
                                #d = repr(c)
                                answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                                #print(d,"d")
                                #print(answer1,"answer1")
                                #print(dictionarylist[-1],"dictionarylist")
                                if answer1 is not None:
                                    answer[1][-1][-1][answer[2]] = answer1
                                    inputlist.append(answer[0])
                                    dictanswer = answer[1][0]
                                    dictionarylist.append(dictanswer)
                                    stacklist.append([])
                                    intorpreter(inputlist,stacklist,dictionarylist)
                                else:
                                    print('1')
                                    errorcase(stacklist[-1],a,b)
                            else:
                                print('2')
                                errorcase(stacklist[-1],a,b)
                        elif answer[3] == 1:
                            if isinstance(b,int) or b[0] == ':':
                                dictionarylist[0][0][answer[2]] = b
                                #print(dictionarylist,"thisisdlist")
                                answer[1][-1][-1][answer[2]] = b
                                inputlist.append(answer[0])
                                dictanswer = answer[1][0]
                                dictionarylist.append(dictanswer)
                               # print(dictionarylist,"dictionarylist")
                                #print(inputlist[-1],"inputlist,yayy")
                                stacklist.append([])
                                #print(stacklist,"stacklist")
                                intorpreter(inputlist,stacklist,dictionarylist)
                            elif b[0].isalpha():
                                answer1 = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                                #print(dictionarylist,"thisisdlist")
                                if answer1 is not None:
                                    dictionarylist[0][0][answer[2]] = answer1
                                    answer[1][-1][-1][answer[2]] = answer1
                                    inputlist.append(answer[0])
                                    dictanswer = answer[1][0]
                                    dictionarylist.append(dictanswer)
                                    print(dictionarylist,"REALDLIST")
                                    stacklist.append([])
                                    intorpreter(inputlist,stacklist,dictionarylist)
                                else:
                                    errorcase(stacklist[-1],a,b)
                            else:
                                errorcase(stacklist[-1],a,b)
                        else:
                            print('3')
                            errorcase(stacklist[-1],a,b)
                    else:
                        print('4')
                        errorcase(stacklist[-1],a,b)
        elif x == "return\n":
            a = stacklist.pop()
            #stacklist.append(a)
            print(a,"aaaa")
            b = a.pop()
            if isinstance(b,int) or b[0] == '"' or b[0] == ':':
                stacklist[-1].append(b)
                #print(stacklist,"um")
            elif b[0].isalpha():
                answer = dictionarychecker(stacklist,countx,county,inthedictionaryvalue,dictionarylist,b)
                if answer is not None:
                    stacklist[-1].append(answer)
                else:
                    stacklist[-1].append(":error:\n")
        elif x == "funEnd\n":
            #stacklist.pop()
            dictionarylist.pop()
            inputlist.pop()
        elif x == "quit":
            break

    return stacklist

def interpreter(input, output):
    inputlist = [[]]
    stacklist = [[]]
    dictionarylist = [[{}]]
    with open(input) as f:
        inputlist[-1] = f.readlines()
   # print (inputlist,"inputlist")
    f1 = open(output, "w")
    laby = intorpreter(inputlist,stacklist,dictionarylist)
    print(laby,"laby")
    laby[-1] = [str(x) for x in laby[-1]]
    laby[-1] = [x.rstrip() for x in laby[-1]]
    laby[-1] = [x + '\n' for x in laby[-1]]
    laby[-1] = [x.replace('"',"") for x in laby[-1]]
    laby[-1][0] = laby[-1][0].rstrip()
    
    
    for x in reversed(laby[-1]):
        f1.write(str(x))
    f.close()
    f1.close()
