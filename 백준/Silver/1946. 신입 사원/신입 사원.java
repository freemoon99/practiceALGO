import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	static int t, n;
	static ArrayList<Pair> list;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        t = Integer.parseInt(br.readLine());
        
        for (int i=0; i<t; i++) {
        	n = Integer.parseInt(br.readLine());
        	list = new ArrayList<>();
        	int cnt = 1;
        	
        	
        	for (int j=0; j<n; j++) {
        		st = new StringTokenizer(br.readLine());
        		
        		int a = Integer.parseInt(st.nextToken());
        		int b = Integer.parseInt(st.nextToken());
        		
        		list.add(new Pair(a, b));
        	}
        	
        	Collections.sort(list);
        	
        	int pre = list.get(0).n2;
        	for (Pair next : list) {
        		int now = next.n2;
        		
        		if (now < pre) {
        			cnt ++;
        			pre = now;
        		}
        		
        	}
        	
        	System.out.println(cnt);
        }
        
    }
    
    static class Pair implements Comparable<Pair>{
    	int n1, n2;
    	
    	public Pair(int n1, int n2) {
    		 this.n1 = n1;
    		 this.n2 = n2;
    	}
    	
    	public int compareTo(Pair p) {
    		return this.n1 - p.n1;
    	}
    	
    }

}