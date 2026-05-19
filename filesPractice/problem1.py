with open("practice.txt","r") as file:

    data = file.read()

new_data = data.replace("java","python")

print(new_data)


with open("practice.txt","w") as f:
    f.write(new_data)


word = "pythons"
with open("practice.txt","r") as f:
    data = f.read()
    if data.find(word)!= -1 :
        print("find python")
    else:
        print("not finding")


def check_for_line():
    word = "python"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no += 1
        return -1
print(check_for_line())