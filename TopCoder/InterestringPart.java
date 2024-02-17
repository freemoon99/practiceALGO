import java.util.*;

public class InterestingParty{
    public int bestInvitation(String[] first, String[] second){
    	HashMap<String, Integer> dic = new HashMap<>();
        
        for(int i=0; i<first.length; i++){
            if (!dic.containsKey(first[i])){
            	dic.put(first[i], 1);
            } else {
            	int count = dic.get(first[i]);
            	dic.put(first[i], count + 1);
            }
            if (!dic.containsKey(second[i])){
            	dic.put(second[i], 1);
            } else {
            	int count = dic.get(second[i]);
            	dic.put(second[i], count + 1);
            }
        }
        
       	int answer = 0;
        for (int val : dic.values()){
        	answer = Math.max(answer, val);
        }
        
        return answer;
    }
}