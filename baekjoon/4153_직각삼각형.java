import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int n1, n2, n3;
        double a, b, c;
        while(!str.equals("0 0 0")){
            st = new StringTokenizer(str);
            n1 = Integer.parseInt(st.nextToken());
            n2 = Integer.parseInt(st.nextToken());
            n3 = Integer.parseInt(st.nextToken());
            a = Math.pow(n1, 2);
            b = Math.pow(n2, 2);
            c = Math.pow(n3, 2);
            if(a + b == c || a + c == b || b + c == a){
                sb.append("right");
                sb.append("\n");
            }
            else{
                sb.append("wrong");
                sb.append("\n");
            }
            str = br.readLine();
        }
        System.out.println(sb.toString());
    }
}
