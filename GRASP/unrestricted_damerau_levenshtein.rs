use std::cmp::min;
use std::collections::HashMap;

pub fn unrestricted_damerau_levenshtein(s1: &str, s2: &str) -> usize {
    let len_s1 = s1.chars().count();
    let len_s2 = s2.chars().count();
    let inf = len_s1 + len_s2;

    let mut d = vec![vec![0; len_s2 + 2]; len_s1 + 2];
    let mut last_row: HashMap<char, usize> = HashMap::new();

    for i in 0..=len_s1 {
        d[i + 1][0] = inf;
        d[i + 1][1] = i;
    }
    for j in 0..=len_s2 {
        d[0][j + 1] = inf;
        d[1][j + 1] = j;
    }

    let s1_chars: Vec<char> = s1.chars().collect();
    let s2_chars: Vec<char> = s2.chars().collect();

    for i in 1..=len_s1 {
        let mut last_match_column = 0;
        for j in 1..=len_s2 {
            let cost = if s1_chars[i - 1] == s2_chars[j - 1] { 0 } else { 1 };

            d[i + 1][j + 1] = min(
                min(d[i][j + 1] + 1, d[i + 1][j] + 1),
                d[i][j] + cost,
            );

            if let Some(&last_matching_row) = last_row.get(&s2_chars[j - 1]) {
                if last_match_column > 0 {
                    d[i + 1][j + 1] = min(
                        d[i + 1][j + 1],
                        d[last_matching_row][last_match_column]
                            + (i - last_matching_row - 1)
                            + 1
                            + (j - last_match_column - 1),
                    );
                }
            }

            if cost == 0 {
                last_match_column = j;
            }
        }
        last_row.insert(s1_chars[i - 1], i);
    }

    d[len_s1 + 1][len_s2 + 1]
}
