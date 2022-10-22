#include <stdio.h>
int main (void) {
// "変換指定子"
// char
// int
// float
// double
printf ("標準出力の書式\n");
printf ("Hello,World!\n");
// 文字型
char text;
text = 'A';
printf ("こんにちは、%c\n",text);
// 整数型
int a,b,c;
a = 1;
b = 2;
c = 3;
printf ("%d、%d、%d、です。\n",a,a+b,c);
// 浮動小数点数型（単精度実数)
float x;
x = 33.333;
printf ("%f\n",x);
return 0;
}
