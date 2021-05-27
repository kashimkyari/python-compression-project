# importing required modules
import time
from zipfile import ZipFile
import os


startTime = time.time()
nameZip = input("Enter filename after compression: ")
compressFolder = input("Enter the directory to compress:  ")

def get_all_file_paths(directory):

	# initializing empty file paths list
	file_paths = []

	# crawling through directory and subdirectories
	for root, directories, files in os.walk(directory):
		for filename in files:
			# join the two strings in order to form the full filepath.
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)

	# returning all file paths
	return file_paths		

def main():
    
    
	# path to folder which needs to be zipped
	directory = compressFolder

	# calling function to get all file paths in the directory
	file_paths = get_all_file_paths(directory)

	# printing the list of all files to be zipped
	print('Following files will be zipped:')
	for file_name in file_paths:
		print(file_name)
  

	# writing files to a zipfile
	with ZipFile(nameZip+".zip",'w') as zip:
		# writing each file one by one
		for file in file_paths:
			zip.write(file)

	print('All files zipped successfully! as ' + nameZip + ".zip")	



if __name__ == "__main__":
	main()

 #print exection time 
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))

