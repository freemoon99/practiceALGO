import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;


public class Main {
	static int n;
    static long ans = 0;
	static ArrayList<ArrayList<Integer>> graph;
    
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		n = Integer.parseInt(br.readLine());
		graph = new ArrayList<>();
		
		for (int i=0; i<=n ; i++) {
			graph.add(new ArrayList<>());
		}
		
		for (int i=1; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			
			graph.get(a).add(b);
			graph.get(b).add(a);
		}
		
		dfs(1, 0, 0);
		System.out.print((ans % 2 == 0) ? "No" : "Yes");
	}
	
	private static void dfs(int node, int parent, int cnt) {		
//		종료 조건
		if (graph.get(node).size() == 1 && node != 1) {
		    ans += cnt;
		}

		
		for (int next : graph.get(node)) {
			if (next != parent) {
				dfs(next, node, cnt+1);
			}
		}
	}

}
