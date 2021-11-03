import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        // 입력 최적화
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        int[] b = new int[3];
        int[] c = new int[3];
        
        // 초기값 세팅
        String[] st = br.readLine().split(" ");
        for(int j = 0; j < 3; j++){
            c[j] = Integer.parseInt(st[j]);
        }
        
        // 동적계획법 실행
        for(int i = 0; i < a - 1; i++){
            int[] temp = new int[3];
            
            st = br.readLine().split(" ");
            for(int j = 0; j < 3; j++){
                b[j] = Integer.parseInt(st[j]);
            }
            
            temp[0] = Math.min(b[0] + c[1], b[0] + c[2]);
            temp[1] = Math.min(b[1] + c[0], b[1] + c[2]);
            temp[2] = Math.min(b[2] + c[0], b[2] + c[1]); 
            c[0] = temp[0];
            c[1] = temp[1];
            c[2] = temp[2];
        }
        System.out.println(Math.min(c[0], Math.min(c[1], c[2])));
    }
}
