import java.util.*;
public class InterestingDigits{
    public int[] digits(int base){
    	ArrayList<Integer> list = new ArrayList<>();
        
        for (int n=2; n<base; n++){
            boolean flag = true;
        	outloop:
            for (int i=0; i<base; i++){
                for (int j=0; j<base; j++){
                    for (int k=0; k<base; k++){
                    	int nowNum = i+j*base+k*base*base;
                        
                        if ((nowNum % n == 0) && ((i+j+k)%n != 0)) {
                            flag = false;
                            break outloop;
                        }
                    }
                }
            }
            if (flag) list.add(n);
        }
        
        int[] ans = new int[list.size()];
        for (int i=0; i<list.size(); i++) ans[i] = list.get(i);
        
        return ans;
    }
}

// 수학적 요소를 이용한 답
// base - 1을 후보군 n으로 나누어 떨어진다면 조건에 맞는 답이 됨
// 증명은 topcoder 알고리즘 책 참고 p.108 ~ p.110
import java.util.*;
public class InterestingDigits{
    public int[] digits(int base){
    	ArrayList<Integer> list = new ArrayList<>();
        
        for (int i=2; i<base; i++) {
        	if((base-1) % i == 0) list.add(i);
        }
        
        int[] ans = new int[list.size()];
        for (int i=0; i<list.size(); i++) ans[i] = list.get(i);
        
        return ans;
    }
}