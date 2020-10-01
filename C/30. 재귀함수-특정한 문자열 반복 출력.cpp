#include <stdio.h>


// 재귀 함수 (Recursive Function) 
// 어떠한 것을 반복하는 것을 수행하되, 자기 자신을 포함하는 것.
 
void print(int count) {	
	if(count == 0) {
		return;
	}else {
		printf("문자열을 출력합니다. \n");
		print(count-1);	// 자기 자신을 한 번 더 수행한다. 
	}
}

int main(void) {
	int count;
	printf("몇 번 수행할 것입니까? : ");
	scanf("%d", &count);
	print(count);
	return 0;
}
