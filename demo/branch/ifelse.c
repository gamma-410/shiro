#include <stdio.h>
int main (void) {
// 変数の宣言
int a;
// 数値の入力
printf ("数値を入力してください=");
scanf ("%d", &a);
// 条件分岐
if (a)
{
// 真のときの処理
printf ("真（true）だよ。\n");
printf ("%d\n",a);
}
else
{
// 偽のときの処理
printf ("偽（true）だよ。\n");
printf ("%d\n",a);
}
return 0;
}
