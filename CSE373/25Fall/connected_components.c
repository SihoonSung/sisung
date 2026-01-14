#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int n, m, **S, *sz, *ans, ans_cnt = 999;

int check(int *c) {
    for (int i = 1; i <= n; i++) if (!c[i]) return 0;
    return 1;
}

int gain(int *c, int idx) {
    int g = 0;
    for (int j = 0; j < sz[idx]; j++) if (!c[S[idx][j]]) g++;
    return g;
}

int lb(int *c) {
    int r = 0;
    for (int i = 1; i <= n; i++) if (!c[i]) r++;
    if (r == 0) return 0;
    int mg = 0;
    for (int i = 0; i < m; i++) {
        int g = gain(c, i);
        if (g > mg) mg = g;
    }
    return mg > 0 ? (r + mg - 1) / mg : 999;
}

void solve(int *c, int *sol, int cnt, int idx) {
    if (cnt >= ans_cnt || cnt + lb(c) >= ans_cnt) return;
    if (check(c)) {
        ans_cnt = cnt;
        for (int i = 0; i < cnt; i++) ans[i] = sol[i];
        return;
    }
    if (idx >= m) return;
    
    int g = gain(c, idx);
    if (g == 0) {
        solve(c, sol, cnt, idx + 1);
        return;
    }
    
    int *nc = (int*)malloc((n + 1) * sizeof(int));
    memcpy(nc, c, (n + 1) * sizeof(int));
    for (int j = 0; j < sz[idx]; j++) nc[S[idx][j]] = 1;
    sol[cnt] = idx;
    solve(nc, sol, cnt + 1, idx + 1);
    free(nc);
    solve(c, sol, cnt, idx + 1);
}

void greedy(int *c) {
    int cnt = 0, *s = (int*)malloc(m * sizeof(int));
    while (!check(c)) {
        int b = -1, mg = 0;
        for (int i = 0; i < m; i++) {
            int g = gain(c, i);
            if (g > mg) { mg = g; b = i; }
        }
        if (b == -1) break;
        s[cnt++] = b;
        for (int j = 0; j < sz[b]; j++) c[S[b][j]] = 1;
    }
    ans_cnt = cnt;
    for (int i = 0; i < cnt; i++) ans[i] = s[i];
    free(s);
}

void sort(int *a, int len) {
    for (int i = 1; i < len; i++) {
        int x = a[i], j = i - 1;
        while (j >= 0 && a[j] > x) { a[j + 1] = a[j]; j--; }
        a[j + 1] = x;
    }
}

int main(void) {
    scanf("%d %d", &n, &m);
    S = (int**)malloc(sizeof(int*) * m);
    sz = (int*)calloc(m, sizeof(int));
    ans = (int*)malloc(m * sizeof(int));
    char *line = NULL;
    size_t cap = 0;
    getchar();
    for (int i = 0; i < m; i++) {
        S[i] = (int*)malloc(sizeof(int) * n);
        getline(&line, &cap, stdin);
        char *p = strtok(line, " \t\r\n");
        while (p) {
            int v = atoi(p);
            if (1 <= v && v <= n) S[i][sz[i]++] = v;
            p = strtok(NULL, " \t\r\n");
        }
    }
    free(line);
    int *c = (int*)calloc(n + 1, sizeof(int));
    int *sol = (int*)malloc(m * sizeof(int));
    greedy(c);
    memset(c, 0, (n + 1) * sizeof(int));
    solve(c, sol, 0, 0);
    for (int i = 0; i < ans_cnt; i++) ans[i]++;
    sort(ans, ans_cnt);
    printf("%d\n", ans_cnt);
    for (int i = 0; i < ans_cnt; i++) printf("%s%d", i ? " " : "", ans[i]);
    printf("\n");
    for (int i = 0; i < m; i++) free(S[i]);
    free(S);
    free(sz);
    free(ans);
    free(c);
    free(sol);
    return 0;
}