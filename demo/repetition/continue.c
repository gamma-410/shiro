#include <stdio.h>
int main (void) {
int i;
for (i=0;i<10;i++)
{
if (i==5)
{
continue;
}
if (i==7)
{
continue;
}
printf ("Hello!-%d\n",i);
}
return 0;
}
