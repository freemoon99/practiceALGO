import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int n, total = 0;
	static int[][] s;
	static int[] numbers;
	static ArrayList<ArrayList<Integer>> starts;
	static boolean[] visited;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        n = Integer.parseInt(br.readLine());
        s = new int[n+1][n+1];
        
        for (int i =1; i<n+1; i++) {
        	st = new StringTokenizer(br.readLine());
        	for (int j=1; j<n+1; j++) {
        		s[i][j] = Integer.parseInt(st.nextToken());
        		
        		total += s[i][j];
        	}
        }
        
        numbers = new int[n];
        for (int i =0; i<n; i++) {
        	numbers[i] = i+1;
        }
        
        visited = new boolean[n+1];
        starts = new ArrayList<>();
        combination(0, 0, n / 2);
        
        int ans = total;
        for (ArrayList<Integer> start : starts) {
        	int teamStart = 0;
            int teamLink = 0;
        	
        	for (int num1 : start) {
        		for (int num2 : start) {
        			teamStart += s[num1][num2];
        		}
        	}
        	
            ArrayList<Integer> link = new ArrayList<>();
            for (int i = 1; i <= n; i++) {
                if (!start.contains(i)) {
                    link.add(i);
                }
            }

            for (int num1 : link) {
                for (int num2 : link) {
                    teamLink += s[num1][num2];
                }
            }
        	int diff = Math.abs(teamStart - teamLink);
        	
        	if (diff < ans) {
        		ans = Math.min(diff, ans);
        	}
        }
        
        System.out.print(ans);
    }
    
    private static void combination(int depth, int start, int r) {
        if (r == 0) {
            ArrayList<Integer> team = new ArrayList<>();
            for (int i=0; i<n+1; i++) {
            	if (visited[i]) team.add(numbers[i]);
            }
            
            starts.add(team);
            return;
        }

        for (int i = start; i < n; i++) {
            visited[i] = true;
            combination(depth + 1, i + 1, r - 1);
            visited[i] = false;
        }
    }

}