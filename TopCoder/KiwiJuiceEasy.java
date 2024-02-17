public class KiwiJuiceEasy {
  public int[] thePouring(int[] capacities, int[] bottles, int[] fromId, int[] toId) {
      int n = fromId.length;
      for (int i=0; i<n; i++) {
          int f = fromId[i];
          int t = toId[i];
          int diff = Math.min(bottles[f], capacities[t]-bottles[t]);
          
          bottles[f] -= diff;
          bottles[t] += diff;
      }
      
      return bottles;
  }
}