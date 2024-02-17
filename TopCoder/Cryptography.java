// 전체 탐색
public class Cryptography {
  public long encrypt(int[] numbers) {
    long min = Long.MAX_VALUE;
      
      long mul = 1;
      for (int n : numbers) {
        min = Math.min(min, n);
          mul *= n;
      }
      
      long ans = (mul / min) * (min+1);
      
      return ans;
  }
}

// 정렬 사용
import java.util.*;
public class Cryptography {
    public long encrypt(int[] numbers) {
        long mul = 1;
        Arrays.sort(numbers);
        numbers[0]++;
        
        for (int n : numbers) {
            mul *= n;
        }
        
        return mul;
    }
}