from pathlib import Path
import re
import os
import collections
import time
import csv
from config import USER_DEFINED_CORRECTIONS_FILE_Path

# this stores which are adjacent keys on a keyboard
KEYBOARD_ADJACENCY = {
    'q': {'w', 'a'}, 'w': {'q', 'e', 's', 'a'}, 'e': {'w', 'r', 'd', 's'}, 'r': {'e', 't', 'f', 'd'}, 't': {'r', 'y', 'g', 'f'},
    'y': {'t', 'u', 'h', 'g'}, 'u': {'y', 'i', 'j', 'h'}, 'i': {'u', 'o', 'k', 'j'}, 'o': {'i', 'p', 'l', 'k'}, 'p': {'o', 'l'},
    'a': {'q', 's', 'z'}, 's': {'a', 'w', 'd', 'x', 'e', 'z'}, 'd': {'s', 'e', 'f', 'c','r','x'}, 'f': {'d', 'r', 'g', 'v', 't', 'c'},
    'g': {'f', 't', 'h', 'b', 'v', 'y'}, 'h': {'g', 'y', 'j', 'n', 'b', 'u'}, 'j': {'h', 'u', 'k', 'm', 'i', 'n'}, 'k': {'j', 'i', 'l','o','m'},
    'l': {'k', 'o', ';'}, 'z': {'a', 'x'}, 'x': {'z', 's', 'c'}, 'c': {'x', 'd', 'v'}, 'v': {'c', 'f', 'b'},
    'b': {'v', 'g', 'n','h'}, 'n': {'b', 'h', 'm', 'j'}, 'm': {'n', 'j', 'k'},
}

# this stores words which have irregular variation
IRREGULAR_WORDS = {
    "went": "go", "gone": "go",
    "better": "good", "best": "good",
    "children": "child", "men": "man", "women": "woman",
    "mice": "mouse", "geese": "goose",
    "ran": "run", "saw": "see", "seen": "see",
    "did": "do", "done": "do",
    "had": "have", "has": "have",
    "was": "be", "were": "be", "am": "be", "is": "be", "are": "be",
}

def lemmatize(word):
    """ Lemmatize word (convert words into lemma)
    """
    # check if a word is in irregular words
    word_lower = word.lower()
    if word_lower in IRREGULAR_WORDS:
        return IRREGULAR_WORDS[word_lower]
    
    # multiple expressions
    if re.match(r".+ies$", word):
        return word[:-3] + "y"
    if re.match(r".+ves$", word):
        return word[:-3] + "f"
    if re.match(r".+oes$", word) or re.match(r".+ses$", word):
        return word[:-2]
    if re.match(r".+s$", word) and not re.match(r".+ss$", word):
        return word[:-1]
    
    # # past expressions
    # if re.match(r".+ed$", word):
    #     if re.match(r".+ied$", word):
    #         return word[:-3] + "y"
    #     return word[:-2]
    
    # -ing expressions
    if re.match(r".+ing$", word):
        if re.match(r".+ying$", word):
            return word[:-3] + "ie"
        return word[:-3]
    
    return word # if no grammar rule cannot apply

def get_keyboard_distance(char1, char2):
    """ Returns the cost, given the keys' adhacency.

    Keyword Arguments:
        char1, char2: these are a character to check if they are adjacent

    Returns:
        0: those characters are the same.
        0.2: those characters are not the same but adjacent.
        1: those characters are not adjacent and different.
    """
    if char1 == char2:
        return 0
    elif char1 in KEYBOARD_ADJACENCY and char2 in KEYBOARD_ADJACENCY[char1]:
        return 0.2
    return 1

class TrieNode:
    """ Represents nodes of Trie

    Each of nodes has 'children' and 'is_end_of_word'
    Keyword Arguments:
        children: storing children nodes
        char: a character to be stored in each
        is_end_of_word: a flag which shows us if it is the end of word
    """
    def __init__(self, char=None):
        """ A constructer of class TrieNode
        
        Args:
            Nothing
        
        Returns:
            Nothing
        """
        self.char = char
        self.children = collections.defaultdict(TrieNode)
        self.is_end_of_word = False

class Trie:
    """ Represents data construction

    Keyword Arguments:
        root: a root node of Trie
    """
    def __init__(self):
        """ Initialize a root node
        
        A constructer of class Trie
        Args:
            Nothing
        
        Returns:
            Nothing
        """
        self.root = TrieNode()
    
    def insert(self, word):
        """ Insert a word into Trie (ALWAYS conver to lowercase)

        Keyword Arguments:
            word: a word to be inserted
        
        Returns:
            Nothing
        """
        word = word.lower() # convert to lowercase
        node = self.root
        for char in word:
            # create a new node for the character if it doesn't exist
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        """ Search a word and see whether the specific word exists or not (ALWAYS conver to lowercase)

        Keyword Arguments:
            word: a word to be searched
        
        Returns:
            node.is_end_of_word: bool type;
                return 'True' if the word exists.
        """
        word = word.lower() # convert to lowercase
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

