#include <stdio.h>
#include <limits.h>
#define NUMBER 5

int main(void) {
	int i, max, min, index;
	// array[0] ~ array[4] : �� 5���� ��� �� �� �ִ� ũ���� �迭 ���� 
	int array[NUMBER];	// �迭 ���� 
	max = 0;
	index = 0;
	
	
	for(i=0; i<NUMBER; i++) {
		printf("���� �Է����ּ��� : ");
		scanf("%d", &array[i]);
		
		// �ִ� ���� 
		if(max < array[i]) {
			max = array[i];
			index = i;
		}
	}
	printf("���� ū ���� %d�Դϴ�. \n�׸��� %d��°�� �ֽ��ϴ�.\n", max, index+1);

	min = INT_MAX;
	for(i=0; i<NUMBER; i++) {
		printf("���� �Է����ּ��� : ");
		scanf("%d", &array[i]);
		
		// �ִ� ���� 
		if(min > array[i]) {
			min = array[i];
			index = i;
		}
	}	
	printf("���� ���� ���� %d�Դϴ�. \n�׸��� %d��°�� �ֽ��ϴ�.\n", min, index+1);
	
	
	return 0;
	
	
	
}
 
