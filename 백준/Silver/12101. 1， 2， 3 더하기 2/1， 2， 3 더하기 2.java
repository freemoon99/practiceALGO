import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	static int n, k;
	static ArrayList<String>[] dp;
	static int MAX_VALUE = 11;
	
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        
        dp = new ArrayList[MAX_VALUE+1];
        
        for (int i=0; i<MAX_VALUE+1; i++) {
        	dp[i] = new ArrayList<>();
        }
        
        dp[1].add("1");
        dp[2].add("1+1");
        dp[2].add("2");
        dp[3].add("1+1+1");
        dp[3].add("1+2");
        dp[3].add("2+1");
        dp[3].add("3");
        
        for(int i=4; i<n+1; i++) {
        	for (int j=0; j<=3; j++) {
        		for (String now : dp[i-j]) {
        			dp[i].add(now+"+"+j);
        		}
        	}
        }
        
        if (dp[n].size() < k) {
        	System.out.print(-1);
        } else {
        	Collections.sort(dp[n]);
        	System.out.print(dp[n].get(k-1));
        }
        
    }
    
   
}