import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	static int n;
	static Node[] tree;
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		n = Integer.parseInt(br.readLine());
		tree = new Node[123];
		
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			char node = st.nextToken().charAt(0);
			char left = st.nextToken().charAt(0);
			char right = st.nextToken().charAt(0);
			
			tree[node] = new Node(node);
			tree[node].left = left;
			tree[node].right = right;
			
//			System.out.print(tree);
		}
		
//		전위
		preorder('A');
		System.out.println();
//		중위
		inorder('A');
		System.out.println();
//		후위
		postorder('A');
		System.out.println();

	}
	
	static class Node{
		char parent, left, right;
		
		public Node(char parent) {
			this.parent = parent;
		}
	}
	
	private static void preorder(char node) {
		if (node == '.') return;
		System.out.print(tree[node].parent);
		preorder(tree[node].left);
		preorder(tree[node].right);
		
	}
	
	private static void inorder(char node) {
		if (node == '.') return;
		inorder(tree[node].left);
		System.out.print(tree[node].parent);
		inorder(tree[node].right);
		
	}
	
	private static void postorder(char node) {
		if (node == '.') return;
		postorder(tree[node].left);
		postorder(tree[node].right);
		System.out.print(tree[node].parent);
	}

}
