import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        final int NUM_MAX = 10001;
        int a = Integer.parseInt(br.readLine());
        int[] nums = new int[NUM_MAX];
        
        for(int i = 0; i < a; i++)
            nums[Integer.parseInt(br.readLine())]++;
        
        for(int i = 1; i < NUM_MAX; i++)
            sb.append((i+ "\n").repeat(nums[i]));
        System.out.println(sb.toString());
    }
}
