Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tha=int(input("Number of employees:"))
goods= {'Macbook Pro:':229900,'IPods:': 22349,'Digital Camera:':11101,'Alexa:':9999,'Microwave Oven:':9800,'Fitbit Plus:':7980,'Scale:':4999,'Cult Pass:':2799,'Sandwich Toaster:':2195,'MI Band:':999}
l=list(goods.values())
l.sort(reverse=True)
n=tha-1
l1=[]
i=0
y=[]
while(n<len(l)):
    x=l[i]-l[n]
    y.append(x)
    i=i+1
    n=n+1
r=y.index(min(y))
l3=l[r:r+tha]
keys=list(goods.keys())
vals=list(goods.values())
print("The goodies selected for the distriburion are")
for i in l3:
    print(keys[vals.index(i)],i)
print("And the difference between the chosen goodie with highest price and the lowest price is %d"%(max(l3)-min(l3)))