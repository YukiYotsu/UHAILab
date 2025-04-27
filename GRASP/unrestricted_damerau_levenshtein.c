#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Damerau-Levenshtein距離を求める関数
int damerau_levenshtein(const char *s1, const char *s2) {
    int len_s1 = strlen(s1);
    int len_s2 = strlen(s2);
    int INF = len_s1 + len_s2; // instead of infinity

    // 動的配列の確保
    int **d = (int **)malloc((len_s1 + 2) * sizeof(int *));
    for (int i = 0; i < len_s1 + 2; i++) {
        d[i] = (int *)malloc((len_s2 + 2) * sizeof(int));
    }

    for (int i = 0; i <= len_s1; i++) {
        d[i + 1][0] = INF;
        d[i + 1][1] = i;
    }
    for (int j = 0; j <= len_s2; j++) {
        d[0][j + 1] = INF;
        d[1][j + 1] = j;
    }

    for (int i = 1; i <= len_s1; i++) {
        for (int j = 1; j <= len_s2; j++) {
            int cost;
            if (s1[i - 1] == s2[j - 1]) {
                cost = 0;
            } else {
                cost = 1;
            }

            int insert = d[i + 1][j] + 1;
            int del = d[i][j + 1] + 1;
            int replace = d[i][j] + cost;

            d[i + 1][j + 1] = replace;
            if (insert < d[i + 1][j + 1]) {
                d[i + 1][j + 1] = insert;
            }
            if (del < d[i + 1][j + 1]) {
                d[i + 1][j + 1] = del;
            }

            // ここが「隣接 transposition」のみ許す部分
            if (i > 1 && j > 1) {
                if (s1[i - 1] == s2[j - 2] && s1[i - 2] == s2[j - 1]) {
                    int transposition = d[i - 1][j - 1] + 1;
                    if (transposition < d[i + 1][j + 1]) {
                        d[i + 1][j + 1] = transposition;
                    }
                }
            }
        }
    }

    int result = d[len_s1 + 1][len_s2 + 1];

    for (int i = 0; i < len_s1 + 2; i++) {
        free(d[i]);
    }
    free(d);

    return result;
}
