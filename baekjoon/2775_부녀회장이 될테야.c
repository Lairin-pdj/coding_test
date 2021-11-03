#define _CRT_SECURE_NO_WARNINGS
#define MAX 15
#include<stdio.h>

int be_a_president() {
	int floor, num;
	int apart[MAX][MAX];
	scanf("%d %d", &floor, &num);
	for (int i = 0; i <= floor; i++)
	{
		for (int j = 0; j < num; j++)
		{
			if (i == 0) apart[i][j] = j+1;

			else
			{	
				int sum = 0;
				for (int k = 0; k <= j; k++)
				{
					sum += apart[i-1][k];
				}
				apart[i][j] = sum;
			}
		}
	}
	return apart[floor][num-1];
}

int main() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	{
		printf("%d\n", be_a_president());
	}
	return 0;
}
