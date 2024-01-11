import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int[] dp, numbers;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        n = Integer.parseInt(br.readLine());
        dp = new int[n+1];
        numbers = new int[n+1];
        
        st = new StringTokenizer(br.readLine());
        
        for (int i=0; i<n; i++) {
        	numbers[i] = Integer.parseInt(st.nextToken());
        }
        
        for (int i=0; i<n; i++) {
        	int mx = 0;
        	for (int j=0; j<i; j++) {
        		if (numbers[i] > numbers[j]) {
        			mx = Math.max(mx, dp[j]);
        		}
        	}
        	dp[i] = mx+1;
        }
        
        int max = 0;
        for (int i = 0; i < dp.length; i++) {
            if (dp[i] > max) {
                max = dp[i];
            }
        }
        System.out.println(max);

        

    }

}