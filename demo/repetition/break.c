#include <stdio.h>
int main (void) {
int i;
for (i=0;i<10;i++)
{
printf ("Hello!-%d\n",i);
if (i==5)
{
break;
}
}
return 0;
}
