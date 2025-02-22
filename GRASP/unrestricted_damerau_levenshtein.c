#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

// Damerau-Levenshtein距離を求める関数
int unrestricted_damerau_levenshtein(const char *s1, const char *s2) {
    int len_s1 = strlen(s1);
    int len_s2 = strlen(s2);
    int INF = len_s1 + len_s2; // 無限大の代わり

    // 動的配列の確保
    int **d = (int **)malloc((len_s1 + 2) * sizeof(int *));
    for (int i = 0; i < len_s1 + 2; i++) {
        d[i] = (int *)malloc((len_s2 + 2) * sizeof(int));
    }

    // ASCII文字用のlast_row
    int last_row[256] = {0}; 

    for (int i = 0; i <= len_s1; i++) {
        d[i + 1][0] = INF;
        d[i + 1][1] = i;
    }
    for (int j = 0; j <= len_s2; j++) {
        d[0][j + 1] = INF;
        d[1][j + 1] = j;
    }

    for (int i = 1; i <= len_s1; i++) {
        int last_match_column = 0;
        for (int j = 1; j <= len_s2; j++) {
            int cost = (s1[i - 1] == s2[j - 1]) ? 0 : 1;

            d[i + 1][j + 1] = 
                (d[i][j + 1] + 1 < d[i + 1][j] + 1) ? 
                ((d[i][j + 1] + 1 < d[i][j] + cost) ? d[i][j + 1] + 1 : d[i][j] + cost) :
                ((d[i + 1][j] + 1 < d[i][j] + cost) ? d[i + 1][j] + 1 : d[i][j] + cost);

            int last_matching_row = last_row[(unsigned char)s2[j - 1]];
            int last_matching_col = last_match_column;
            if (last_matching_row > 0 && last_matching_col > 0) {
                d[i + 1][j + 1] = 
                    (d[i + 1][j + 1] < d[last_matching_row][last_matching_col] + 
                     (i - last_matching_row - 1) + 1 + (j - last_matching_col - 1)) ? 
                    d[i + 1][j + 1] :
                    d[last_matching_row][last_matching_col] + 
                    (i - last_matching_row - 1) + 1 + (j - last_matching_col - 1);
            }

            if (cost == 0) {
                last_match_column = j;
            }
        }
        last_row[(unsigned char)s1[i - 1]] = i;
    }

    // 計算結果取得
    int result = d[len_s1 + 1][len_s2 + 1];

    // メモリ解放
    for (int i = 0; i < len_s1 + 2; i++) {
        free(d[i]);
    }
    free(d);

    return result;
}
