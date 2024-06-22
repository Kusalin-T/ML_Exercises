c_pop = {'China':143,
        'India':136,
        'USA':32,
        'Pakistan':21}

def exer2(u_in):
    if u_in=='print':
        print(''.join([f"{c}==>{c_pop[c]}\n" for c in c_pop]))
    elif u_in=='add':
        newname=input('Enter country name: ')
        if newname in c_pop:
            print('Already have this country')
        else:
            newpop=input('Enter the population: ')
            c_pop[newname]=newpop
            exer2('print')
    elif u_in=='remove':
        remname=input('Enter country name: ')
        if remname in c_pop:
            c_pop.pop(remname)
            exer2('print')
        else:
            print('Country no exist')    
    elif u_in=='query':
        qname=input('Enter country name: ')
        print(f'Population is {c_pop[qname]}')
    else:
        print('Unknown Command')    
        
exer2('print')