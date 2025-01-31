import subprocess
import os
from pathlib import Path
import collections
import csv
import itertools

grandparent_directory = Path(__file__).resolve().parent.parent
VOCABULARY_FILE_Path = os.path.join(grandparent_directory,'ver1_Programming_vocabulary.csv')

class TrieNode:
    """
    """
    def __init__(self):
        """
        """
        self.children = collections.defaultdict(TrieNode)
        self.is_end_of_word = False

class Trie:
    """
    """
    def __init__(self):
        """
        """
        self.root = TrieNode()
    
    def insert(self, word):
        """
        """
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        """
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

def damerau_levenshtein_distance(s1, s2):
    """
    """
    d = [[i+j if i * j == 0 else 0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            d[i][j] = min(
                d[i-1][j] + 1,    # deletion/削除
                d[i][j-1] + 1,    # insertion/挿入
                d[i-1][j-1] + cost  # substitution/置換
            )
            
            if i > 1 and j > 1 and s1[i-1] == s2[j-2] and s1[i-2] == s2[j-1]:
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + 1)  # transposition/隣り合う文字の交換
    
    return d[len(s1)][len(s2)]

def get_closest_word(word, trie, vocabulary):
    """
    """
    min_distance = float('inf')
    closest_word = None
    
    for vocab_word in vocabulary:
        distance = damerau_levenshtein_distance(word, vocab_word)
        if distance < min_distance:
            min_distance = distance
            closest_word = vocab_word
    
    return closest_word

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
    vocabulary = read_file_as_list(VOCABULARY_FILE_Path)
    trie = Trie()
    for word in vocabulary:
        trie.insert(word)
    
    while True:
        word = input("Enter a word (or type 'exit' to quit): ")
        if word == "exit":
            break
        
        if trie.search(word):
            print(f"'{word}' is spelled correctly.")
        else:
            suggestion = get_closest_word(word, trie, vocabulary)
            print(f"'{word}' is not in the vocabulary. Did you mean '{suggestion}'?")

def connectiontest(arg1: int, arg2: int):
    """ Test stable relations between some files in different python programs

    Keyword arguments:
        arg1 (int): The number of candidate number decided by the programmer
        arg2 (int): The other number of candidate number decided by the programmer

    Returns:
        int: The sum of arg1 and arg2
    """
    
    return arg1 + arg2

if __name__ == "__main__":
    # this is implemented only when this python file is selected directly.
    main()