# project
#include <iostream>#include <cstring>#include <stdlib.h>
using namespace std;
int T, K;int p[101], num[101], d[101][10001];
int main() { scanf_s("%d %d", &T, &K); for (int i = 1; i <= K; i++)  scanf_s("%d %d", &p[i], &num[i]);
 d[0][0] = 1; for (int i = 1; i <= K; i++) {  for (int j = 0; j <= T; j++) {   for (int k = 0; j >= k*p[i] && k <= num[i]; k++)    d[i][j] += d[i - 1][j - k*p[i]];  } }
 printf("%d\n", d[K][T]); return 0;}
