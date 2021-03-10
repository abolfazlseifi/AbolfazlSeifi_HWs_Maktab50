file_text = open("file_text.txt","r")
txt_text = file_text.read()
file_text.close()
text_counter = [len(txt_text.split("\n")),len(txt_text.split()),len(''.join(txt_text.split()))]
print(text_counter)
#print(txt_text.split("\n"))
