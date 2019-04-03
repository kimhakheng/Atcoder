#include<stdio.h>
main()
{
	int a,b=1,c;
	printf("Enter the number of terms: ");
	scanf("%d",&a);
	for (c=1;c<=a;c++)
	{
		b=b*c;
	}
	printf ("The fatorial of given number is %d",b);
}
