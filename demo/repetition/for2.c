#include <stdio.h>
int main (void) {
int i;
int sum = 0;
for (i=0;i<=100;i++)
{
printf ("%d\n",i);
sum+=i;
}
printf ("\n合計=%d\n",sum);
return 0;
}
