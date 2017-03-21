import json


with open('cleaninf') as inf:
    infdic = {}
    infdic['vdan'] = []
    for rt in inf:
        if rt[-3] == 'د' and rt[-4] =="و":
            infdic['vdan'].append(rt)
with open('infrootsjson', 'w') as winf:
    winf.write(json.dumps(infdic))
"""
with open('UPCcleanjson', 'w') as ucj, open('UPCclean') as txt:
    ucjdic = {}
    words = []
    for line in txt:
        words.append(line[:-1])
    ucjdic['words'] = words
    ucj.write(json.dumps(ucjdic))
"""        


with open('UPCcleanjson') as clfrq:
    clfrq = json.load(clfrq)
    clfrq = clfrq['words']
    infprodic = {}
    def vdan():
        rtslice = rt[:-4]
        drvl = list(rtslice)
        drvl.append('ایش') 
        pat = 'گشایش'
        drv = ''.join(drvl)
        if drv in clfrq:
            if rt not in infprodic:
                infprodic[rt] = {drv: {'pattern':  pat}}
            else:
                if drv not in infprodic[rt]:
                    infprodic[rt][drv]= {'proc':  pat}

        rtslice = rt[:-2]
        #print(rtslice)
        drvl = list(rtslice)
        drvl.append('گی') 
        pat = 'گشودگی'
        drv = ''.join(drvl)
        if drv in clfrq:
            print(drv)
            if rt not in infprodic:
                infprodic[rt] = {drv: {'pattern':  pat}}
            else:
                if drv not in infprodic[rt]:
                    infprodic[rt][drv]= {'proc':  pat}
        #print(infprodic)
                    
    for rt in infdic['vdan']:
        vdan()
    #print(infprodic)
        
    with open('infprojson', 'w') as ipj:
        ipj.write(json.dumps(infprodic))

"""
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

"""
            
