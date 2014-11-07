def count_lines():
	file_to_read = open('count_lines_input.txt', 'r')
	counter=0
	for line in file_to_read:
		counter+=1
	file_to_write = open('count_lines_output.txt', 'w')
	file_to_write.write("Numarul de linii este:")
	file_to_write.write(str(counter))
	file_to_read.close()
	file_to_write.close()

count_lines()