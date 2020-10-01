#include <stdio.h>

// 특정한 금액을 받아서 가장 적은 거스름 화폐의 개수를 구하는 함수.
int smallest(int number) {
	int count = 0;
	
	// 50000원 
	while(number >= 50000) {
		number -= 50000;
		count++;
	}
	// 10000원 
	while(number >= 10000) {
		number -= 10000;
		count++;
	}
	// 5000원 
	while(number >= 5000) {
		number -= 5000;
		count++;
	}
	// 1000원 
	while(number >= 1000) {
		number -= 1000;
		count++;
	}
	// 500원 
	while(number >= 500) {
		number -= 500;
		count++;
	}
	// 100원 
	while(number >= 100) {
		number -= 100;
		count++;
	}
	// 10원 
	while(number >= 10) {
		number -= 10;
		count++;
	}
	return count;
} 

int main(void) {
	int money;
	printf("금액을 입력하세요 : ");
	scanf("%d", &money);
	printf("최소로 나올 수 있는 화폐의 갯수는 %d개입니다.", smallest(money));
	return 0;
}
