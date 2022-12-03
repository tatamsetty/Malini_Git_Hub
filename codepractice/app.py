import master_data as md
import core_engine as ce
import random
import os
import sys, logging
import datetime

 #Create a LOGGING Object
######################################################################
l_file_suffix=datetime.datetime.today().strftime("%d%b%Y%H%M%S")

# STEP 1. Create a LOGGING Object
tiFileLog = logging.getLogger('tinitiate-file')

# STEP 2. Create a Log File Handler, the log messages will be created in 
#         this file
logfilename = 'C:\\Malini\\Precision\\codepractice\\Training\\tinPython'+l_file_suffix+'.log'

LogFile = logging.FileHandler(logfilename)

#LogFile = logging.FileHandler('C:\\Malini\\Precision\\codepractice\\Training\\tinPython'+l_file_suffix+'.log', mode='a', encoding=None, delay=False, errors=None)

# STEP 3. Add the handler to the logging object
tiFileLog.addHandler(LogFile)

# STEP 4. Set Log Level
tiFileLog.setLevel(logging.INFO)


#########################################



# Unit Test
# ######################
l_cust_name = "aa"
l_cust_cs = 233
l_cust_req_loan_amt = 23444


result = ce.lms_engine(p_logger=tiFileLog,p_md=md.md_loan, p_cust_name=l_cust_name, p_cust_cs=l_cust_cs, p_cust_loan_amt=l_cust_req_loan_amt)
print(result)

new_file = open("C:\Malini\Precision\codepractice\Output/" + l_cust_name + ".txt", "w")
new_file.write(str(result))
new_file.close()


# Bulk Test
# ######################
for c1 in range(10):
    l_cust_name = "aa " + str(random.randint(1, 100000))
    l_cust_cs = random.randint(100, 499)
    l_cust_req_loan_amt = random.randint(10000, 24999)
    
    result = ce.lms_engine(p_logger=tiFileLog,p_md=md.md_loan, p_cust_name=l_cust_name, p_cust_cs=l_cust_cs, p_cust_loan_amt=l_cust_req_loan_amt)
    print(result)
    
    new_file = open("C:\Malini\Precision\codepractice\Output/" + l_cust_name + ".txt", "w")
    new_file.write(str(result))
    new_file.close()
    
