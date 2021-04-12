file_text = open("file_text.txt","r")
txt_text = file_text.read()
file_text.close()
<<<<<<< HEAD
text_counter = [len(txt_text.split("\n")),
                len(txt_text.split()),
                len(''.join(txt_text.split()))]
=======
text_counter = [len(txt_text.split("\n")),len(txt_text.split()),len(''.join(txt_text.split()))]
>>>>>>> 960dbcf37d1b6c8e565d094c5bd9c5add7be79cf
print(text_counter)
#print(txt_text.split("\n"))
