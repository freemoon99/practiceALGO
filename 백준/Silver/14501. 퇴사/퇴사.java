import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int[] t, p, dp;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        n = Integer.parseInt(br.readLine());
        t = new int[n+1];
        p = new int[n+1];
        dp = new int[n+2];
        
        for (int i=1; i<=n; i++) {
        	st = new StringTokenizer(br.readLine());
        	
        	t[i] = Integer.parseInt(st.nextToken());
        	p[i] = Integer.parseInt(st.nextToken());
        }
        
        for (int i=1; i<=n; i++) {
        	for (int j=i+t[i];j<=n+1; j++) {
        		dp[j] = Math.max(dp[j], dp[i]+p[i]);
        		
        	}
        }
        
        System.out.print(dp[n+1]);
    }

}