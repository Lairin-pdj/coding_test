import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 파싱
        int n = Integer.parseInt(br.readLine());
        int[] check = new int[26];

        // 글자 체크
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            check[(int)s.charAt(0) - 97] += 1;
        }

        // 가능한 글자 출력
        boolean flag = true;
        for (int i = 0; i < 26; i++) {
            if (check[i] >= 5) {
                System.out.print((char)(i + 97));
                flag = false;
            }
        }

        // 예외처리
        if (flag) {
            System.out.println("PREDAJA");
        }
    }
}
