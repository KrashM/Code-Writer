import os

lines = []

with open("TestFile.txt", "r") as file:
    for line in file:
        lines.append(line)
    
while True:
    print("What do you want to add?")
    print('Class?(c) | Method?(m) | Variable?(v)')
    inside = input()
    to_be_inserted = ''
    if inside == 'c':
        print('Public or private?(+|-)')
        inside = input()
        pub_pri = ''
        if inside == '+':
            pub_pri = 'public'
        if inside == '-':
            pub_pri = 'private'
        print('Name?')
        name = input()
        to_be_inserted = pub_pri + ' class ' + name + ' {\n\n\n}\n'
        for i in range(len(lines) + 1):
            if i < len(lines):
                if 'using' in lines[i]:
                    continue
                else:
                    lines.insert(i, to_be_inserted)
                    break
            else:
                lines.append(to_be_inserted)
    if inside == 'm':
        print('Public or private?(+|-)')
        inside = input()
        pub_pri = ''
        if inside == '+':
            pub_pri = 'public'
        if inside == '-':
            pub_pri = 'private'
        print('Type?')
        inside = input()
        type = ''
        if inside == 'void':
            type = 'void'
        if inside == 'int':
            type = 'int'
        if inside == 'char':
            type = 'char'
        if inside == 'string':
            type = 'string'
        if inside == 'double':
            type = 'double'
        print('Name?')
        name = input()
        to_be_inserted = pub_pri + ' ' + type + ' ' + name + '() {\n\n\n}\n'
        for i in range(len(lines) + 1):
            if i < len(lines):
                if 'using' in lines[i]:
                    continue
                else:
                    lines.insert(i, to_be_inserted)
                    break
            else:
                lines.append(to_be_inserted)
    if inside == 'v':
        print('Public or private?(+|-)')
        inside = input()
        pub_pri = ''
        if inside == '+':
            pub_pri = 'public'
        if inside == '-':
            pub_pri = 'private'
        print('Type?')
        inside = input()
        type = ''
        if inside == 'int':
            type = 'int'
        if inside == 'char':
            type = 'char'
        if inside == 'string':
            type = 'string'
        if inside == 'double':
            type = 'double'
        print('Name?')
        name = input()
        to_be_inserted = pub_pri + ' ' + type + ' ' + name + ';\n'
        for i in range(len(lines) + 1):
            if i < len(lines):
                if 'using' in lines[i]:
                    continue
                else:
                    lines.insert(i, to_be_inserted)
                    break
            else:
                lines.append(to_be_inserted)
    print("Do you want to add something else?(y|n)")
    inside = input()
    if inside == 'n':
        break

with open("TestFile.txt", "w") as file:
    for line in lines:
        file.write(line)