import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

file = open(input_file, 'r') 
print(file.read())

file = open(output_file, 'w') 

file.write('Hello AlexDad! Text output was edited!')

file = open(output_file, 'r') 
print(file.read())

# print(input_file, output_file)