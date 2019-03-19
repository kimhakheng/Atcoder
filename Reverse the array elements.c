//1. Reverse the array elements
#include<stdio.h>
void main()
{ int a[30],i,j,n,temp;
printf("\n Enter no of elements :");
scanf("%d",&n);
for(i=0 ; i < n ; i++)
scanf("%d",&a[i]);
j = i-1; // j will Point to last Element
i = 0; // i will be pointing to first element
while(i < j)
{ temp = a[i];
a[i] = a[j];
a[j] = temp;
i++;
j--; }
for(i = 0 ;i< n ;i++)
printf("\n %d",a[i]);
}

