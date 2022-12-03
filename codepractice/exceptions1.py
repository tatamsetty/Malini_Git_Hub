"""print(1)
 
try:
    a=10
    print(a)

except:
   print("some error")     
   #print(b)
finally:
    print("Tinitiate: THIS MESSAGE MUST BE PRINTED")   
   
print(2)
"""

try:
    # a=10
    #print(a)
    a=1/0
except Exception as e:
    print(type(e)._name_, e)
    print(type(e)._name_, e)
else:
    print("Message from Else section")     
finally:
    print("Message from finally")
print(3)          