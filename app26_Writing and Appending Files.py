worker_file = open("workers_data", "a")  # append to the file
print("Info_1: Append to a file \n")
# to append the file
worker_file.write("\nRogee - Genius Designer")
worker_file.close()

# overrite to the file

worker_file = open("workers_data", "w")  # overrite to the file
print("Info_2: write to a file \n")
# to write the file
worker_file.write("\nRogee - Genius Designer")
worker_file.close()


# create a new file

worker_file = open("workers_data2.txt", "w")  # create a new file
print("Info_3: create a new file \n")
# to write the file
worker_file.write("\nAbdou - Pythonist")
worker_file.close()

# create an HTML file
worker_file = open("index.html", "w")  # create an HTML file
print("Info_3: create an HTML file \n")
# to write the file
worker_file.write("<p>This is HTML</p>")
worker_file.close()

