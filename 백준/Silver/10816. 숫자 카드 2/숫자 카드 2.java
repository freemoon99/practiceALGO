import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.StringTokenizer;


public class Main {
	static int n, m;
	static int[] numbers, answer;
	static HashMap<Integer, Integer> map;
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		n = Integer.parseInt(br.readLine());
		numbers = new int[n];
		st = new StringTokenizer(br.readLine(), " ");
		for (int i=0; i<n; i++){
			numbers[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(numbers);
		
		map = new HashMap<>();
		for (int j=0; j<n; j++) {
			if (map.get(numbers[j]) != null) {
				map.put(numbers[j], map.get(numbers[j])+1);
			}
			else{
				map.put(numbers[j], 1);
			}
		}
		
		m = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine(), " ");
		StringBuilder sb = new StringBuilder();
		for (int k=0; k<m; k++) {
			int num = Integer.parseInt(st.nextToken());
			if (map.containsKey(num)) {
				sb.append(map.get(num)).append(" ");
			} else {
				sb.append(0).append(" ");
			}
		}
		System.out.print(sb.toString().trim());
	}
	
}
