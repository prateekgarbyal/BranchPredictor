import math
import sys
#filename='training_set.csv'

#data=np.loadtxt(filename, delimiter=',', skiprows=1)

myinput=[]
actual=[]
localpre=[]
globalpre=[]
selector=[]
selectorpre=[]
localindex=[]
final=[]
output=[]


f = open("sample_branch_sequence.txt")
myinput = f.read().split('\n')

for x in range (0,len(myinput)-1):
  actual.append(myinput[x][1])

localp=['00']*10

selector=['00']*10

globalp=['00']*64

globaladd='000000'

for x in range(0,len(myinput)-1):
    localindex=int(myinput[x][0])
    
    if localp[localindex]=='00' or localp[localindex]=='01': 
        localpre.append('n')
    else:
        localpre.append('t')
    #print(localpre[x])
    if actual[x]=='t':
        if localp[localindex]=='00':
            localp[localindex]='01'
            
        elif localp[localindex]=='01':
            localp[localindex]='10'
            
        elif localp[localindex]=='10':
            localp[localindex]='11'
            
        else:
            localp[localindex]='11'
    
    if actual[x]=='n':
        if localp[localindex]=='00':
            localp[localindex]='00'
            
        elif localp[localindex]=='01':
            localp[localindex]='00'
            
        elif localp[localindex]=='10':
            localp[localindex]='01'
            
        else:
            localp[localindex]='10'
 
for x in range(0,len(myinput)-1):
    globalindex=int(globaladd, 2)
    
    if globalp[globalindex]=='00' or globalp[globalindex]=='01': 
        globalpre.append('n')
    else:
        globalpre.append('t')
    #print(localpre[x])
    if actual[x]=='t':
        if globalp[globalindex]=='00':
            globalp[globalindex]='01'
            
        elif globalp[globalindex]=='01':
            globalp[globalindex]='10'
            
        elif globalp[globalindex]=='10':
            globalp[globalindex]='11'
            
        else:
            globalp[globalindex]='11'
    
    if actual[x]=='n':
        if globalp[globalindex]=='00':
            globalp[globalindex]='00'
            
        elif globalp[globalindex]=='01':
            globalp[globalindex]='00'
            
        elif globalp[globalindex]=='10':
            globalp[globalindex]='01'
            
        else:
            globalp[globalindex]='10'
        
    globaladd=str(globaladd[1:])
    if actual[x]=='t' :
        globaladd=globaladd +'1'
    else:
        globaladd=globaladd +'0'

for x in range(0,len(myinput)-1):
    localindex=int(myinput[x][0])
    
    if selector[localindex]=='00' or selector[localindex]=='01': 
        selectorpre.append('l')
    else:
        selectorpre.append('g')
        
    #print(localpre[x])
    if (localpre[x]!=globalpre[x]):
        if (localpre[x]==actual[x]):
            if selector[localindex]=='00':
                selector[localindex]='00'

            elif selector[localindex]=='01':
                selector[localindex]='00'

            elif selector[localindex]=='10':
                selector[localindex]='01'

            else:
                selector[localindex]='10'

        else:
            if selector[localindex]=='00':
                selector[localindex]='01'

            elif selector[localindex]=='01':
                selector[localindex]='10'

            elif selector[localindex]=='10':
                selector[localindex]='11'

            else:
                selector[localindex]='11'

for x in range(0,len(myinput)-1):
  if selectorpre[x]=='l':
    final.append(localpre[x])
  else:
    final.append(globalpre[x])

for x in range(0,len(myinput)-1):
  output.append(myinput[x][0]+localpre[x]+globalpre[x]+selectorpre[x]+final[x]+actual[x])

outputfile = open('myoutput.txt', 'w')
outputfile.write("\n".join(output))