#include <stdio.h>


// ��� �Լ� (Recursive Function) 
// ��� ���� �ݺ��ϴ� ���� �����ϵ�, �ڱ� �ڽ��� �����ϴ� ��.
 
void print(int count) {	
	if(count == 0) {
		return;
	}else {
		printf("���ڿ��� ����մϴ�. \n");
		print(count-1);	// �ڱ� �ڽ��� �� �� �� �����Ѵ�. 
	}
}

int main(void) {
	int count;
	printf("�� �� ������ ���Դϱ�? : ");
	scanf("%d", &count);
	print(count);
	return 0;
}
