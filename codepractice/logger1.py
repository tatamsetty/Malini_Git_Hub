import sys, logging
'''################################################################################
# LOGGING MODULE - Log to console
################################################################################


# STEP 1. Create a LOGGING Object
tiConsLog = logging.getLogger('tinitiate-console')

# STEP 2. Create a Streamhandler for the LOGGING Object
ConsHandler = logging.StreamHandler( sys.__stdout__ )

# STEP 3. Set Log Formatting
formatter = logging.Formatter('[%(asctime)s] %(name)-12s: %(levelname)-8s %(message)s')
ConsHandler.setFormatter(formatter)

# STEP 4. Add the Console Handler to the LOGGING Object
tiConsLog.addHandler(ConsHandler)

# STEP 5. Set Log Level
tiConsLog.setLevel(logging.DEBUG)
# print(tiConsLog.getEffectiveLevel())





# Use the functions [debug, info, warn, error] of the logging object
tiConsLog.debug('This is a debug message')
tiConsLog.info('This is a info message')
#tiConsLog.warn('This is a warning message')
tiConsLog.error('This is an error message')
tiConsLog.critical('This is a critical message')

# Change Log level and retry logging all level log messages
tiConsLog.setLevel(logging.INFO)

tiConsLog.debug('This is a debug message')
tiConsLog.info('This is a info message')
#tiConsLog.warn('This is a warning message')
tiConsLog.error('This is an error message')
tiConsLog.critical('This is a critical message')

'''

################################################################################
# LOGGING MODULE - Log to file
################################################################################

import datetime
l_file_suffix=datetime.datetime.today().strftime("%d%b%Y%H%M%S")
print(l_file_suffix)

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
tiFileLog.setLevel(logging.ERROR)


# Run Log messages
tiFileLog.debug('This is a debug message')
tiFileLog.info('This is a info message')


# ONLY THE FOLLOEING MESSAGES ARE LOGGED TO FILE
tiFileLog.error('This is an error message')
tiFileLog.critical('This is a critical message')

# MARKDOWN ```