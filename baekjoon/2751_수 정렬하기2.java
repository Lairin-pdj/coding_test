import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int a = Integer.parseInt(br.readLine());
        
        ArrayList<Integer> nums = new ArrayList<>(a);
        for(int i = 0; i < a; i++){
            nums.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(nums);
        
        for(int n : nums)
            sb.append(n + "\n");
        System.out.println(sb.toString());
    }
}
