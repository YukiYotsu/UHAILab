use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io::{self, BufRead, BufReader, Write};
use std::path::Path;
use std::time::Instant;
use lazy_static::lazy_static;
use regex::Regex;
use std::sync::Mutex;

mod unrestricted_damerau_levenshtein;
use unrestricted_damerau_levenshtein::unrestricted_damerau_levenshtein;

lazy_static! {
    static ref KEYBOARD_ADJACENCY: HashMap<char, HashSet<char>> = {
        let mut m = HashMap::new();
        m.insert('q', vec!['w', 'a'].into_iter().collect());
        m.insert('w', vec!['q', 'e', 's', 'a'].into_iter().collect());
        m.insert('e', vec!['w', 'r', 'd', 's'].into_iter().collect());
        m.insert('r', vec!['e', 't', 'f', 'd'].into_iter().collect());
        m.insert('t', vec!['r', 'y', 'g', 'f'].into_iter().collect());
        m.insert('y', vec!['t', 'u', 'h', 'g'].into_iter().collect());
        m.insert('u', vec!['y', 'i', 'j', 'h'].into_iter().collect());
        m.insert('i', vec!['u', 'o', 'k', 'j'].into_iter().collect());
        m.insert('o', vec!['i', 'p', 'l', 'k'].into_iter().collect());
        m.insert('p', vec!['o', 'l'].into_iter().collect());
        m
    };
    
    static ref IRREGULAR_WORDS: HashMap<&'static str, &'static str> = {
        let mut m = HashMap::new();
        m.insert("went", "go");
        m.insert("gone", "go");
        m.insert("better", "good");
        m.insert("best", "good");
        m.insert("children", "child");
        m.insert("men", "man");
        m.insert("women", "woman");
        m.insert("mice", "mouse");
        m.insert("geese", "goose");
        m.insert("ran", "run");
        m.insert("saw", "see");
        m.insert("seen", "see");
        m.insert("did", "do");
        m.insert("done", "do");
        m.insert("had", "have");
        m.insert("has", "have");
        m.insert("was", "be");
        m.insert("were", "be");
        m.insert("am", "be");
        m.insert("is", "be");
        m.insert("are", "be");
        m
    };
}

struct TrieNode {
    children: HashMap<char, TrieNode>,
    is_end_of_word: bool,
}

impl TrieNode {
    fn new() -> Self {
        TrieNode {
            children: HashMap::new(),
            is_end_of_word: false,
        }
    }
}

struct Trie {
    root: TrieNode,
}

impl Trie {
    fn new() -> Self {
        Trie {
            root: TrieNode::new(),
        }
    }

    fn insert(&mut self, word: &str) {
        let mut node = &mut self.root;
        for c in word.chars() {
            node = node.children.entry(c).or_insert_with(TrieNode::new);
        }
        node.is_end_of_word = true;
    }

    fn search(&self, word: &str) -> bool {
        let mut node = &self.root;
        for c in word.chars() {
            if let Some(next) = node.children.get(&c) {
                node = next;
            } else {
                return false;
            }
        }
        node.is_end_of_word
    }
}

fn lemmatize(word: &str) -> String {
    let irregular_words: HashMap<&str, &str> = [
        ("went", "go"), ("gone", "go"),
        ("better", "good"), ("best", "good"),
        ("children", "child"), ("men", "man"), ("women", "woman"),
        ("mice", "mouse"), ("geese", "goose"),
        ("ran", "run"), ("saw", "see"), ("seen", "see"),
        ("did", "do"), ("done", "do"),
        ("had", "have"), ("has", "have"),
        ("was", "be"), ("were", "be"), ("am", "be"), ("is", "be"), ("are", "be"),
    ].iter().cloned().collect();

    let word_lower = word.to_lowercase();

    if let Some(lemma) = irregular_words.get(word_lower.as_str()) {
        return lemma.to_string();
    }

    let re_ies = Regex::new(r".+ies$").unwrap();
    let re_ves = Regex::new(r".+ves$").unwrap();
    let re_oes = Regex::new(r".+oes$").unwrap();
    let re_ses = Regex::new(r".+ses$").unwrap();
    let re_s = Regex::new(r".+s$").unwrap();
    let re_ing = Regex::new(r".+ing$").unwrap();

    if re_ies.is_match(&word_lower) {
        return format!("{}y", &word_lower[..word_lower.len()-3]);
    }
    if re_ves.is_match(&word_lower) {
        return format!("{}f", &word_lower[..word_lower.len()-3]);
    }
    if re_oes.is_match(&word_lower) || re_ses.is_match(&word_lower) {
        return format!("{}", &word_lower[..word_lower.len()-2]);
    }
    if re_s.is_match(&word_lower) && !word_lower.ends_with("ss") {
        return format!("{}", &word_lower[..word_lower.len()-1]);
    }
    if re_ing.is_match(&word_lower) {
        if Regex::new(r".+[^aeiou][^aeiou]ing$").unwrap().is_match(&word_lower) {
            return format!("{}", &word_lower[..word_lower.len()-4]);
        }
        return format!("{}", &word_lower[..word_lower.len()-3]);
    }

    word_lower
}

