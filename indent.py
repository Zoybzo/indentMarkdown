import os
import sys

def indent(file_path):   
    """
    indent the markdown file
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
            # change the line in the file
            f.write(line)
            print(line)
    # print the success message
    print('The file has been indented successfully')
    return 

if __name__ == '__main__':
    # get the file path from the augments
    file_path = sys.argv[1]
    # indent the file
    indent(file_path)
    
