#include <stdio.h>

// *���� �����Ͱ� ����Ű�� �ִ� �� 

/*ex)
	int x = 70;
	int *y = &x;
	
	print(y) -> x�� �ּҰ� 
	print(*y) -> 70 

*/

// �� ������ ���� ���� ��ȯ�ϴ� ǥ���� �Լ� 
void swap(int *x, int *y) {
	int temp;
	temp = *x;	//x�� �⸮Ű�� ���� ������
	*x = *y;
	*y = temp; 
}

void swap2(int x, int y) {
	int temp;
	temp = x;	//x�� �⸮Ű�� ���� ������
	x = y;
	y = temp; 
}

int main(void) {
	int x=1;
	int y=2;
	printf("x = %d\ny = %d\n", x, y);
	printf("swap ����\n");
	swap(&x, &y);
	printf("x = %d\ny = %d\n", x, y);
	printf("swap2 ����\n");
	swap2(x, y);
	printf("x = %d\ny = %d\n", x, y);
	return 0;
	
		
}
