import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
   public static void main(String[] args) throws IOException, NullPointerException {
      // 빠른 입출력을 위하여
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

      int N = Integer.parseInt(br.readLine());
      int count = 0;
      int sixCount = 0;
      int rise = 0; 
      int num = 666;
      int check = 0;
      int answer = 0;
      
      for(int i = 666; count < N; i++){
          num = i;
          sixCount = 0;
          while(true){
              check = num % 10;
              if(check == 6){
                  sixCount++;
              }
              else{
                  sixCount = 0;
              }
              if(sixCount >= 3){
                  answer = i;
                  count++; 
                  break;
              }
              num /= 10;
              if(num <= 0){
                  break;
              }
          }
      }
      bw.write(Integer.toString(answer));
      bw.flush();
      br.close();
   }
}
