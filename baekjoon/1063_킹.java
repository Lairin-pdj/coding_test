import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 파싱
        String[] st = br.readLine().split(" ");
        int n = Integer.parseInt(st[2]);

        // 체스판 설정
        char kingX = st[0].charAt(0);
        char kingY = st[0].charAt(1);
        char stoneX = st[1].charAt(0);
        char stoneY = st[1].charAt(1);

        // 명령어 처리
        for (int i = 0; i < n; i++) {
            String op = br.readLine();
            char temp;
            // 분기
            switch (op) {
                case "R":
                    temp = (char)Math.min((int)kingX + 1, 'H');
                    // 돌 체크
                    if (temp == stoneX && kingY == stoneY) {
                        // 돌이 이동 할 수 있는 경우
                        if (stoneX != 'H') {
                            kingX = temp;
                            stoneX = (char)((int)temp + 1);
                        }
                    }
                    // 상관없이 이동
                    else {
                        kingX = temp;
                    }
                    break;
                case "L":
                    temp = (char)Math.max((int)kingX - 1, 'A');
                    // 돌 체크
                    if (temp == stoneX && kingY == stoneY) {
                        // 돌이 이동 할 수 있는 경우
                        if (stoneX != 'A') {
                            kingX = temp;
                            stoneX = (char)((int)temp - 1);
                        }
                    }
                    // 상관없이 이동
                    else {
                        kingX = temp;
                    }
                    break;
                case "B":
                    temp = (char)Math.max((int)kingY - 1, '1');
                    // 돌 체크
                    if (temp == stoneY && kingX == stoneX) {
                        // 돌이 이동 할 수 있는 경우
                        if (stoneY != '1') {
                            kingY = temp;
                            stoneY = (char)((int)temp - 1);
                        }
                    }
                    // 상관없이 이동
                    else {
                        kingY = temp;
                    }
                    break;
                case "T":
                    temp = (char)Math.min((int)kingY + 1, '8');
                    // 돌 체크
                    if (temp == stoneY && kingX == stoneX) {
                        // 돌이 이동 할 수 있는 경우
                        if (stoneY != '8') {
                            kingY = temp;
                            stoneY = (char)((int)temp + 1);
                        }
                    }
                    // 상관없이 이동
                    else {
                        kingY = temp;
                    }
                    break;
                case "RT":
                    if (kingX != 'H' && kingY != '8') {
                        kingX = (char)((int)kingX + 1);
                        kingY = (char)((int)kingY + 1);
                        // 돌 체크
                        if (kingX == stoneX && kingY == stoneY) {
                            // 돌이 이동 할 수 있는 경우
                            if (stoneX != 'H' && stoneY != '8') {
                                stoneX = (char)((int)stoneX + 1);
                                stoneY = (char)((int)stoneY + 1);
                            }
                            // 돌이 이동 할 수 없는 경우
                            else {
                                // 원복
                                kingX = (char)((int)kingX - 1);
                                kingY = (char)((int)kingY - 1);
                            }
                        }
                    }
                    break;
                case "LT":
                    if (kingX != 'A' && kingY != '8') {
                        kingX = (char)((int)kingX - 1);
                        kingY = (char)((int)kingY + 1);
                        // 돌 체크
                        if (kingX == stoneX && kingY == stoneY) {
                            // 돌이 이동 할 수 있는 경우
                            if (stoneX != 'A' && stoneY != '8') {
                                stoneX = (char)((int)stoneX - 1);
                                stoneY = (char)((int)stoneY + 1);
                            }
                            // 돌이 이동 할 수 없는 경우
                            else {
                                // 원복
                                kingX = (char)((int)kingX + 1);
                                kingY = (char)((int)kingY - 1);
                            }
                        }
                    }
                    break;
                case "RB":
                    if (kingX != 'H' && kingY != '1') {
                        kingX = (char)((int)kingX + 1);
                        kingY = (char)((int)kingY - 1);
                        // 돌 체크
                        if (kingX == stoneX && kingY == stoneY) {
                            // 돌이 이동 할 수 있는 경우
                            if (stoneX != 'H' && stoneY != '1') {
                                stoneX = (char)((int)stoneX + 1);
                                stoneY = (char)((int)stoneY - 1);
                            }
                            // 돌이 이동 할 수 없는 경우
                            else {
                                // 원복
                                kingX = (char)((int)kingX - 1);
                                kingY = (char)((int)kingY + 1);
                            }
                        }
                    }
                    break;
                case "LB":
                    if (kingX != 'A' && kingY != '1') {
                        kingX = (char)((int)kingX - 1);
                        kingY = (char)((int)kingY - 1);
                        // 돌 체크
                        if (kingX == stoneX && kingY == stoneY) {
                            // 돌이 이동 할 수 있는 경우
                            if (stoneX != 'A' && stoneY != '1') {
                                stoneX = (char)((int)stoneX - 1);
                                stoneY = (char)((int)stoneY - 1);
                            }
                            // 돌이 이동 할 수 없는 경우
                            else {
                                // 원복
                                kingX = (char)((int)kingX + 1);
                                kingY = (char)((int)kingY + 1);
                            }
                        }
                    }
                    break;
            }
        }

        // 결과출력
        System.out.printf("%c%c\n", kingX, kingY);
        System.out.printf("%c%c", stoneX, stoneY);
    }
}
