with open('UPC-2016') as upc, open('alpha2') as alp2, open('UPCclean', 'w') as upcc:
    lalp2 = []
    for line in alp2:
        lalp2.append(line[0])
    #print(lalp2)
    for line in upc:
        cline = []
        line = list(line)
        #print(line)
        for let in line:
            if let in lalp2:
                cline.append(let)
    
        cline = "".join(cline)
        #upcc.write(cline + "\n")
                

   
"""
with open('alpha') as alp:
    lcount = 0
    ncleanchara = [] 
    for line in alp:
        line = list(line)
        for chara in line:
            if chara != '‌' and chara != "\n":
                lcount += 1
                print(chara)
                ncleanchara.append(chara)
with open('alpha2', 'w') as alp:
    for chara in ncleanchara:
        alp.write(chara + "\n")
        
"""                
    


    

    
