class Tinitiate:

    # a class Variable
    ti_var   = 100

    # def __init__(self, var1, var2):
    #     # These are Instance variables
    #     self.var1 = var1
    #     self.var2 = var2

    def print_member_attributes(self):
        var99 = 1000
        print(var99)
        # print("Variables from the CONSTRUCTOR var1: ",self.var1 ," var2:",self.var2)

    def add_num_to_class_var(self,in_num):
        # print(self.ti_var)
        print(in_num + self.ti_var)
  
  
tiObject = Tinitiate()
print(tiObject.ti_var)
tiObject.print_member_attributes()
tiObject.add_num_to_class_var(12)

tiObject.ti_var=9
tiObject.add_num_to_class_var(12)

print('===')


o2 = Tinitiate()
print(tiObject.ti_var)
o2.print_member_attributes()
o2.add_num_to_class_var(22)

o2.ti_var=88
o2.add_num_to_class_var(22)

print('===')

tiObject.add_num_to_class_var(12)

# OBJECT of the CLASS Tinitiate
# tiObject = Tinitiate(1,2)

# Call the CLASS's function
# tiObject.print_member_attributes()