#include <stdio.h>

// Ư���� �ݾ��� �޾Ƽ� ���� ���� �Ž��� ȭ���� ������ ���ϴ� �Լ�.
int smallest(int number) {
	int count = 0;
	
	// 50000�� 
	while(number >= 50000) {
		number -= 50000;
		count++;
	}
	// 10000�� 
	while(number >= 10000) {
		number -= 10000;
		count++;
	}
	// 5000�� 
	while(number >= 5000) {
		number -= 5000;
		count++;
	}
	// 1000�� 
	while(number >= 1000) {
		number -= 1000;
		count++;
	}
	// 500�� 
	while(number >= 500) {
		number -= 500;
		count++;
	}
	// 100�� 
	while(number >= 100) {
		number -= 100;
		count++;
	}
	// 10�� 
	while(number >= 10) {
		number -= 10;
		count++;
	}
	return count;
} 

int main(void) {
	int money;
	printf("�ݾ��� �Է��ϼ��� : ");
	scanf("%d", &money);
	printf("�ּҷ� ���� �� �ִ� ȭ���� ������ %d���Դϴ�.", smallest(money));
	return 0;
}
