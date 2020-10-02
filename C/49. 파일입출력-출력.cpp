#include <stdio.h>

int main(void) {
	
	FILE *fp = NULL;
	int c;
	
	fp = fopen("input.txt", "r");
	
	if(fp == NULL) {
		printf("파일 열기에 실패했습니다. \n");
	}else {
		printf("파일 열기에 성공했습니다. \n");
	}
	while((c = fgetc(fp)) != EOF) {
		// 파일의 char가 끝이 아니라면 반복
		putchar(c);	//출력 
	}
	fclose(fp);
	return 0;
}
