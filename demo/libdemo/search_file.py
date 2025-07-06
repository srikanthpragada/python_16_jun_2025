# Take filename and search string
# Display first line that contains the string
# if string is not found, display error message

filename = input("Enter filename :")
f = open(filename, "rt")
searchstring = input("Enter search string :")
while True:
    line = f.readline()
    if line == "":  # EOF
        print("Sorry! Search failed!")
        break

    if searchstring in line:
        print('Found : ', line)
        break

f.close()
