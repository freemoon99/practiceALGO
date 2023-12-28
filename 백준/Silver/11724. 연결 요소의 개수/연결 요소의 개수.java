import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.StringTokenizer;


public class Main {
	static int n, m;
	static ArrayList<ArrayList<Integer>> graph;
	static HashSet<Integer> visited;
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		graph = new ArrayList<>();
		
		for (int i=0; i<n+1; i++) {
			graph.add(new ArrayList<>());
		}
		
		for (int j=0; j<m; j++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken());
			graph.get(a).add(b);
			graph.get(b).add(a);
		}
		int cnt = 0;
		visited = new HashSet<>();
		for (int k=1; k<n+1; k++) {
			if (!visited.contains(k)) {
				dfs(k);
				cnt += 1;
			}
		}
		
		System.out.print(cnt);
	}
	
	private static void dfs(int node) {
		visited.add(node);
		
		for (int next : graph.get(node)) {
			if (!visited.contains(next)) {
				dfs(next);
			}
		}
		
	}
}
