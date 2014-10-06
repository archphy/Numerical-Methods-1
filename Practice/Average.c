#include <stdio.h>


int main(void)
{
	int sum , value ,average ,size;
	sum = 0;
	average = 0 ;
	size = 0 ;

	printf(">> Program asks for input , adds the inputs and return the avarage \n>> Enter 0 to exit \n");

	while(1)
	{
		printf("Enter the input = ");
		scanf("%d",&value);
		if (value == 0)
		{
			printf("0 entered : Program will stop \n");
			break ;
		}
		sum += value; s
		size++;
	}
	
	average = sum / size ;

	printf("The Average is %d", average );


	return 0;
}