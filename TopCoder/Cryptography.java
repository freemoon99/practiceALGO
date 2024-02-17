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