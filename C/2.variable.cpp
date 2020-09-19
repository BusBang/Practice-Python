#include <stdio.h>

int main(void)
{
	int x;
	x=5;
	printf("%d", x);  // %d <- int 정수가 들어간다 
	printf("변수 x의 메모리 크기는 %d입니다. ", sizeof(x));  // sizeof <- byte 크기를 표현 
	return 0;
	
}
