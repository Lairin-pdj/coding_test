import java.util.Arrays;

class Solution {
    public String[] solution(String[] strings, int n) {
        // 문자열 앞에 n번째 문자를 붙여 정렬
        for(int i = 0; i < strings.length; i++){
            strings[i] = strings[i].charAt(n) + strings[i];
        }
        
        Arrays.sort(strings);
        
        // 붙였던 n번째 문자를 제거 후 반환
        for(int i = 0; i < strings.length; i++){
            strings[i] = strings[i].substring(1, strings[i].length());
        }
        
        return strings;
    }
}
