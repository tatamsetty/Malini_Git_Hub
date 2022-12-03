'''def EmployeeDiscount(bill_amount):
   return bill_amount - 15

def StudentDiscount(bill_amount):
   return bill_amount - 10


def ApplyCoupon(bill_amount, func):
    
    final_amount = func(bill_amount)
    print(final_amount)


ApplyCoupon(100, EmployeeDiscount)
ApplyCoupon(100, StudentDiscount)
'''
'''
def EmpDiscount(func):
   def inner(bill_amount): # inner or use any name
      print("Applying Employee Discount")
      return func(bill_amount - 15)
   return inner

def StuDiscount(func):
   def inner(bill_amount):
      print("Applying Student Discount")
      return func(bill_amount - 10)
   return inner

@EmpDiscount   
def CouponApply1(bill_amount):
    print(bill_amount)

@StuDiscount   
def CouponApply2(bill_amount):
    print(bill_amount)


# Test the Decorators
CouponApply1(100)
CouponApply2(100)

@EmpDiscount
@StuDiscount
def CouponApply3(bill_amount):
    print(bill_amount)


# Test the Decorators
CouponApply3(100)
# MARKDOWN ```
'''

def decorator_coupon(N1):
    def wrap(f):
        def wrapped_f(A):
            return f(A - N1)
        return wrapped_f
    return wrap    


# USE DECORATOR WITH FUNCTION DECLARATION
@decorator_coupon(15)
def GetFinalPrice1(A):
    print(A)

@decorator_coupon(25)
def GetFinalPrice2(A):
    print(A)


# Applying Multiple Decorators on a single function declaration
@decorator_coupon(15)
@decorator_coupon(25)
def MultipleCoupons(A):
    print(A)

# CALL THE FUNCTION WITH DECORATOR
GetFinalPrice1(100)
GetFinalPrice2(100)
MultipleCoupons(100)

    

