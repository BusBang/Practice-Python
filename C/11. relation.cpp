#include <stdio.h>

int main(void) {
	int x = 50, y = 30;
	printf("x�� y�� ������? %d\n", x==y); // 1 : true, 0 : false
	printf("x�� y�� �ٸ���? %d\n", x!=y); // 1 : true, 0 : false
	printf("x�� y���� ū��? %d\n", x>y); // 1 : true, 0 : false
	printf("x�� y���� ������? %d\n", x<y); // 1 : true, 0 : false
	printf("x�� y���� ������? %d\n", x=y); // 1 : true, 0 : false
	printf("x�� y���� ������? %d\n", (x=y)); // 1 : true, 0 : false
	return 0;
	
}
