
#include <stdio.h>

//Function prototype

__global__ void square(int *a , int *b);


int askInput();



int main(void)
{
	int threads = askInput();

	//char * lable1[] = "Enter Number of Threads to be executed ";
	//char * lable2[] = "No of threads = ";
	

	//No of threads 
	int N = threads;

	//Size of array 
	int *a , *b ;
	int *Da , *Db ; 
	int size = N * sizeof(int);


	//Allocate memory CPU
	a = (int*)malloc(size);
	b = (int*)malloc(size);

	//Allocate memory GPU
	cudaMalloc((void**)&Da ,size);
	cudaMalloc((void**)&Db ,size);

	//Write Data in the CPU array 
	for (int i = 0 ; i < N ; i++)
	{
		a[i] = i;
		// printf("%d",a[i]); 													//DEBUG
	}

	//Copy from CPU to GPU 
	cudaMemcpy(Da,a,size,cudaMemcpyHostToDevice);

	//Work 
	square<<<1,N>>>(Da,Db);

	//Copy from GPU to CPU
	cudaMemcpy(b,Db,size,cudaMemcpyDeviceToHost);

	for(int i = 0 ; i < N ; i++)
	{
		printf("%d",b[i]);
		printf(" ");
		if (i % 4 == 0)
		{
			printf("\n");
		}
	}
	printf("\n");

	//Free Memory GPU
	cudaFree(Da);
	cudaFree(Db);

	//Free Memory CPU
	free(a);
	free(b);


	return 0 ; 

}

__global__ void square(int *a , int *b)
{
	int idx = threadIdx.x;
	b[idx] = a[idx] * a[idx];
}



int askInput()
{
	printf("\n");
	int input;
	printf ("Enter Number of Threads to be executed ");
    scanf ("%d", &input);
    printf ("No of threads = %d", input);
    printf("\n");
    return input;
}














