#dictionaries
import os


#list to store data
file_list = []


#get the list of files
for file_name in os.listdir():
    if os.path.isfile(file_name):

        #get file extension
        file_extension = file_name.split('.')[-1] if '.' in file_name else 'Unknown'

        #get file size
        file_size = os.path.getsize(file_name)

        #dictionary for file data
        file_metadata = {
            'file_name': file_name,
            'file_size_bytes': file_size,
            'file_extension': file_extension
        }


        file_list.append(file_metadata)


for file in file_list:
    print(file)




#teams = {'Carolina': 'Panthers',
#          'Baltimore': 'Ravens',
#            'Atlanta': 'Falccons',
#            'Miami': 'Dolphins',
#            'Denver': 'Broncos', 
#            'New-York': 'Giants', 
#            'Tennessee': 'Titans', 
#            'Arizona': 'Cardinals'
#         }

#print(teams)