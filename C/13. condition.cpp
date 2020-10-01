#include <stdio.h>
#include <math.h>

int main(void)
{
	int x = -50, y=30;
	int absX = (x>0)?x:-1;		// 삼항연산자 
	

	
	int max = (x>y) ? x : y;
	int min = (x<y) ? x : y;
	int absX2 = abs(x);
	double powXY = pow(x, y);	
	
	printf("x의 절댓값은 %d 입니다. \n", absX);
	printf("x의 절댓값은 %d 입니다. \n", absX2);
	printf("x와 y중 최댓값은 %d 입니다. \n", max);
	printf("x와 y중 최솟값은 %d 입니다. \n", min);
	printf("x의 y승은 %.0f 입니다. \n", powXY);
	 
	
	return 0;
}
