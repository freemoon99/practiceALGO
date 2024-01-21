import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int t, n;
    static long[] list;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        t = Integer.parseInt(br.readLine());
        
        for (int i=0; i<t; i++) {
        	n = Integer.parseInt(br.readLine());
        	list = new long[n];
        	st = new StringTokenizer(br.readLine());
        	long cnt = 0, max = 0;
        	
        	for (int j=0; j<n; j++) {
        		list[j] = Long.parseLong(st.nextToken());
        	}
        	
        	// 계산
        	max = list[n-1];
        	for (int k=n-2; k>=0; k--) {
        		if (list[k] < max) {
        			cnt += max-list[k];
        		} else {
        			max = Math.max(max, list[k]);
        		}
        	}
        	
        	System.out.println(cnt);
        }
        
    }
}
