#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(long num) {
    int answer = 0;
    
    for( ; answer < 500; answer++){     // 500번 까지만 시도
        if(num == 1){                   // 목표에 도달하면 반복문 탈출
            break;
        }
        else if(num % 2){               // 홀수일 경우
            num *= 3;
            num += 1;
        }
        else{                           // 짝수일 경우
            num /= 2;
        }
    }
    
    if(answer == 500){                  // 500번을 초과하는 경우
        answer = -1;
    }
    
    return answer;
}
