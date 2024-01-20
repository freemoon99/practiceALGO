import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    static int n, d, k, c;
    static int[] list, checked;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        
        list = new int[n];
        checked = new int[d+1];
        
        for (int i = 0; i < n; i++) {
            list[i] = Integer.parseInt(br.readLine());
        }
        
        // 쿠폰을 사용했다고 가정
        int max = 1;
        checked[c]++;
        
        for (int i=0; i<k; i++) {
        	if (checked[list[i]] == 0) max++;
        	checked[list[i]]++;
        }
        
        int cnt = max;
        for (int i=1; i<n; i++) {
        	int pop = list[i-1];
        	checked[pop]--;
        	if (checked[pop] == 0) cnt--;
        	
        	int add = list[(i+k-1)%n];
        	if(checked[add] == 0) cnt++;
        	checked[add]++;
        	
        	max = Math.max(max, cnt);
        }
        
        
        
        System.out.println(max);
    }
}
