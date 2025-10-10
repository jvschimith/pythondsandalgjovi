#include <stdio.h>
#include <stdbool.h>


bool is_multiple(int n, int m){

	if(n%m == 0)
	       	return true;
	else 
		return false;

}


int main(){

	int n, m;

	printf("Insira n m: ");
	scanf("%d %d", &n, &m);

	if (is_multiple(n, m))
		printf("\nTrue\n");
	else 
		printf("\nFalse\n");

	return 0;
}
