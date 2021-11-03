#include <iostream>
#include <algorithm>

using namespace std;

int N;
int board[20][20] = {0};
int answer = 0;

void move(int d){
    int check[20][20] = {0};
    
    if(d == 0){
        for(int i = 1; i < N; i++){
            for(int j = 0; j < N; j++){
                if(board[i][j] == 0){
                    continue;
                }
                int r = i;
                int c = j;
                while(1){
                    int nr = r - 1;
                    if(nr < 0){
                        break;
                    }
                    if(board[nr][c] == 0){
                        board[nr][c] = board[r][c];
                        board[r][c] = 0;
                    }
                    else{
                        if (board[nr][c] == board[r][c] && check[nr][c] == 0){
                            board[nr][c] = board[r][c] * 2;
                            board[r][c] = 0;
                            check[nr][c] = 1;
                        }
                        break;
                    }
                    r = nr;
                }
            }
        }
    }
    else if(d == 1){
        for(int i = N - 2; i > -1; i--){
            for(int j = 0; j < N; j++){
                if(board[i][j] == 0){
                    continue;
                }
                int r = i;
                int c = j;
                while(1){
                    int nr = r + 1;
                    if(nr >= N){
                        break;
                    }
                    if(board[nr][c] == 0){
                        board[nr][c] = board[r][c];
                        board[r][c] = 0;
                    }
                    else{
                        if (board[nr][c] == board[r][c] && check[nr][c] == 0){
                            board[nr][c] = board[r][c] * 2;
                            board[r][c] = 0;
                            check[nr][c] = 1;
                        }
                        break;
                    }
                    r = nr;
                }
            }
        }
    }
    else if(d == 2){
        for(int i = 0; i < N; i++){
            for(int j = 1; j < N; j++){
                if(board[i][j] == 0){
                    continue;
                }
                int r = i;
                int c = j;
                while(1){
                    int nc = c - 1;
                    if(nc < 0){
                        break;
                    }
                    if(board[r][nc] == 0){
                        board[r][nc] = board[r][c];
                        board[r][c] = 0;
                    }
                    else{
                        if (board[r][nc] == board[r][c] && check[r][nc] == 0){
                            board[r][nc] = board[r][c] * 2;
                            board[r][c] = 0;
                            check[r][nc] = 1;
                        }
                        break;
                    }
                    c = nc;
                }
            }
        }
    }
    else if(d == 3){
        for(int i = 0; i < N; i++){
            for(int j = N - 2; j > -1; j--){
                if(board[i][j] == 0){
                    continue;
                }
                int r = i;
                int c = j;
                while(1){
                    int nc = c + 1;
                    if(nc >= N){
                        break;
                    }
                    if(board[r][nc] == 0){
                        board[r][nc] = board[r][c];
                        board[r][c] = 0;
                    }
                    else{
                        if (board[r][nc] == board[r][c] && check[r][nc] == 0){
                            board[r][nc] = board[r][c] * 2;
                            board[r][c] = 0;
                            check[r][nc] = 1;
                        }
                        break;
                    }
                    c = nc;
                }
            }
        }
    }
}

void solution(int count){ 
    
    if (count == 5){
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                answer = max(answer, board[i][j]);
            }
        }
        return;
    }
    
    for(int d = 0; d < 4; d++){
        int temp[20][20] = {0};

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                temp[i][j] = board[i][j];
            }
        }
        
        move(d);
        solution(count + 1);
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                board[i][j] = temp[i][j];
            }
        }
    }
}

int main() {
   cin.tie(0); 
   cout.tie(0);
   ios::sync_with_stdio(0);

   cin >> N;
   for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
         cin >> board[i][j];
      }
   }

   solution(0);
   cout << answer;

   return 0;
}
