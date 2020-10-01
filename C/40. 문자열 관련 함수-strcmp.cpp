#include <stdio.h>
#include <string.h>

int main(void) {
	char inputOne[5] = "A";
	char inputTwo[5] = "C";
	
	printf("문자열 비교 : %d\n", strcmp(inputOne, inputTwo));
	
	// 사전적으로 같으면 0
	// 먼저 나온 것이 작다면 -
	// 먼저 큰 것이 크다면 +
	
	return 0;
}
