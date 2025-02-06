import subprocess
import os
from pathlib import Path
import re
import collections

class TrieNode:
    """ Represents nodes of Trie

    Each of nodes has 'children' and 'is_end_of_word'
    Keyword Arguments:
        children: storing children nodes
        is_end_of_word: a flag which shows us if it is the end of word
    """
    def __init__(self):
        """ A constructer of class TrieNode
        
        Args:
            Nothing
        
        Returns:
            Nothing
        """
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
        """ Insert a word into Trie

        Keyword Arguments:
            word: a word to be inserted
        
        Returns:
            Nothing
        """
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        """ Search a word and see whether the specific word exists or not

        Keyword Arguments:
            word: a word to be searched
        
        Returns:
            node.is_end_of_word: bool type;
                return 'True' if the word exists.
        """
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
                d[i][j] + cost    # substitution/置換
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

def compute_lps(pattern):
    """ Calculate LPS (Longest proper Prefix Suffix)

    Keyword Arguments:
        pattern: specific strings which are tested to see whether they matches

    Returns:
        lps: array which represents a match between prefix and suffix
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length -1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(pattern, text):
    """ Search a string in given texts with KMP algorithm

    Keyword Arguments:
        pattern: specific strings which are tested to see whether they matches
        text: strings (words) to search in
    
    Returns:
        matches: certain position where pattern is found
    """
    lps = compute_lps(pattern)
    i, j = 0, 0
    matches = []
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            j = lps[j - 1] if j != 0 else 0
            i += 1 if j == 0 else 0
    return matches

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
    import jellyfish
    if not vocabulary:
        return None
    
    length_threshold = max(2, len(word) // 2)

    min_distance = float('inf')
    closest_word = None
    
    for dict_word in vocabulary:
        distance = jellyfish.damerau_levenshtein_distance(word, dict_word)

        adaptive_threshold = length_threshold

        if any(char.isdigit() or not char.isalnum() for char in word):
            adaptive_threshold += 1

        if distance <= adaptive_threshold and distance < min_distance:
            min_distance = distance
            closest_word = dict_word
    
    # Here, exclude a word which exceeds threshold.
    if min_distance >= length_threshold:
        return 'UNIQUE expression'
    
    return closest_word

def spell_check_code(code, dictionary):
    """ Check the code is correctly spelled or not

    Keyword Arguments:
        code: specific expressions / phrases to search
        dictionary: vocaburaly (words) which checked target code refers to

    Returns:
        suggestions (dict) : suggestions for correrctly-spelled words after checked
        unique_expressions (list) :
            this stores expressions regarded a unique word
    """
    identifiers = extract_identifiers(code)
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    
    suggestions = {}
    unique_expressions = []

    for identifier in identifiers:
        if not trie.search(identifier):
            suggestion = get_closest_word(identifier, dictionary)
            if suggestion == 'UNIQUE expression':
                unique_expressions.append(identifier)
            else:
                suggestions[identifier] = suggestion
    
    return suggestions, unique_expressions