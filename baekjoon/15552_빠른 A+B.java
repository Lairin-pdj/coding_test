import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int caseNum = Integer.parseInt(sc.nextLine());
        String[] input = new String[2];
        int res = 0;
        for(int i = 0; i < caseNum; i++) {
            input[0] = sc.next();
            input[1] = sc.next();
            res = Integer.parseInt(input[0]) + Integer.parseInt(input[1]);
            bw.write(res + "\n");
        }
        bw.flush();
    }
}
