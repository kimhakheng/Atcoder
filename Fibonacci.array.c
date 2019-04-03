#include<stdio.h>
main() 
{
	int i,a[50];
	//printf("Enter the number of the terms of sequence: ");
	//scanf("%d",&n);//n=5
	a[0]=0;
	a[1]=1;
	for(i=2;i<=49;i++)
	{
		a[i]=a[i-1]+a[i-2];
	}
	for(i=0;i<=49;i++)
	{
		printf("%d, ",a[i]);
	}
	printf("...");
}
