import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static int[] arr;
	static boolean[] visited;
	static int[][] map;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        
        map = new int[n+1][n+1];
        
        for (int i=1; i<n+1; i++) {
        	for (int j=1; j<n+1; j++) {
            	map[i][j] = 101;
            }
        }
        
        for (int i=0; i<m; i++) {
        	st = new StringTokenizer(br.readLine());
        	
        	int a = Integer.parseInt(st.nextToken());
        	int b = Integer.parseInt(st.nextToken());
        	
        	map[a][b] = 1;
        	map[b][a] = 1;
        }
        
        for (int k=1; k<n+1; k++) {
        	for (int i=1; i<n+1; i++) {
        		if (i == k) continue;
        		for (int j=1; j<n+1; j++) {
        			if (i==k||j==k) continue;
        			
        			map[i][j] = Math.min(map[i][j], map[i][k] + map[k][j]);
        		}
        	}
        }
        
        int min = Integer.MAX_VALUE;
        int ans1=0, ans2=0;
        
        for (int i=1; i<n+1; i++) {
        	for (int j=1; j<n+1; j++) {
        		if (i == j) continue;
        		
        		int now = sum(i, j);
        		
        		if (min > now) {
        			ans1 = i;
        			ans2 = j;
        			min = now;
        		}
        	}
        }
        System.out.print(ans1+" "+ans2+" "+min*2);

    }
     
    private static int sum(int x, int y) {
    	int temp = 0;
    	for(int i=1; i<n+1; i++) {
    		if(i == x || i == y) continue;
    		
    		temp += Math.min(map[x][i], map[y][i]);
    	}
    	
    	return temp;
    }
    
   
}