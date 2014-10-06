//
//  Add.cu
//  
//
//  Created by Sandeep on 10/1/14.
//
//

#include <stdio.h>

#define N 512


__global__ void add(int *a ,int *b , int *c)
{
    c[blockIdx.x] = a[blockIdx.x] + b[blockIdx.x] ;
}

int main(void)
{
int *a,*b,*c;
int *d_a,*d_b,*d_c;
int size = N * sizeof( int ) ; 

cudaMalloc( (void**)&d_a,size);
cudaMalloc( (void**)&d_b,size);
cudaMalloc( (void**)&d_c,size);

a = (int*)malloc( size );
b = (int*)malloc( size );
c = (int*)malloc( size );

for(int i = 0 ; i < N ; i++)
	{
		a[i] = rand();
	}



cudaMemcpy( d_a , a , size , cudaMemcpyHostToDevice);
cudaMemcpy( d_b , b , size , cudaMemcpyHostToDevice);

add<<<N,1>>>(d_a,d_b,d_c);

cudaMemcpy( c, d_c , size , cudaMemcpyDeviceToHost);

for(int i = 0 ;i < N ; i++)
{
printf("%d \n",c[i]);
}

free(a);
free(b);
free(c);

cudaFree( d_a );
cudaFree( d_b );
cudaFree( d_c );


return 0 ; 


}










