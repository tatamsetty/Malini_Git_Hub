import csv
#from curses import keyname
#from lib2to3.pgen2.token import NEWLINE

#with open('C:/Malini/Precision/codepractice/usa_cities.csv', 'r') as file:
 #   csv_data = csv.reader(file)     
  #  print(csv_data)
    #next(csv_data)
    #for row in csv_data:
      #print(row)
    
 #   with open('C:/Malini/Precision/codepractice/usa_cities_new.csv', 'w', newline='') as new_file:
  #      usa_cities_writer = csv.writer(new_file, delimiter='\t')
   #    for row in csv_data:
   # #     usa_cities_writer.writerow(row)

 #DictWriter Method
with open('C:/Malini/Precision/codepractice/usa_cities.csv', 'r') as file:
     rfieldnames = ['LatD','LatM', 'LatS', 'NS', 'LonD', 'LonM', 'LonS', 'EW', 'City', 'State']
     csv_data = csv.DictReader(file, fieldnames=rfieldnames)
     #for row in csv_data:
     #   print(row)
     
     with open('C:/Malini/Precision/codepractice/usa_cities_new.csv', 'w', newline='') as new_file:
        #wfieldnames = ['LatD','LatM', 'LatS', 'NS', 'LonD', 'LonM', 'LonS', 'EW', 'City', 'State']
        #popfieldnames = ['LonD', 'LonM']
        usa_cities_writer = csv.DictWriter(new_file, fieldnames=rfieldnames, delimiter=',')
        usa_cities_writer.writeheader()

        for row in csv_data:
             if row:
                #print(row)
                row.pop("LonD")
                row.pop("LonM")
                usa_cities_writer.writerow(row)
    
# 
# 