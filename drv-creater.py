


import json


with open('infinitives') as inf:
    urt['v2'] = []
    urt['short'] = []
   

    

   

    for rt in inf:
        
        if rt[-2] == 'د' and rt[-3] == 'و':
            print(rt)
            
            

          
#with open('uniroots2.txt', 'w') as wurt:
    #wurt.write(json.dumps(urt))



"""
urtl = []
upcpro = {}
with open('uniroots2.txt') as urt, open('cleanfreq.txt') as clfrq:
    urt = json.load(urt)
    clfrq = json.load(clfrq)

    
    for root in urt['roots']:
       

        drvl = list(root)
        drvl.insert(2, 'ی')
        drvl.insert(1, 'ا')
        drvl.insert(0, 'ت')
        pat = 'تشاویق'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        pat = 'فعل'
        drv = root
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.insert(3, 'ت')
        pat = 'فعلت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.insert(3, 'ه')
        pat = 'فعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.insert(3, 'ا')
        pat = 'فعلا'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
       
        drvl = list(root)
        drvl.insert(2, 'و')
        pat = 'فعول'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        pat = 'فعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
                    
        drvl = list(root)
        drvl.insert(2, 'ی')
        pat = 'فعیل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        pat = 'فاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(4, 'ه')
        pat = 'فاعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(4, 'ت')
        pat = 'فعالت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ی')
        drvl.insert(4, 'ه')
        pat = 'فعیله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ی')
        drvl.insert(4, 'ت')
        pat = 'فعیلت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(3, 'ی')
        drvl.insert(4, 'ت')
        pat = 'فعلیت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(3, 'ی')
        pat = 'فعایل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        pat = 'افعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        drvl.insert(2, 'ت')
        pat = 'افتعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        drvl.insert(1, 'ن')
        pat = 'انفعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ت')
        drvl.insert(0, 'س')
        drvl.insert(0, 'ا')
        pat = 'استفعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        pat = 'تفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(3, 'ی')
        pat = 'تفعیل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(2, 'ا')
        pat = 'تفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        pat = 'مفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        pat = 'مفعول'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(1, 'ت')
        pat = 'متفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(2, 'ت')
        pat = 'مفتعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(1, 'ن')
        pat = 'منفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(4, 'ه')
        pat = 'مفعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        drvl.insert(5, 'ا')
        pat = 'مفعولا'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        pat = 'مفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        pat = 'مفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        drvl.insert(5, 'ه')
        pat = 'مفاعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        drvl.insert(5, 'ت')
        pat = 'مفاعلت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'ت')
        drvl.insert(0, 'م')
        pat = 'متفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        drvl.insert(5, 'ی')
        drvl.insert(6, 'ت')
        pat = 'مفعولیت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(0, 'س')
        drvl.insert(0, 'م')
        pat = 'مستفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}


    for root in urt['dubs']:
        drvl = list(root)

        pat = 'فعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.pop(2)
        pat = 'حد'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.pop(2)
        pat = 'محداد'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        
        drvl = list(root)
        drvl.pop(2)
        drvl.insert(2, 'ت')
        pat = 'حدت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.insert(3, 'ا')
        pat = 'فعلا'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
       
        drvl = list(root)
        drvl.insert(2, 'و')
        pat = 'فعول'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        pat = 'فعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
                    
        drvl = list(root)
        drvl.insert(2, 'ی')
        pat = 'فعیل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        pat = 'فاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(4, 'ه')
        pat = 'فاعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(4, 'ت')
        pat = 'فعالت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ی')
        drvl.insert(4, 'ه')
        pat = 'فعیله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(3, 'ی')
        drvl.insert(4, 'ت')
        pat = 'فعلیت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(3, 'ی')
        pat = 'فعایل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        pat = 'افعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        drvl.insert(2, 'ت')
        pat = 'افتعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        drvl.insert(1, 'ن')
        pat = 'انفعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ت')
        drvl.insert(0, 'س')
        drvl.insert(0, 'ا')
        pat = 'استفعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        pat = 'تفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(3, 'ا')
        pat = 'تفعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(0, 'م')
        drvl.insert(3, 'ا')
        drvl.pop(5)
        pat = 'متحاد'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(3, 'ی')
        pat = 'تفعیل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(2, 'ا')
        pat = 'تفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        pat = 'مفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        pat = 'مفعول'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(1, 'ت')
        pat = 'متفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(2, 'ت')
        pat = 'مفتعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(1, 'ن')
        pat = 'منفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(4, 'ه')
        pat = 'مفعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        drvl.insert(5, 'ا')
        pat = 'مفعولا'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        pat = 'مفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        drvl.insert(5, 'ه')
        pat = 'مفاعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        drvl.insert(5, 'ت')
        pat = 'مفاعلت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'ت')
        drvl.insert(0, 'م')
        pat = 'متفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        drvl.insert(5, 'ی')
        drvl.insert(6, 'ت')
        pat = 'مفعولیت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(0, 'س')
        drvl.insert(0, 'م')
        drvl.pop(5)
        pat = 'مستفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}



    for root in urt['hollv']:
        
        pat = 'فعل'
        drv = root
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.insert(3, 'ت')
        pat = 'فعلت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.insert(3, 'ه')
        pat = 'فعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.insert(3, 'ا')
        pat = 'فعلا'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
       
        drvl = list(root)
        drvl.insert(2, 'و')
        pat = 'فعول'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        pat = 'فعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
                    
        drvl = list(root)
        drvl.insert(2, 'ی')
        pat = 'فعیل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        pat = 'فاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(4, 'ه')
        pat = 'فاعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(4, 'ت')
        pat = 'فعالت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ی')
        drvl.insert(4, 'ه')
        pat = 'فعیله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ی')
        drvl.insert(4, 'ت')
        pat = 'فعیلت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(3, 'ی')
        drvl.insert(4, 'ت')
        pat = 'فعلیت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(3, 'ی')
        pat = 'فعایل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        pat = 'افعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        drvl.insert(2, 'ت')
        pat = 'افتعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        drvl.insert(1, 'ن')
        pat = 'انفعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ت')
        drvl.insert(0, 'س')
        drvl.insert(0, 'ا')
        pat = 'استفعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        pat = 'تفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(3, 'ی')
        pat = 'تفعیل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(2, 'ا')
        pat = 'تفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        pat = 'مفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        pat = 'مفعول'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(1, 'ت')
        pat = 'متفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(2, 'ت')
        pat = 'مفتعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(1, 'ن')
        pat = 'منفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(4, 'ه')
        pat = 'مفعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        drvl.insert(5, 'ا')
        pat = 'مفعولا'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        pat = 'مفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        pat = 'مفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        drvl.insert(5, 'ه')
        pat = 'مفاعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        drvl.insert(5, 'ت')
        pat = 'مفاعلت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'ت')
        drvl.insert(0, 'م')
        pat = 'متفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        drvl.insert(5, 'ی')
        drvl.insert(6, 'ت')
        pat = 'مفعولیت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(0, 'س')
        drvl.insert(0, 'م')
        pat = 'مستفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.pop(1)
        drvl.insert(1, 'ا')
        drvl.insert(1, 'ت')
        drvl.insert(0, 'م')
        pat = 'مشتاق'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.pop(1)
        drvl.insert(1, 'ی')
        drvl.insert(3, 'ت')
        pat = 'قیمت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        drvl = list(root)
        drvl.pop(1)
        drvl.insert(1, 'ی')
        drvl.insert(1, 'ا')
        pat = 'قایم'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.pop(1)
        drvl.insert(1, 'ی')
        drvl.insert(2, 'ا')
        pat = 'قیام'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.pop(1)
        drvl.insert(1, 'ا')
        drvl.insert(1, 'ی')
        drvl.insert(1, 'ت')
        drvl.insert(0, 'ا')
        pat = 'اشتیاق'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ی')
        drvl.insert(1, 'ا')
        drvl.insert(0, 'ت')
        pat = 'تشاویق'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        

    for root in urt['holly']:
        
        drvl = list(root)
        drvl.insert(2, 'ی')
        drvl.insert(1, 'ا')
        drvl.insert(0, 'ت')
        pat = 'تشاویق'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(3, 'ی')
        pat = 'تفعیل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        pat = 'فید'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        
        drvl = list(root)
        drvl.insert(0, 'م')
        pat = 'مفید'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        pat = 'فیاد'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

    
        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.pop(2)
        drvl.insert(2, 'ا')
        pat = 'مفاد'
        drv = ''.join(drvl)
        if drv in clfrq:

            
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}


    
        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(4, 'ه')
        pat = 'فایده'
        drv = ''.join(drvl)
        if drv in clfrq:
           
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(4, 'ه')
        drvl.insert(0, 'م')
        pat = 'مفایده'
        drv = ''.join(drvl)
        if drv in clfrq:
           
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        
        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(0, 'س')
        drvl.insert(0, 'ا')
        drvl.pop(4)
        drvl.insert(4, 'ا')
        drvl.insert(6, 'ه')
        pat = 'استفاده'
        drv = ''.join(drvl)
        if drv in clfrq:
            
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        pat = 'فایده'
        drv = ''.join(drvl)
        if drv in clfrq:
            
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ا')
        drvl.pop(2)
        drvl.insert(2, 'ا')
        drvl.insert(4, 'ه')
        pat = 'افاده'
        drv = ''.join(drvl)
        if drv in clfrq:
           
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(0, 'س')
        drvl.insert(0, 'م')
        pat = 'مستفید'
        drv = ''.join(drvl)
        if drv in clfrq:
            
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(2, 'ا')
        pat = 'ممایز'
        drv = ''.join(drvl)
        if drv in clfrq:
            
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.pop(1)
        drvl.insert(0, 'م')
        drvl.insert(2, 'ت')
        drvl.insert(3, 'ا')
        pat = 'ممتاز'
        drv = ''.join(drvl)
        if drv in clfrq:
            
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        pat = 'تمیز'
        drv = ''.join(drvl)
        if drv in clfrq:
            
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(2, 'ا')
        pat = 'تمایز'
        drv = ''.join(drvl)
        if drv in clfrq:
            
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ا')
        drvl.insert(2, 'ت')
        drvl.insert(4, 'ا')
        pat = 'امتیاز'
        drv = ''.join(drvl)
        if drv in clfrq:
            
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        

    
    for root in urt['holla']:
       
        
        drvl = list(root)
        pat = 'عاد'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ی')
        drvl.insert(1, 'ا')
        drvl.insert(0, 'ت')
        pat = 'تشاویق'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(2, 'ت')
        pat = 'معتاد'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ا')
        drvl.insert(2, 'ت')
        drvl.insert(3, 'ی')
        pat = 'اعتیاد'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(0, 'س')
        drvl.insert(0, 'ا')
        drvl.pop(4)
        drvl.insert(4, 'ا')
        drvl.insert(6, 'ه')
        pat = 'استفاده'
        drv = ''.join(drvl)
        if drv in clfrq:
            
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        

    for root in urt['lasty']:
        pat = 'قضی'
        drv = root
        
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.pop(3)
        drvl.insert(1, 'ی')
        drv = ''.join(drvl)
        pat = 'مقیض'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.pop(2)
        drvl.insert(2, 'ا')
        drv = ''.join(drvl)

        pat = 'قضا'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.pop(3)
        drvl.insert(3, 'ی')
        drv = ''.join(drvl)
        pat = 'قاضی'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'ا')
        drvl.pop(4)
        drvl.insert(4, 'ه')
        drv = ''.join(drvl)
        pat = 'اقاضه'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
                    
        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(2, 'ا')
 
        drvl.insert(4, 'ا')
        drvl.insert(5, 'ت')
        drvl.pop(6)
        
        drv = ''.join(drvl)
        pat = 'مقاضات'
      
        if drv in clfrq:
            freq = clfrq[drv]
            
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(1, 'ا')
 
        drvl.insert(4, 'ا')
        drvl.pop(5)
        
        drv = ''.join(drvl)
        pat = 'ماقضا'
      
        if drv in clfrq:
            freq = clfrq[drv]
            
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(2, 'ا')
        drvl.insert(4, 'ا')
        drvl.pop(5)
        drv = ''.join(drvl)
        pat = 'تقاضا'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                  upcpro[root][drv]= {'freq': freq, 'proc':  pat}
                  
        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(4, 'ت')
        drv = ''.join(drvl)
        pat = 'قضایت'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                  upcpro[root][drv]= {'freq': freq, 'proc':  pat}
                  
        drvl = list(root)
        drvl.pop(2)
        drvl.insert(2, 'ی')
        drvl.insert(3, 'ه')
        drv = ''.join(drvl)
        pat = 'قضیه'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
             
        drvl = list(root)
        drvl.pop(2)
        drvl.insert(2, 'ی')
        drvl.insert(0, 'ت')
        drvl.insert(4, 'ه')
        drv = ''.join(drvl)
        pat = 'تقضیه'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
              
        drvl = list(root)
        drvl.pop(2)
        drvl.insert(2, 'ی')
        drvl.insert(0, 'ت')
        drv = ''.join(drvl)
        pat = 'تقضی'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.pop(2)
        drvl.insert(2, 'ا')
        drvl.insert(1, 'ت')
        drvl.insert(0, 'ا')
        drv = ''.join(drvl)
        pat = 'اقتضا'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}


    for root in urt['firsta']:
        drvl = list(root)
        pat = 'فعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(3, 'ت')
        pat = 'فعلت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.insert(3, 'ه')
        pat = 'فعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.insert(3, 'ا')
        pat = 'فعلا'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
       
        drvl = list(root)
        drvl.insert(2, 'و')
        pat = 'فعول'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        pat = 'فعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
                    
        drvl = list(root)
        drvl.insert(2, 'ی')
        pat = 'فعیل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        pat = 'فاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(4, 'ه')
        pat = 'فاعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(4, 'ت')
        pat = 'فعالت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ی')
        drvl.insert(4, 'ه')
        pat = 'فعیله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(3, 'ی')
        drvl.insert(4, 'ت')
        pat = 'فعلیت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(3, 'ی')
        pat = 'فعایل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        pat = 'افعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        drvl.insert(2, 'ت')
        pat = 'افتعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        drvl.insert(1, 'ن')
        pat = 'انفعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ت')
        drvl.insert(0, 'س')
        drvl.insert(0, 'ا')
        pat = 'استفعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        pat = 'تفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(3, 'ی')
        pat = 'تفعیل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(2, 'ا')
        pat = 'تفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        pat = 'مفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.pop(0)
        drvl.insert(0, 'و')
        drvl.insert(0, 'م')
        pat = 'موعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            print(drv)
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        pat = 'مفعول'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(1, 'ت')
        pat = 'متفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(2, 'ت')
        pat = 'مفتعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(1, 'ن')
        pat = 'منفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(4, 'ه')
        pat = 'مفعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        drvl.insert(5, 'ا')
        pat = 'مفعولا'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        pat = 'مفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'م')
        pat = 'مفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        drvl.insert(5, 'ه')
        pat = 'مفاعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        drvl.insert(5, 'ت')
        pat = 'مفاعلت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ت')
        drvl.insert(0, 'م')
        pat = 'متفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        drvl.insert(5, 'ی')
        drvl.insert(6, 'ت')
        pat = 'مفعولیت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(0, 'س')
        drvl.insert(0, 'م')
        pat = 'مستفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.pop(0)
        drvl.insert(0, 'ا')
        drvl.insert(1, 'ت')
        drvl.insert(3, 'ا')
        drv = ''.join(drvl)
        pat = 'اتحاد'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.pop(0)
        drvl.insert(0, 'م')
        drvl.insert(1, 'ت')
        drv = ''.join(drvl)
        pat = 'متحد'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        

    for root in urt['firstv']:
        if rt[0] == 'ا' and rt[1] == 'ث' and rt[2] == 'ر':
            print("here")
        drvl = list(root)
        pat = 'فعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(3, 'ت')
        pat = 'فعلت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.insert(3, 'ه')
        pat = 'فعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.insert(3, 'ا')
        pat = 'فعلا'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
       
        drvl = list(root)
        drvl.insert(2, 'و')
        pat = 'فعول'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        pat = 'فعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
                    
        drvl = list(root)
        drvl.insert(2, 'ی')
        pat = 'فعیل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        pat = 'فاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(4, 'ه')
        pat = 'فاعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(4, 'ت')
        pat = 'فعالت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ی')
        drvl.insert(4, 'ه')
        pat = 'فعیله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(3, 'ی')
        drvl.insert(4, 'ت')
        pat = 'فعلیت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(3, 'ی')
        pat = 'فعایل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        pat = 'افعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        drvl.insert(2, 'ت')
        pat = 'افتعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ا')
        drvl.insert(1, 'ن')
        pat = 'انفعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ت')
        drvl.insert(0, 'س')
        drvl.insert(0, 'ا')
        pat = 'استفعال'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        pat = 'تفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(3, 'ی')
        pat = 'تفعیل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(2, 'ا')
        pat = 'تفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        pat = 'مفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        pat = 'مفعول'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(1, 'ت')
        pat = 'متفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(2, 'ت')
        pat = 'مفتعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(1, 'ن')
        pat = 'منفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(4, 'ه')
        pat = 'مفعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        drvl.insert(5, 'ا')
        pat = 'مفعولا'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        pat = 'مفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'م')
        pat = 'مفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        drvl.insert(5, 'ه')
        pat = 'مفاعله'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(1, 'ا')
        drvl.insert(0, 'م')
        drvl.insert(5, 'ت')
        pat = 'مفاعلت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(2, 'ا')
        drvl.insert(0, 'ت')
        drvl.insert(0, 'م')
        pat = 'متفاعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'م')
        drvl.insert(3, 'و')
        drvl.insert(5, 'ی')
        drvl.insert(6, 'ت')
        pat = 'مفعولیت'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.insert(0, 'ت')
        drvl.insert(0, 'س')
        drvl.insert(0, 'م')
        pat = 'مستفعل'
        drv = ''.join(drvl)
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}
        
        drvl = list(root)
        drvl.pop(0)
        drvl.insert(0, 'ا')
        drvl.insert(1, 'ت')
        drvl.insert(3, 'ا')
        drv = ''.join(drvl)
        pat = 'اتحاد'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.pop(0)
        drvl.insert(0, 'م')
        drvl.insert(1, 'ت')
        drv = ''.join(drvl)
        pat = 'متحد'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        drvl = list(root)
        drvl.pop(0)
        drvl.insert(0, 'ی')
        drvl.insert(0, 'م')
        drvl.insert(3, 'ا')
        drv = ''.join(drvl)
        pat = 'میحاد'
        if drv in clfrq:
            freq = clfrq[drv]
            if root not in upcpro:
                upcpro[root] = {drv: {'freq': freq, 'proc':  pat}}
            else:
                if drv not in upcpro[root]:
                    upcpro[root][drv]= {'freq': freq, 'proc':  pat}

        
        
with open('upcprojson.txt', 'w') as upj:
    upj.write(json.dumps(upcpro))
        
        

                    
                    
                    
            


            

                
            
         

            
                
            
            

            


    
        


