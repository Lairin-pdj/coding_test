import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] st = br.readLine().split(" ");
        int[] nums = Arrays.stream(st).mapToInt(Integer::parseInt).toArray();

        int now = nums[1];
        if (now + nums[3] > nums[2]) {
            System.out.println(-1);
            return;
        }

        int count = 0;
        int time = 0;
        while (count != nums[0]) {
            time += 1;
            if (now + nums[3] <= nums[2]) {
                now += nums[3];
                count += 1;
            }
            else {
                now = Math.max(now - nums[4], nums[1]);
            }
        }

        System.out.println(time);
    }
}
