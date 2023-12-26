import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Objects;
import java.util.Queue;
import java.util.HashSet;
import java.util.StringTokenizer;

class Pair {
	int x, y, cnt;
	
	public Pair(int x, int y, int cnt) {
		this.x = x;
		this.y = y;
		this.cnt = cnt;
	}
	
	@Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Pair pair = (Pair) o;
        return x == pair.x && y == pair.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
}

public class Main {
	static int a, b, c, d;
	static Queue<Pair> q;
	static HashSet<Pair> visited;
	
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		a = Integer.parseInt(st.nextToken());
		b = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());	
		
		bfs(c, d);
	}
	
	private static void bfs(int c, int d) {
		q = new LinkedList<>();
		visited = new HashSet<>();
		q.add(new Pair(0, 0, 0));
		visited.add(new Pair(0, 0, 0));
		
		while (!q.isEmpty()) {
			Pair now = q.poll();
			
			
			if (now.x==c && now.y==d) {
				System.out.println(now.cnt);
				return;
			}
			
//			Fill 2개
			if (now.x < a) {
				Pair p = new Pair(a, now.y, now.cnt+1);
				
				if (!visited.contains(p)) {
					visited.add(p);
					q.add(p);
				}	
			}
			
			if (now.y < b) {
				Pair p = new Pair(now.x, b, now.cnt+1);
				
				if (!visited.contains(p)) {
					visited.add(p);
					q.add(p);
				}	
			}
			
//			Empty 2개
			
			if (now.x > 0) {
				Pair p = new Pair(0, now.y, now.cnt+1);
				
				if (!visited.contains(p)) {
					visited.add(p);
					q.add(p);
				}
			}
			
			if (now.y > 0) {
				Pair p = new Pair(now.x, 0, now.cnt+1);
				
				if (!visited.contains(p)) {
					visited.add(p);
					q.add(p);
				}
			}
			
//			Move 2개 (x->y), (y->x)
			if (now.x + now.y <= b) {
				Pair p = new Pair(0, now.x+now.y, now.cnt+1);
				
				if (!visited.contains(p)) {
					visited.add(p);
					q.add(p);
				}
			} else {
				Pair p = new Pair(now.x+now.y-b, b, now.cnt+1);
				
				if (!visited.contains(p)) {
					visited.add(p);
					q.add(p);
				}
			}
			
			if (now.x + now.y <= a) {
				Pair p = new Pair(now.x+now.y, 0, now.cnt+1);
				
				if (!visited.contains(p)) {
					visited.add(p);
					q.add(p);
				}
			} else {
				Pair p = new Pair(a, now.x+now.y-a, now.cnt+1);
				
				if (!visited.contains(p)) {
					visited.add(p);
					q.add(p);
				}
			}
		}
		System.out.println(-1);
	}
}
