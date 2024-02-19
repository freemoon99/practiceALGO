// 단순 구현
// 최초의 문자가 팰린드롬 문자이면 그대로 return
// 아니라면 처음 문자열 젤 뒤에 공백 추가해주고 시작
// 가장 뒤와 최초의 문자열 젤 뒷자리와 start인덱스를 비교해주기
// 같을때까지 -> 같다면 그 길이 -1 이 답
// 아니라면 start를 옮겨주고, 문자열에 공백 추가해주는 식으로 하기

public class ThePalindrome {
    public int find(String s) {
        int n = s.length();
        
        // 팰린드롬 확인
        boolean isPalindrome = true;
        for (int i = 0; i < n / 2; i++) {
            if (s.charAt(i) != s.charAt(n - i - 1)) {
                isPalindrome = false;
                break;
            }
        }
        
        if (isPalindrome) {
        	int ans = s.length();
            return ans;
        } else {
        	s += '0';
        	
        	int start = 0;
            int end = s.length() - 1;
            
            while (start < end) {
                if (s.charAt(start) != s.charAt(end)) {
                    start++;
                    s += '0';
                    end = n-1;
                } else {
                    break;
                }
            }
            
            int ans = s.length()-1;
            
           	return ans;
        }
    }
}


// 좀 더 간단한 답
import java.util.*;

public class ThePalindrome {
    public int find(String s) {
    	for (int i=s.length();;i++) {
    		boolean flag = true;
    		
    		for (int j=0; j<s.length(); j++) {
    			if ((i-j-1)<s.length() && s.charAt(j) != s.charAt(i-j-1)) {
    				flag = false;
    				break;
    			}
    		}
    		if (flag) return i;
    	}
    }
}