def damerau_levenshtein_distance(s1, s2):
    """ Compute restricted Damerau Levenshtein distance

    Keyword Arguments:
        s1, s2: strings where the distance is computed
    
    Returns:
        d: array which distances' data has put 
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

def unrestricted_damerau_levenshtein_distance(s1, s2):
    """ Compute unrestricted Damerau Levenshtein distance

    This is treated as a true distance in general.
    Keyword Arguments:
        s1, s2: strings where the distance is computed
    
    Returns:
        d: array which distances' data has put 
    """
    len_s1, len_s2 = len(s1), len(s2)
    INF = len_s1 + len_s2 # large number instead of infinity
    
    d = [[0] * (len_s2 + 2) for _ in range(len_s1 + 2)]
    last_row = {}
    
    for char in set(s1 + s2):
        last_row[char] = 0
    
    for i in range(len_s1 + 1):
        d[i + 1][0] = INF
        d[i + 1][1] = i
    
    for j in range(len_s2 + 1):
        d[0][j + 1] = INF
        d[1][j + 1] = j
    
    for i in range(1, len_s1 + 1):
        last_match_column = 0
        for j in range(1, len_s2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            d[i + 1][j + 1] = min(
                d[i][j + 1] + 1,  # deletion/削除
                d[i + 1][j] + 1,  # insertion/挿入
                d[i][j] + cost   # substitution/置換
            )
            # transportation/転置
            last_matching_row = last_row.get(s2[j - 1], 0)
            last_matching_col = last_match_column
            if last_matching_row > 0 and last_matching_col > 0:
                d[i + 1][j + 1] = min(
                    d[i + 1][j + 1], d[last_matching_row][last_matching_col] + (i - last_matching_row - 1) + 1 + (j - last_matching_col - 1)
                )
            if cost == 0:
                last_match_column = j
        
        last_row[s1[i - 1]] = i
    
    return d[len_s1 + 1][len_s2 + 1]

def extract_identifiers(code):
    """ Extract specific expressions and return

    Keyword Arguments:
        code: specific expressions / phrases to search
    
    Returns:
        phrases found in text, code, or sentence
    """
    return set(re.findall(r'\b[A-Za-z_][A-Za-z0-9_]*\b', code))

def get_closest_word(word, vocabulary):
    """ Return the closest word in str-form

    This function uses unlimited_damerau_levenshtein_distance.  

    Keyword Arguments:
        word: candidate word to check how / if the word matches
        vocabulary: in other words, dictionary which has correctly-spelled words.
        length_threshold: distance threshold, which makes the program not consider a word misspelled 
                    if it exceeds the threshold
        
    Returns:
        closest_word: the str-form closest word
    """
    if not vocabulary:
        return None
    
    min_distance = float('inf')
    closest_word = None
    lemma_word = lemmatize(word)
    
    print(f"Checking word: {word} (Lemma: {lemma_word})")

    for dict_word in vocabulary:
        distance = unrestricted_damerau_levenshtein_distance(lemma_word, dict_word)

        for i in range(min(len(lemma_word), len(dict_word))):
            if lemma_word[i] != dict_word[i]:
                distance += get_keyboard_distance(lemma_word[i], dict_word[i])

        adaptive_threshold = max(3, len(lemma_word) // 2 + 1)

        if distance < min_distance:
            min_distance = distance
            closest_word = dict_word
            print(f"Comparing with: {dict_word}, Distance: {distance}")
    
    print(f"Final closest word: {closest_word}")
    return closest_word if min_distance < adaptive_threshold else "❓UNIQUE"


def spell_check_code(code, dictionary):
    """ Check the code is correctly spelled or not

    Keyword Arguments:
        code: specific expressions / phrases to search
        dictionary: vocaburaly (words) which checked target code refers to

    Returns:
        suggestions (dict) : suggestions for correrctly-spelled words after checked
    
    Features for Devs:
        In this method, return the executing time and the number of characters 
        to grasp this application performance.
    """
    start_time = time.time() # to get working time
    char_count = len(code) # to get the number of character

    identifiers = {word.lower() for word in extract_identifiers(code)}
    trie = Trie()
    for word in dictionary:
        trie.insert(lemmatize(word.lower()))
    
    suggestions = {}
    for identifier in identifiers:
        lemma_identifier = lemmatize(identifier)
        if not trie.search(lemma_identifier):
            suggestion = get_closest_word(lemma_identifier, dictionary)
    
            suggestions[identifier] = suggestion
    
    execution_time = time.time() - start_time
    print("⏳Execution time is:")
    print(execution_time)
    print("📝The number of character: ")
    print(char_count)
    return suggestions

def load_user_defined_corrections(file_path):
    """Load user-defined spelling corrections from a CSV file.

    Args:
        file_path (str): Path to the user-defined corrections CSV file.

    Returns:
        dict: A dictionary mapping misspelled words to their correct forms.
    """
    try:
        corrections =[]
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if len(row) == 2:
                    corrections.append(row[1].strip())
    except FileNotFoundError:
        print(f"‼️ User-defined corrections file not found: {file_path}")
    return corrections

def save_user_defined_correction(misspelled, correct):
    """ Save a user-defined spelling correction to CSV
    """
    with open(USER_DEFINED_CORRECTIONS_FILE_Path, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([misspelled, correct])