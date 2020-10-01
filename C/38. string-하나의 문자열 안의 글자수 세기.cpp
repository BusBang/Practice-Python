#include <stdio.h>

int main(void) {
	char input[1001];
	gets(input);	// enter를 칠때까지의 char가 input 안에 들어감
	int count = 0;
	
	// input[count]가 NULL 이 아닐때 까지.
	// HELLO
	// 01234	--> index=5, NULL 
	while(input[count] != '\0') {
		count++;
	} 
	printf("입력한 문자열의 길이는 %d입니다. \n", count);
	printf("입력한 문자열 : %s", input);
	return 0;
}
