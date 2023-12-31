import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static int[] result;
    static ArrayList<Integer>[] list;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        result = new int[n+1];
        list = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++) {
            list[i] = new ArrayList<>();
        }
        
        st = new StringTokenizer(br.readLine());
        for (int i=1; i<n+1; i++) {	// 1부터 시작한 인덱스가 현재 직원 번호, 값은 상사 번호
        	int num = Integer.parseInt(st.nextToken());
        	
        	if (num != -1) {
        		list[num].add(i);	// 반대호 num의 부하는 i
        	}
        }
        
        for (int i=0; i<m; i++) {
        	st = new StringTokenizer(br.readLine());
        	int idx = Integer.parseInt(st.nextToken());
        	int w = Integer.parseInt(st.nextToken());
        	
        	result[idx] += w;
        }
        dfs(1);
        
        for (int i=1; i<=n; i++) {
        	System.out.print(result[i]+" ");
        }

    }
    
    private static void dfs(int node) {    	
    	for (int next : list[node]) {
    		result[next] += result[node];
    		dfs(next);
    	}
    }
}
