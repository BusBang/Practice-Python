#include <stdio.h>
#include <math.h>

int main(void)
{
	int x = -50, y=30;
	int absX = (x>0)?x:-1;		// ���׿����� 
	

	
	int max = (x>y) ? x : y;
	int min = (x<y) ? x : y;
	int absX2 = abs(x);
	double powXY = pow(x, y);	
	
	printf("x�� ������ %d �Դϴ�. \n", absX);
	printf("x�� ������ %d �Դϴ�. \n", absX2);
	printf("x�� y�� �ִ��� %d �Դϴ�. \n", max);
	printf("x�� y�� �ּڰ��� %d �Դϴ�. \n", min);
	printf("x�� y���� %.0f �Դϴ�. \n", powXY);
	 
	
	return 0;
}
