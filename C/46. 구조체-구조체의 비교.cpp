#include <stdio.h>

struct point {
	int x;
	int y;
	
};

void comparePoint(struct point p1, struct point p2) {
	if(p1.x == p2.x && p2.y == p2.y) {
		printf("p1과 p2는 같습니다. \n");
	}
}

int main(void) {
	
	struct point p1;
	struct point p2;
	
	p1.x = 30;
	p1.y = 10;
	
	p2.x = 30;
	p2.y = 10;
	
	/*
	구조체는 타입이 같더라도 그 자체로 비교할 수 없다.
	if(p1 == p2) {
		printf("p1과 p2는 같습니다. ");
	}
	*/
	if(p1.x == p2.x && p2.y == p2.y) {
		printf("p1과 p2는 같습니다. \n");
	}
	comparePoint(p1, p2);
	
	return 0;
}
