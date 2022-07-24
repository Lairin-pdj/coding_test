import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 파싱
        String[] st = br.readLine().split(" ");
        int n = Integer.parseInt(st[0]);
        int m = Integer.parseInt(st[1]);

        // 배열 처리
        ArrayList<StringBuilder> now = new ArrayList<>();
        ArrayList<StringBuilder> target = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            now.add(new StringBuilder(br.readLine()));
        }
        for (int i = 0; i < n; i++) {
            target.add(new StringBuilder(br.readLine()));
        }

        // 3이하 초기 처리
        if (n < 3 || m < 3) {
            if (now.toString().equals(target.toString())) {
                System.out.println(0);
            }
            else {
                System.out.println(-1);
            }
            return;
        }

        // 그리디 변환
        int answer = 0;
        for (int i = 0; i < n - 2; i++) {
            for (int j = 0; j < m - 2; j++) {
                // 같지 않은 경우
                if (now.get(i).charAt(j) != target.get(i).charAt(j)) {
                    // 변환
                    for (int k = 0; k < 3; k++) {
                        for (int l = 0; l < 3; l++) {
                            if (now.get(i + k).charAt(j + l) == '1') {
                                now.get(i + k).setCharAt(j + l, '0');
                            }
                            else {
                                now.get(i + k).setCharAt(j + l, '1');
                            }
                        }
                    }
                    answer++;
                }
            }
            // 변경 불가 부분 일치 여부 판단
            if (now.get(i).charAt(m - 2) != target.get(i).charAt(m - 2) ||
                    now.get(i).charAt(m - 1) != target.get(i).charAt(m - 1)) {
                System.out.println(-1);
                return;
            }
        }
        // 변경 불가 부분 일치 여부 판단
        if (!now.get(n - 2).toString().equals(target.get(n - 2).toString()) ||
                !now.get(n - 1).toString().equals(target.get(n - 1).toString())) {
            System.out.println(-1);
            return;
        }

        // 결과 출력
        System.out.println(answer);
    }
}
