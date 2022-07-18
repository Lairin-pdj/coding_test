import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 파싱
        String[] st = br.readLine().split(" ");

        // 계산
        long answer = 0;
        for (int i = 0; i < st[0].length(); i++) {
            for (int j = 0; j < st[1].length(); j++) {
                answer += (st[0].charAt(i) - '0') * (st[1].charAt(j) - '0');
            }
        }

        // 출력
        System.out.println(answer);
    }
}
