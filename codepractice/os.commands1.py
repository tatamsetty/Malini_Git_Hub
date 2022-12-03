'''import os
# String to store the OS command
OScommand = "echo Tinitiate.com"
# Run the OS command using system function
os.system(OScommand)

# Executing OS command SubProcess Module
import subprocess
subprocess.call(['echo','Hello Tinitiate'], shell=True)

# Capture Standard Output
# Execute a SYNTACTICALLY VALID DOS command on windows using subprocess.Popen
# Capture Standard Out and Standard Error in SDOut and SDErr variables

(SDOut,SDErr) = subprocess.Popen( ['echo','Hello World!']
                                 ,stdout=subprocess.PIPE
                                 ,stderr=subprocess.PIPE
                                 ,shell=True).communicate()

# Print the SDOut and SDErr variables
print(SDOut)
print(SDErr)

# Use wait for the OS command to execute, using wait
process = subprocess.Popen( ['cat','1.text']
                             ,stdout=subprocess.PIPE
                             ,stderr=subprocess.PIPE
                             ,shell=True).communicate()

# Print the SDOut and SDErr variables
print(SDOut)
print(SDErr)
'''
import subprocess
 # Use wait for the OS command to execute, using wait
(SDOut,SDErr) = subprocess.Popen( ['python','C:\\Malini\\Precision\\codepractice\\file_read.py']
                             ,stdout=subprocess.PIPE
                             ,stderr=subprocess.PIPE
                             ,shell=True).communicate()
# Print the SDOut and SDErr variables
print(str(SDOut))
print(str(SDErr))

                         



