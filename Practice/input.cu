/*
*
*	input.cu
*	
*
*
*
*/

#include <stdio.h>

int main(void)
{
	int val ;
	int status = 0 ; 


	while(status < 1)
	{
		printf("Enter an interger : ");
		status = scanf("%d",&val);

		if (status == 0 )
		{
			printf("Exited!");
		}
	}
	printf("%d",val);
	printf("\n");


	printf(">> COUNTING NUMBER OF DIGITS");
	printf("\n");

	int num = val ;
	int digits = 0 ; 

	while(num != 0 )
	{
		num /= 10 ; 
		digits++;
	}

	printf("%d",digits);
	printf("\n");


	printf(">> REVERSE NUMBER OF DIGITS");
	printf("\n");

	int rev = 0 ; 
	num = val ; 

	while(num != 0 )
	{
		rev *= 10; 
		rev += num % 10 ; 
		num /= 10 ; 
	}	

	printf("INPUT : %d",val);
	printf("\n");
	
	printf("REVERSE : %d",rev);

	printf("\n");

}