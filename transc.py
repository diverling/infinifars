import re
with open('infinitivesbreakout')  as ibr, open('infinitives') as inf, open('cleaninf', 'w') as clinf:
    letdic = {}
    startdic = ['æ', 'e', 'o']
    for line in ibr:
        lets = list(line)
        letdic[lets[0]] = lets[-2]
    for line in inf:
        reline = re.findall(r"\[\w+]", line)
        #print(reline)
        for word in reline:
            if len(word) > 4 and word[-2] == 'n' and (word[-4] == 't' or word[-4] == 'd'):
                #print(word)
                wordcut = list(word[1:-1])
                firstlet = wordcut[0]
                wordcutr = wordcut[1:]
                #and (word[-3] == 't' or word[-3] == 'd')
                
                
                finalwordl = []
                if firstlet == 'ɒ':
                    finalwordl.append('آ')
                if firstlet in startdic:
                    finalwordl.append('ا')
                

                for let in wordcutr:
                
                    if let in letdic.keys():
                        finalwordl.append(letdic[let])
                wordcut = "".join(finalwordl)
                clinf.write(wordcut + "\n")
"""


        linelist = list(line)
        linelistn = []
        for letter in linelist:
            if letter in keepchar:
                linelistn.append(letter)
        line = "".join(linelistn)
        if len(line) > 3:
            #print(line)

            reline = re.findall(r"\[\w+]", line)
            #print(reline)
            for word in reline:
                if word[-2] == 'n' and len(word) > 4:
                    wordcut = list(word[1:-1])
    
                    if wordcut[0] in startdic:
                        #print(wordcut)
                        wordcut.pop(0)
                        wordcut.insert(0, 'ا')
                    
                    if wordcut[0] == '‫‪ɒ‬‬':
                        #print(wordcut)
                        wordcut.pop(0)
                        wordcut.insert(0, 'آ')
                    
                    finalwordl = []
                    for let in wordcut:
                        finalwordl.append(letdic[let])
                    wordcut = "".join(finalwordl)
                    clinf.write(wordcut + "\n")
            #print(reline)
            #print(line)
            #clinf.write(reline + '\n')
        #line = "".join(linelist)

        #print(line)
    #print(letdic)
    #print(rlts)
"""
