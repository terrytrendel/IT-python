import os
from banner import banner

banner("HTML TAG COUNTER", "TRENDEL")


def load(filename):
    data = []
    print(f"...... loading from {filename}")
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def tags_in(line):
    tag = "<"
    count = 0
    previous_char = None
    for char in line:
        if previous_char == "<" and char != "/":
            count = count +1
        previous_char = char
    return count

def main():
    print("welcome to the HTML counter")
    filename = input("html file:")
    #filename = "testing/index.html"
    lines = load(filename)
    count = 0
    for line in lines:
        count = count + tags_in(line)
    print(count)







main()
