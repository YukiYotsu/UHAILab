import sys
import os
from pathlib import Path
import csv
import itertools

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GRASP import core # retrieve the path of the target for the test
from GRASP import ui

grandparent_directory = Path(__file__).resolve().parent.parent
VOCABULARY_FILE_Path = os.path.join(grandparent_directory,'ver1_Programming_vocabulary.csv')

def read_file_as_list(filePath = None):
    """ Make the list of words (vocabulary)

    Keyword Arguments:
        filePath: the path of the file to read

    Returns:
        The list of vocabulary read from CSV file or TXT file
    """
    if filePath[-4:] == '.txt': # for TXT file
        with open(filePath, 'r') as f:
            text_data = [line.strip() for line in f]
        return text_data
    
    elif filePath[-4:] == '.csv': # for CSV file
        with open(filePath, 'r') as f:
            csv_data =  [line for line in csv.reader(f)]
            return list(itertools.chain.from_iterable(csv_data))
    else:
        return None
    
def main():
    """
    """
    dictionary = read_file_as_list(VOCABULARY_FILE_Path)

    ui.spell_check_ui(dictionary)

if __name__ == "__main__":
    main()