#include <stdio.h>
int main (void) {
// 変数の定義
int x,y,z;
// xの数値を入力
printf ("Input\n");
printf ("x=");
scanf ("%d", &x);
// yの数値を入力
printf ("y=");
scanf ("%d", &y);
// x+yを計算
z = x+y;
// 入力した数値の出力
printf ("\nOutput\n");
printf ("x=%d\n",x);
printf ("y=%d\n",y);
// 計算した和の出力
printf ("x+y=%d\n",z);
return 0;
}
