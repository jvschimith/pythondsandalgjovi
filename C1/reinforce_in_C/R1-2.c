#include <stdio.h>
#include <stdbool.h>

bool is_even(int n){

	if ((n & 1) == 0)
		return true;
	else 
		return false;

}


int main(){

	int n;

	printf("Insira um n: ");
	scanf("%d", &n);

	if (is_even(n))
		printf("Is even");
	else
		printf("Is odd");

	return 0;
}
