#include <stdio.h>

int main(void) {
//	윤년 : 4년 마다 +1, 그렇지만 100년 단위 일때는 +0.
//			400년 단위 일 때는 어떠한 상황이든간 윤년으로 설정
	int year = 2016;
	if((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
		printf("%d년은 윤년입니다. \n", year);
	}else {
		printf("%d년은 윤년이 아닙니다. \n", year);
	}
}
