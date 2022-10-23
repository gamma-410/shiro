#include <stdio.h>
int main (void) {
int i = 1;
int sum = 0;
while (sum<100)
{
sum=sum+i;
printf ("(i,sum)=(%d,%d)",i,sum);
i=i+1;
}
return 0;
}
