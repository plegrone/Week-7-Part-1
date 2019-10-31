

#This function reads from a file and replaces a word with another that a user is prompted to input
#Try statements inserted for opening, reading, writing, and closing files that will result in specific error statements if they fail

def sed(search_for, replace_with, source_file, destination_file):
    try:
        fin = open(source_file, 'r')
        fout = open(destination_file, 'w')
    except:
        print('Cannot open file!')
        
    for line in fin:
        try:
            line = line.replace(search_for, replace_with)
        except:
            print('Cannot read file')

        try:
            fout.write(line)
        except:
            print('Cannot write to file!')

    try:
        fin.close()
        fout.close()
    except:
        print('Cannot close file!')

search_for = 'Emma'
replace_with = 'EMMA! EMMA! EMMA!'
source_file = 'emma.txt'
destination_file = source_file + 'NEW.replaced'
sed(search_for, replace_with, source_file, destination_file)

