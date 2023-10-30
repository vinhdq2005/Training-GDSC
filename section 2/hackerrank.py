s = input()
t = input()

def compare_string(string):
    length = len(string)
    count = 0
    for i in range(0, length):
        if string[i] != "#":
            string = string[:count] + string[i] + string[count+1:]
            count += 1
        elif string[i] == "#" and count >= 0:
            count -= 1
        if count < 0:
            count = 0

    new_string = ""
    for i in range(0, count):
        new_string += string[i]
    return new_string

if compare_string(s) == compare_string(t):
    print("true")
else:
    print("false")