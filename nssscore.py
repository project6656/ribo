import re
import math
import matplotlib.pyplot as plt
import matplotlib.patches as pts
import numpy as np


plt.title('NSS SCORE')
plt.plot([-1,25],[0,0],'b-')
plt.axis([-1,25,-10,10])
plt.xlabel('chromosome position')
plt.ylabel('Selective Sweep Score')
plt.text(23, -10.5, 'X',color='black',style='normal',size='small')
plt.text(23, -10.2, 'l',color='black',style='normal',size='small')

plt.text(22, 9, 'Positive selection',color='black',style='normal',size='small')
plt.text(22, 8, 'Negative selection',color='black',style='normal',size='small')
plt.plot(21.8,9,'ro')
plt.plot(21.8,8,'go')
from re import finditer



h=open('E:/chromosomalxy/satlist.txt','r')
b=h.readlines()


for o in range(0,len(b)):
        t=b[o]
        h1=open('E:/chromosomalxy/sampleinput.txt','r')
        n=h1.readlines()
        for j in range(0,len(n)):
                y=n[j]
                y=y.strip()
                yy=y.split(':')
                t=t.strip()
                tt=t.split('/')
                sec=tt[2]
                q1=yy[0]
                q2=sec[0:len(sec)-4]
                q1=q1.strip()
                q2=q2.strip()
                if q1==q2:
                        f=open(t,'r')
                        a=f.readlines()
                        for i in range(0,len(a)):
                                x=a[i]
                                #m1=re.findall(r'(chr(.*)):(\d+))',y)
                                m1=re.findall(r'(chr(.*)):(\d+)',y)
                                s1=re.findall(r'(chr(.*))\t(\d+)\t(\d+)\t([+-]?\d.\d+),([+-]?\d.\d+)',x)
                                for k in range(0,len(m1)):
                                        w=m1[k]
                                        for l in range(0,len(s1)):
                                                z=s1[l]
                                                if z[0]==w[0]:
                                                        if int(z[2])<int(w[2]):
                                                                if int(z[3])>int(w[2]):
                                                                        v=float(z[4])
                                                                        if v>0.0:
                                                                                plt.plot(y,v,'go')
                                                                                print (y,'======>','Negative Selection')
                                                                        else:
                                                                                plt.plot(y,v,'ro')
                                                                                print (y,'======>','Positive Selection')
        
                                                
                                                                                        
                                
                                                
plt.savefig('E:/nss.png')
print('End')

