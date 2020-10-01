#include <stdio.h>

// *값은 포인터가 가리키고 있는 값 

/*ex)
	int x = 70;
	int *y = &x;
	
	print(y) -> x의 주소값 
	print(*y) -> 70 

*/

// 두 변수의 값을 서로 변환하는 표인터 함수 
void swap(int *x, int *y) {
	int temp;
	temp = *x;	//x가 기리키는 값을 가져옴
	*x = *y;
	*y = temp; 
}

void swap2(int x, int y) {
	int temp;
	temp = x;	//x가 기리키는 값을 가져옴
	x = y;
	y = temp; 
}

int main(void) {
	int x=1;
	int y=2;
	printf("x = %d\ny = %d\n", x, y);
	printf("swap 실행\n");
	swap(&x, &y);
	printf("x = %d\ny = %d\n", x, y);
	printf("swap2 실행\n");
	swap2(x, y);
	printf("x = %d\ny = %d\n", x, y);
	return 0;
	
		
}
