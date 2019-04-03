#include<stdio.h>
main()
{
	float a,b,c;
	printf("Enter the value of a");
	scanf("%f",&a);
	printf("Enter the value of b");
	scanf("%f",&b);
	printf("Enter the value of c");
	scanf("%f",&c);
	if(a>b||b>c)
	{
		if(a>b)
		{
			printf("%.2f is the greatest number",a);	
		}
		else
		{
			printf("%.2f is the greatest number",b);
		}
	}
	else
	{
		printf("%.2f is the greatest number",c);
	}
}
