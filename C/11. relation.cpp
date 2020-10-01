#include <stdio.h>

int main(void) {
	int x = 50, y = 30;
	printf("x와 y는 같은가? %d\n", x==y); // 1 : true, 0 : false
	printf("x와 y는 다른가? %d\n", x!=y); // 1 : true, 0 : false
	printf("x는 y보다 큰가? %d\n", x>y); // 1 : true, 0 : false
	printf("x는 y보다 작은가? %d\n", x<y); // 1 : true, 0 : false
	printf("x에 y값을 넣으면? %d\n", x=y); // 1 : true, 0 : false
	printf("x에 y값을 넣으면? %d\n", (x=y)); // 1 : true, 0 : false
	return 0;
	
}
