#include <stdio.h>
int main (void) {
int a;
printf ("数値を入力してください=");
scanf ("%d", &a);
if (a>=10&&a<=20)
{
printf ("入力した数値は,'10以上','20以下'です。\n");
}
return 0;
}
