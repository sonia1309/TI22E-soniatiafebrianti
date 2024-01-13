# open a file
teks = "Halo saya  Sonia Tria Febrianti,saya dari kelas TI22E"

#write to file

#add teks to the file
with open ("test.text", "a") as file1:
        file1.write (teks)

#close the file
file1.close()

with open ("test.text", "r") as file2:
        read_content = file2.read()
        print (read_content)

#close the file
file2.close()
