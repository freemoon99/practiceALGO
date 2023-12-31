import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;


public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		BigInteger n = new BigInteger(br.readLine());
		
		if (n.remainder(BigInteger.valueOf(7)).equals(BigInteger.ZERO) || n.remainder(BigInteger.valueOf(7)).equals(BigInteger.valueOf(2))) {
			System.out.print("CY");
		} else {
			System.out.print("SK");
		}
	}

}
