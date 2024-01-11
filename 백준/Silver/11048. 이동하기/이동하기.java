import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static int[][] miro;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        miro = new int[n+1][m+1];
        
        for (int i=1; i<n+1; i++) {
        	st = new StringTokenizer(br.readLine());        	
        	for (int j=1; j<m+1; j++) {
        		miro[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        
        for (int i=1; i<n+1; i++) {    	
        	for (int j=1; j<m+1; j++) {
        		int max = Math.max(miro[i-1][j], Math.max(miro[i][j-1], miro[i-1][j-1]));
        		
        		miro[i][j] += max;
        	}
        }
        
        System.out.print(miro[n][m]);
    }

}