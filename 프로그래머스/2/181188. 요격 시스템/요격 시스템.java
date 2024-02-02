import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        
        Arrays.sort(targets, (o1, o2) -> {return o1[1]-o2[1];});    // 탈출 기준으로 정렬
        
        int temp = targets[0][1];
        answer++;
        
        for (int[] now : targets){
            int in = now[0];
            int out = now[1];
            
            if (temp <= in){
                temp = out;
                answer++;
            }
        }
        
        return answer;
    }
}