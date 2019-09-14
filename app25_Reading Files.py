



# open("workers_data.txt", "w")  # write the file

# open("workers_data.txt", "w")  # append to the end of the file

# open("workers_data.txt", "r+")  # read and write the file

worker_file = open("workers_data", "r")  # read the file
print("Info_1: \n")
# check if the file is readable  True or False
print(worker_file.readable())
worker_file.close()


worker_file = open("workers_data", "r")  # read the file
print("Info_2: \n")
# to read a line of the file
print(worker_file.readline())
worker_file.close()


worker_file = open("workers_data", "r")  # read the file
print("Info_3: \n")
# to read the file
print(worker_file.read())
worker_file.close()



# Read all lines and put the into an array
worker_file = open("workers_data", "r")  # read the file
print("Info_4: \n")
print(worker_file.readlines()[2])
worker_file.close()


# Or
worker_file = open("workers_data", "r")  # read the file
print("Info_5: \n")
for workers in worker_file.readlines():
    print(workers)
worker_file.close()