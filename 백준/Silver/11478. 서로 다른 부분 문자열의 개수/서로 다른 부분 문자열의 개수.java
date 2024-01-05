import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	static String s;
	static Set<String> candidates;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        String s = br.readLine();
        candidates = new HashSet<>();
        
        for (int i=1; i<=s.length(); i++) {
        	for (int j=0; j<=s.length()-i; j++) {
        		candidates.add(s.substring(j, j+i));
        	}
        }
        
        System.out.print(candidates.size());
    }
}