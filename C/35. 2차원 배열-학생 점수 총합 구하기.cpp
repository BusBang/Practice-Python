#include <stdio.h>

int main(void) {
	int score[5][2];
	int total[2] = {0, }; // 1차원 배열을 만들 때, 모든 값에 0을 넣어줌
	int i;
	
	for(i=0; i<5; i++) {
		printf("%d번 학생의 수학, 영어 점수 : ", i+1);
		scanf("%d %d", &score[i][0], &score[i][1]);
	} 
	
	for(i=0; i<5; i++) {
		total[0] += score[i][0];	//수학 합 
		total[1] += score[i][1];	//영어 합 
	}
	
	printf("\n\n5명의 수학 점수 합계 : %d\n", total[0]);
	printf("\n5명의 영어 점수 합계 : %d\n", total[1]);
	return 0;
	
}
