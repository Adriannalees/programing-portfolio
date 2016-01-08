# secret decoder

# save a message to a file

#encrypt the message to a separate file

#option to decrypt file


def main():
	message = raw_input("enter a message: ")
	file_name =raw_unput("enter a file name: ")
	plain_message = open("plain_message.txt" , "w")
	plain_message.write(message)
	plain_message.close()




main()