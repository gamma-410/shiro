#include <stdio.h>
int main (void) {
int a;
printf ("数値を入力してください。>>>");
scanf ("%d", &a);
switch (a)
{
case 0:
printf ("0だよ。\n");
break;
case 1:
printf ("1だよ。\n");
break;
case 2:
printf ("2だよ。\n");
break;
case 3:
printf ("3だよ。\n");
break;
case 4:
printf ("4だよ。\n");
break;
case 5:
printf ("5だよ。\n");
break;
default:
printf ("それ以外だよ。");
break;
}
return 0;
}
