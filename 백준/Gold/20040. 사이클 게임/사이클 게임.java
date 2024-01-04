import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n, m, ans = 0;
	static int[] parents;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        
        parents = new int[n];
        
        for (int i=0; i<n; i++) {
        	parents[i] = i;
        }
        
        for (int turn=1; turn<=m; turn++) {
        	st = new StringTokenizer(br.readLine());
        	int a = Integer.parseInt(st.nextToken());
        	int b = Integer.parseInt(st.nextToken());
        	
        	if (union(a, b)) {
        		ans = turn;
        		break;
        	}
        }
        System.out.print(ans);
    }
    
    private static boolean union(int x, int y) {
    	int xRoot = find(x);
    	int yRoot = find(y);
    	
    	if (xRoot == yRoot) return true;
    	parents[yRoot] = xRoot;
    	return false;
    	
    }
    
    private static int find(int x) {
    	if (x == parents[x]) return x;
    	return parents[x] = find(parents[x]);
    }

}