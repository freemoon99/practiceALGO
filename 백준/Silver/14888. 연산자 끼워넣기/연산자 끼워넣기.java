import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n, sum;
	static int[] a, op;
	static int max = -1000000000, min = 1000000000;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        n = Integer.parseInt(br.readLine());
        a = new int[n];
        st = new StringTokenizer(br.readLine());
        
        for (int i=0; i<n; i++) {
        	a[i] = Integer.parseInt(st.nextToken());
        }
        
        op = new int[4];
        st = new StringTokenizer(br.readLine());
        
        for (int i=0; i<4; i++) {
        	op[i] = Integer.parseInt(st.nextToken());
        }
        
        dfs(a[0], 1);
        System.out.printf("%d\n%d", max, min);
    }
    
    private static void dfs(int result, int idx) {    	
    	if (idx == n) {
    		max = Math.max(max, result);
    		min = Math.min(min, result);
    		return;
    	}
    	
    	for (int i=0; i<4; i++) {
    		if (op[i] > 0) {
    			
    			op[i]--;
    			
    			if (i == 0) {
    				dfs(result+a[idx], idx+1);
    			} else if (i == 1) {
    				dfs(result-a[idx], idx+1);
    			} else if (i == 2) {
    				dfs(result*a[idx], idx+1);
    			} else if (i == 3) {
    				dfs(result/a[idx], idx+1);
    			}
    			
    			op[i]++;
    		}
    	}
    }
}
