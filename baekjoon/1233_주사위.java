import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 파싱
        String[] st = br.readLine().split(" ");

        // 계산
        int[] check = new int[81];
        for (int i = 1; i <= Integer.parseInt(st[0]); i++) {
            for (int j = 1; j <= Integer.parseInt(st[1]); j++) {
                for (int k = 1; k <= Integer.parseInt(st[2]); k++) {
                    check[i + j + k] += 1;
                }
            }
        }

        // 빈도수 제일 높은 수 찾기
        int answer = 0;
        int high = 0;
        for (int i = 0; i < 81; i++) {
            if (check[i] > high) {
                high = check[i];
                answer = i;
            }
        }

        // 출력
        System.out.println(answer);
    }
}
