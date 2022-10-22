#include <stdio.h>
int main (void) {
int a;
printf ("数値を入力してください=");
scanf ("%d", &a);
if (a > 10)
{
printf ("入力した数値は,'10'より大きいです。\n");
}
else if (a > 5)
{
printf ("入力した数値は,'5'より大きいです。\n");
}
else
{
printf ("入力した数値は,'5'以下です。\n");
}
return 0;
}
