f = open("test1.txt", "w")
f.write("Hello world file")
f.close()

def print_hi(name):

    print(f'Hi, {name}')

f2 = open("test1.txt", "r")
data = f2.read()
f2.close()

if __name__ == '__main__':
    print_hi('PyCharm')


print(data)


def threshold_filter(source_path, output_path, threshold):
    f = open(source_path, "r")
    data = f.read()
    f.close()

    output_data = ""
    for line in data.split("\n"):
        for word in line.split():
            if len(word) > threshold:
                output_data += f"{word}\n"

    f = open(output_path, "w")
    f.write(output_data)
    f.close()


def threshold_filter2(source_path, output_path, threshold):
    with (open(source_path, "r") as source_file,
          open(output_path, "w") as output_file):
        data = source_file.read()

        output_data = ""
        for line in data.split("\n"):
            for word in line.split():
                if len(word) > threshold:
                    output_data += f"{word}\n"

        output_file.write(output_data)




SOURCE_PATH = "data.txt"
FILE_PATH = "filtered.txt"

threshold_filter(SOURCE_PATH, FILE_PATH, 4)


def copy_file(source_path, output_path):
    with (open(source_path, "r") as source_file,
          open(output_path, "w") as output_file):
        output_file.write(source_file.read())

SOURCE_PATH = "data.txt"
FILE_PATH = "copy.txt"

copy_file(SOURCE_PATH, FILE_PATH)

def reverse_file(source_path, output_path):
    with (open(source_path, "r") as source_file,
          open(output_path, "w") as output_file):
        lines = source_file.readlines()
        lines.reverse()
        lines[0] += "\n"
        lines[-1] = lines[-1][:-1]
        output_file.writelines(lines)



SOURCE_PATH = "data2.txt"
FILE_PATH = "copy.txt"

#threshold_filter(SOURCE_PATH, FILE_PATH, 4)
reverse_file(SOURCE_PATH, FILE_PATH)



def first_letter_counter(source_path, character):
    with open(source_path, "r") as source_file:
        data_lines = source_file.readlines()

    counter = 0
    for line in data_lines:
        for word in line.split():
            if word[0] == character:
                counter += 1

    return counter


def censore_file(source_path, output_path, old, new):
    with open(source_path, "r") as source_file:
        data = source_file.read()

    new_data = data.replace(old, new)

    with open(output_path, "w") as file:
        file.write(new_data)


SOURCE_PATH = "data.txt"
FILE_PATH = "copy.txt"

#threshold_filter(SOURCE_PATH, FILE_PATH, 4)
#reverse_file(SOURCE_PATH, FILE_PATH)
count = first_letter_counter(SOURCE_PATH, "a")
print(count)

censore_file(SOURCE_PATH, "cenzura.txt", "a", "!!!!!!!!")


def list_to_file(output_path, data_list):
    my_data = []
    for line in data_list:
        if line[-1] == "\n":
            my_data.append(line)
        else:
            my_data.append(f"{line}\n")

    with open(output_path, "w") as file:
        file.writelines(my_data)


SOURCE_PATH = "data.txt"
FILE_PATH = "copy.txt"

#threshold_filter(SOURCE_PATH, FILE_PATH, 4)
#reverse_file(SOURCE_PATH, FILE_PATH)
#count = first_letter_counter(SOURCE_PATH, "a")
#print(count)
#censore_file(SOURCE_PATH, "cenzura.txt", "a", "!!!!!!!!")


data = ["ahoj","mozno\n","riadok"]
list_to_file("task7.txt", data)
