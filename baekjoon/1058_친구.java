import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 파싱
        int n = Integer.parseInt(br.readLine());
        ArrayList<String> st = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st.add(br.readLine());
        }

        // 각 친구수 계산
        int[] check = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (st.get(i).charAt(j) == 'Y') {
                    check[i]++;
                    check[j]++;
                }
                else {
                    for (int k = 0; k < n; k++) {
                        if (st.get(i).charAt(k) == 'Y' && st.get(j).charAt(k) == 'Y') {
                            check[i]++;
                            check[j]++;
                            break;
                        }
                    }
                }
            }
        }

        // 출력
        System.out.println(Arrays.stream(check).max().getAsInt());
    }
}
