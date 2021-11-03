import java.util.*;
import java.io.*;

public class Main {
    public static int fc(int a, int b){
        if(a == 0)
            return b;
        if(b == 1)
            return 1;
        return fc(a - 1, b) + fc(a, b - 1);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int count = Integer.parseInt(br.readLine());
        int a, b, result;
        for(int i = 0; i < count; i++){
            a = Integer.parseInt(br.readLine());
            b = Integer.parseInt(br.readLine());
            result = fc(a, b);
            bw.write(result + "\n");
        }
        bw.flush();
    }
}
