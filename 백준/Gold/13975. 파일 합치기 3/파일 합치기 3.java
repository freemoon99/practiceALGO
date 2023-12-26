import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int t, k;
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		t = Integer.parseInt(br.readLine());
		
		for (int i=0; i<t; i++) {
			k = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			PriorityQueue<Long> pq = new PriorityQueue<Long>();
			
			for (int j=0; j<k; j++) {
				pq.add(Long.parseLong(st.nextToken()));
			}
			
			Long sum = (long) 0;
			while (pq.size()>1) {
				Long num1 = pq.poll();
				Long num2 = pq.poll();
				Long temp = num1+num2;
				sum += (temp);
				pq.add(temp);
			}
			System.out.println(sum);
		}
	}

}
