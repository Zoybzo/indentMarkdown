import os
import sys

def indent(file_path):   
    """
    indent the headers of the markdown file
    """
    if not os.path.exists(file_path):
        # throw the error
        raise FileNotFoundError('The file does not exist')
    with open(file_path, 'r') as f:
        lines = f.readlines()
    # check the file exists
    with open(file_path, 'w') as f:
        # read the lines from the file
        for line in lines:
        # if the line begin with '#'
            if line.startswith('#'):
            # change the beginning of the line to '##'
                line = '#' + line 
            # if the line begin with '>' and the next line does not begin with '>', add an empty line after the line
            if line.startswith('>'):
                # get the index of the line
                index = lines.index(line)
                # get the length of lines
                length = len(lines)
                # if the next line does not begin with '>'
                if index + 1 >= length or not lines[index+1].startswith('>'):
                    # add an empty line after the line
                    line += '\n'
            # change the line in the file
            f.write(line)
            # print(line)
    # print the success message
    print('The file has been indented successfully')
    return 

if __name__ == '__main__':
    # get the file path from the augments
    file_path = sys.argv[1]
    # indent the file
    indent(file_path)
    
