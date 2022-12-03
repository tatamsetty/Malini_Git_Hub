import funtions1 as f1
import funtions1 as f2

#Instance / Session 1
f1.num1 = 100
f1.num2 = 200

x = f1.add1 ()
print(x)
x = f1.mull()
print(x)

print("------")
#Instance / session 2
f2.num1 = 99
f2.num2 = 199

x = f2.add1()
print(x)
x = f2.mull()
print(x)

print("--------")
print(f1.__sizeof__() + f2.__sizeof__())
