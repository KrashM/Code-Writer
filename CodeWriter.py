import os

lines = []

#Get the file contents
with open("TestFile.txt", "r") as file:
    for line in file:
        lines.append(line)

names_of_classes = []

#Get the names of the classes
for line in lines:
    if 'class' in line:
        name = line.split(' ')
        index = name.index('class')
        names_of_classes.append(name[index + 1].replace('\n', ''))

while True:
    print("What do you want to add?")
    print('Class?(c) | Method?(m) | Variable?(v)')
    inside = input()

    to_be_inserted = ''

    #Insert class
    if inside == 'c':
        #Public or private
        print('Public or private?(+|-)')
        inside = input()
        pub_pri = ''
        if inside == '+':
            pub_pri = 'public'
        if inside == '-':
            pub_pri = 'private'
        
        #Name
        print('Name?')
        name = input()

        #Adding the new class to the list
        names_of_classes.append(name)

        #Inserting into the file contents
        to_be_inserted = pub_pri + ' class ' + name + ' {\n\n\n}\n'
        for i in range(len(lines) + 1):
            if i < len(lines):
                #Checking for the libraries
                if 'using' in lines[i]:
                    continue
                else:
                    lines.insert(i, to_be_inserted)
                    break
            else:
                lines.append(to_be_inserted)
    
    #Insert method
    if inside == 'm':
        #Ask in which method to add it
        print('In which class do you want to add it in?(Type the name)')
        for class_name in names_of_classes:
            print(class_name)
        inside = input()

        #Find on which line is the class
        index_of_class = 0
        for line in lines:
            if inside in line:
                index_of_class = lines.index(line) + 1

        #Public or private
        print('Public or private?(+|-)')
        inside = input()
        pub_pri = ''
        if inside == '+':
            pub_pri = 'public'
        if inside == '-':
            pub_pri = 'private'

        #Type
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

        #Name
        print('Name?')
        name = input()

        #Inserting it into the file contents
        to_be_inserted = pub_pri + ' ' + type + ' ' + name + '() {\n\n\n}\n'
        lines.insert(index_of_class, to_be_inserted)

    #Insert variable
    if inside == 'v':
        #Ask in which method to add it
        print('In which class do you want to add it in?(Type the name)')
        for class_name in names_of_classes:
            print(class_name)
        inside = input()

        index_of_class = 0
        index_of_next_class = len(lines)

        #Find on which line is the class 
        for line in lines:
            if inside in line:
                index_of_class = lines.index(line) + 1
                break
        
        #Find on which line is the next class
        for i in range(index_of_class, len(lines)):
            if 'class' in lines[i]:
                index_of_next_class = lines.index(lines[i]) - 1


        names_of_methods = []
        index_of_method = 0

        #Make a list of all the methods in that class
        for i in range(index_of_class, len(lines)):
            if i >= index_of_next_class:
                break
            if '{' in lines[i]:
                name = lines[i].split(' ')
                index = name.index('{\n')
                names_of_methods.append(name[index - 1].replace('()', ''))

        #Ask if the user wants the variable to be global(for the whole class) or inside a method
        print('In which method do you want to add it in?(Type the name or g for global)')
        for method_name in names_of_methods:
            print(method_name)
        inside = input()

        #Check if it should be inside a method
        if inside != 'g':

            #Find the method inside the file contents
            method_index = 0
            for line in lines:
                if inside in line:
                    method_index = lines.index(line) + 1
            
            #Type
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
            if inside == 'bool':
                type = 'bool'

            #Name
            print('Name?')
            name = input()

            #Insert into the file contents
            to_be_inserted = type + ' ' + name + ';\n'
            lines.insert(method_index, to_be_inserted)

        #If it should be global
        else:
            #Public or private
            print('Public or private?(+|-)')
            inside = input()
            pub_pri = ''
            if inside == '+':
                pub_pri = 'public'
            if inside == '-':
                pub_pri = 'private'

            #Type
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
            if inside == 'bool':
                type = 'bool'

            #Name
            print('Name?')
            name = input()

            #Insert into the file contents
            to_be_inserted = pub_pri + ' ' + type + ' ' + name + ';\n'
            lines.insert(index_of_class, to_be_inserted)

    #Ask for something else
    print("Do you want to add something else?(y|n)")
    inside = input()
    if inside == 'n':
        break

#Write back to the file
with open("TestFile.txt", "w") as file:
    for line in lines:
        file.write(line)