#include <stdio.h>

int main(void) {
	char input[1001];
	gets(input);	// enter�� ĥ�������� char�� input �ȿ� ��
	int count = 0;
	
	// input[count]�� NULL �� �ƴҶ� ����.
	// HELLO
	// 01234	--> index=5, NULL 
	while(input[count] != '\0') {
		count++;
	} 
	printf("�Է��� ���ڿ��� ���̴� %d�Դϴ�. \n", count);
	printf("�Է��� ���ڿ� : %s", input);
	return 0;
}
