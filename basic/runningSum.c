
#include <stdio.h>
int* runningSum(int* nums, int* output, int len){
	/* Function will not allocate memory. The memory must be allocated and freed by the caller */
	int acc=0;
	for(int i=0; i< len; i++){
		acc += nums[i];
		output[i] = acc;
	}
	return output;	
}

void printArray(int* arr, int len){
	printf("[ ");
	for(int i=0; i<len-1; i++){
		printf("%d, ", arr[i]);
	}
	printf("%d ]\n", arr[len-1]);

}

int main(int argc, char** argv){

	int nums[10] = {1,4,6,2,9,5,8,3,7,-2};
	int output[10];
	int len=10;
	runningSum(nums, output, len);
	printf("input:\n");
	printArray(nums, len);
	printf("output:\n");
	printArray(output, len);
	return 0;
	
}
