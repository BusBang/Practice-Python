#include <stdio.h>
#include <limits.h>
#define NUMBER 5

int main(void) {
	int i, max, min, index;
	// array[0] ~ array[4] : 총 5개가 들어 갈 수 있는 크기의 배열 선언 
	int array[NUMBER];	// 배열 생성 
	max = 0;
	index = 0;
	
	
	for(i=0; i<NUMBER; i++) {
		printf("값을 입력해주세요 : ");
		scanf("%d", &array[i]);
		
		// 최댓값 갱신 
		if(max < array[i]) {
			max = array[i];
			index = i;
		}
	}
	printf("가장 큰 값은 %d입니다. \n그리고 %d번째에 있습니다.\n", max, index+1);

	min = INT_MAX;
	for(i=0; i<NUMBER; i++) {
		printf("값을 입력해주세요 : ");
		scanf("%d", &array[i]);
		
		// 최댓값 갱신 
		if(min > array[i]) {
			min = array[i];
			index = i;
		}
	}	
	printf("가장 작은 값은 %d입니다. \n그리고 %d번째에 있습니다.\n", min, index+1);
	
	
	return 0;
	
	
	
}
 
