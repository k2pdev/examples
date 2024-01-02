
output_directory = "./output"
file_name = "file.txt"
output_file_path = output_directory + "/" + file_name

try:
    with open(output_file_path, 'w') as f:
      f.write('text file contents')
      f.close()
except FileNotFoundError:
    print("The output_directory: " + output_directory + " does not exist")

