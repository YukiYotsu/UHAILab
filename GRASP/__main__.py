import sys
import os
from pathlib import Path
import csv
from config import USER_DEFINED_CORRECTIONS_FILE_Path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GRASP import core # retrieve the path of the target for the test
from GRASP import ui

grandparent_directory = Path(__file__).resolve().parent.parent
VOCABULARY_FILE_Path = os.path.join(grandparent_directory,'ver2_vocabulary.csv')

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
        vocabulary = []
        with open(filePath, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader, None)
            for row in csv_reader:
                if len(row) > 1:
                    vocabulary.append(row[1].strip())
            vocabulary.append('penguin') # append the word of 'penguin'
            return vocabulary # Extract only 'lemma' column
    else:
        return None

def merge_dictionaries(base_dict, user_dict):
    """Merge base dictionary and user-defined corrections.

    Args:
        base_dict (list): List of correctly spelled words from the base dictionary.
        user_dict (list): Dictionary of user-defined corrections.

    Returns:
        list: Merged dictionary list.
    """
    return base_dict + user_dict

def main():
    """ Set dictionary and execute UI setting

    Args:
        Nothing
        
    Returns:
        Nothing
    """
    dictionary = read_file_as_list(VOCABULARY_FILE_Path)
    user_defined_corrections = core.load_user_defined_corrections(USER_DEFINED_CORRECTIONS_FILE_Path)
    
    # renew the dictionary
    dictionary = merge_dictionaries(dictionary, user_defined_corrections)

    ui.spell_check_ui(dictionary)

if __name__ == "__main__":
    # this is implemented only when this python file is selected directly.
    main()