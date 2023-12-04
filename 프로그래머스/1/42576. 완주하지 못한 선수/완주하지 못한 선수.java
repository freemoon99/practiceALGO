import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> dic = new HashMap<>();
        
        for (String i : participant) {
            dic.put(i, dic.getOrDefault(i, 0)+1);
        }
        
        for (String j : completion) {
            dic.put(j, dic.get(j) - 1);
        }
        
        for (String key : dic.keySet()) {
            if (dic.get(key) != 0){
                answer = key;
            }
        }
        
        return answer;
    }
}