fn remove_ly_suffix(word: &str) -> String {
    if word.ends_with("ly") {
        return word[..word.len()-2].to_string();
    }
    word.to_string()
}

fn get_keyboard_distance(char1: char, char2: char) -> f32 {
    let mut keyboard_adjacency: HashMap<char, HashSet<char>> = HashMap::new();

    keyboard_adjacency.insert('q', vec!['w', 'a'].into_iter().collect());
    keyboard_adjacency.insert('w', vec!['q', 'e', 's', 'a'].into_iter().collect());
    keyboard_adjacency.insert('e', vec!['w', 'r', 'd', 's'].into_iter().collect());
    keyboard_adjacency.insert('r', vec!['e', 't', 'f', 'd'].into_iter().collect());
    keyboard_adjacency.insert('t', vec!['r', 'y', 'g', 'f'].into_iter().collect());
    keyboard_adjacency.insert('y', vec!['t', 'u', 'h', 'g'].into_iter().collect());
    keyboard_adjacency.insert('u', vec!['y', 'i', 'j', 'h'].into_iter().collect());
    keyboard_adjacency.insert('i', vec!['u', 'o', 'k', 'j'].into_iter().collect());
    keyboard_adjacency.insert('o', vec!['i', 'p', 'l', 'k'].into_iter().collect());
    keyboard_adjacency.insert('p', vec!['o', 'l'].into_iter().collect());

    if char1 == char2 {
        return 0.0;
    } else if let Some(adjacent_chars) = keyboard_adjacency.get(&char1) {
        if adjacent_chars.contains(&char2) {
            return 0.2;
        }
    }
    0.45
}

// we need to add ' and "
fn split_code(code: &str) -> Vec<String> {
    let re = Regex::new(r"[\s\.\:\;\,\-\/\(\)]+").unwrap();
    re.split(code)
        .filter_map(|token| {
            let trimmed = token.trim();
            if !trimmed.is_empty() {
                Some(trimmed.to_string())
            } else {
                None
            }
        })
        .collect()
}

fn merge_dictionaries(base_dict: Vec<String>, user_dict: Vec<String>) -> Vec<String> {
    [base_dict, user_dict].concat()
}

fn get_closest_word(word: &str, dictionary: &HashSet<String>) -> Option<String> {
    let mut min_distance = usize::MAX;
    let mut closest_word = None;
    
    for dict_word in dictionary {
        let distance = damerau_levenshtein(word, dict_word);
        if distance < min_distance {
            min_distance = distance;
            closest_word = Some(dict_word.clone());
        }
    }
    closest_word
}

fn load_user_defined_corrections(file_path: &str) -> HashMap<String, String> {
    let path = Path::new(file_path);
    let mut corrections = HashMap::new();
    if let Ok(file) = File::open(path) {
        for line in BufReader::new(file).lines() {
            if let Ok(entry) = line {
                let parts: Vec<&str> = entry.split(',').collect();
                if parts.len() == 2 {
                    corrections.insert(parts[0].to_string(), parts[1].to_string());
                }
            }
        }
    }
    corrections
}

fn save_user_defined_correction(file_path: &str, incorrect: &str, correct: &str) {
    let mut file = OpenOptions::new().append(true).create(true).open(file_path).unwrap();
    writeln!(file, "{},{}", incorrect, correct).unwrap();
}

// Spell check function
fn spell_check_code(code: &str, dictionary: &HashSet<String>, user_dict_path: &str) -> HashMap<String, String> {
    let start_time = std::time::Instant::now();
    let char_count = code.len();
    let user_corrections = load_user_defined_corrections(user_dict_path);
    let mut full_dict = dictionary.clone();
    full_dict.extend(user_corrections);

    let words: Vec<&str> = code.split(|c: char| !c.is_alphanumeric()).filter(|s| !s.is_empty()).collect();
    let mut suggestions = HashMap::new();

    for word in words {
        if !full_dict.contains(word) {
            let suggestion = get_closest_word(word, &full_dict);
            suggestions.insert(word.to_string(), suggestion);
        }
    }

    let execution_time = start_time.elapsed();
    println!("⏳ Execution time: {:?}", execution_time);
    println!("📝 Character count: {}", char_count);
    suggestions
}