import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int n, m, ans = Integer.MAX_VALUE;
	static int[][] map;
	static ArrayList<Pair> chicken, house;
	static ArrayList<ArrayList<Pair>> candidates;
	static boolean[] visited;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        
        map = new int[n][n];
        for (int i=0; i<n; i++) {
        	st = new StringTokenizer(br.readLine());
        	for (int j=0; j<n; j++) {
        		map[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        
        // 전체 치킨집, 집 배열에 추가
        chicken = new ArrayList<>();
        house = new ArrayList<>();
        for (int i=0; i<n; i++) {
        	for (int j=0; j<n; j++) {
        		if (map[i][j] == 1) {
        			house.add(new Pair(i, j));
        		}
        		if (map[i][j] == 2) {
        			chicken.add(new Pair(i, j));
        		}
        	}
        }
   
        
        // 가능한 치킨 집 뽑기
        candidates = new ArrayList<>();
        visited = new boolean[chicken.size()];
        combination(0, m);
        
        int sum = Integer.MAX_VALUE;
        for(ArrayList<Pair> candidate : candidates) {
        	int chickenDistance = 0;
            for (Pair h : house) {
            	int temp = Integer.MAX_VALUE;
            	for (Pair c : candidate) {
            		int dm = Math.abs(h.x-c.x) + Math.abs(h.y-c.y);
            		
            		temp = Math.min(temp, dm);
            	}
            	chickenDistance += temp;
            }
            
            sum = Math.min(chickenDistance, sum);
        }
        
        System.out.print(sum);
    }
    
    private static void combination(int n, int r) {
    	if(r == 0) {
            ArrayList<Pair> candidate = new ArrayList<>();
            for(int i = 0; i < chicken.size(); i++) {
                if(visited[i]) {
                    candidate.add(chicken.get(i));
                }
            }
            candidates.add(candidate);
            return;
        } 

        for(int i=n; i<chicken.size(); i++) {
            visited[i] = true;
            combination(i + 1, r - 1);
            visited[i] = false;
        }
    }
    
    static class Pair {
    	int x, y;
    	public Pair(int x, int y) {
    		this.x = x;
    		this.y = y;
    	}
    }
}