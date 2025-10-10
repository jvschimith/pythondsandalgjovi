#include <stdio.h>

typedef struct{

	float min;
	float max;
} MinMax;

MinMax minmax(float data[], int n){

	MinMax result;
	result.min = data[0];
	result.max = data[0];

	for (int i = 1; i < n; i++){
		if(data[i] > result.max){
			result.max = data[i];
		}
		if(data[i] < result.min){

			result.min = data[i];
		}

	}

	return result;
}

int main() {
    float numbers[] = {1, 2, 3};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    
    MinMax result = minmax(numbers, size);
    
    printf("(%.2f, %.2f)\n", result.min, result.max);
    
    return 0;
}
