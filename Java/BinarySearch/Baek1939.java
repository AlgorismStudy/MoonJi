import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Baek1939 {
    static int N;
    static ArrayList<ArrayList<Node>> graph = new ArrayList<>();
    static boolean[] visited;
    static int start, end;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        for(int i=0; i < N+1; i++) {
            graph.add(new ArrayList<>());
        }

        int maxCost = 0;
        for(int i=0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());

            graph.get(A).add(new Node(B, C));
            graph.get(B).add(new Node(A, C));

            maxCost = Math.max(maxCost, C);
        }

        st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());

        int low = 1, high = maxCost;

        while(low <= high) {
            int mid = (low + high) / 2;
            if(BFS(mid)) low = mid + 1;
            else high = mid - 1;
        }
        System.out.println(high);
    }

    static boolean BFS(int mid) {
        Queue<Integer> q = new LinkedList<>();
        visited = new boolean[N+1];

        q.offer(start);
        visited[start] = true;

        while(!q.isEmpty()) {
            int cur = q.poll();
            if(cur == end) return true;

            for(Node n : graph.get(cur)) {
                if(!visited[n.d] && n.cost >= mid) {
                    visited[n.d] = true;
                    q.offer(n.d);
                }
            }
        }
        return false;
    }

    static class Node {
        int d;
        int cost;

        public Node(int d, int cost) {
            this.d = d;
            this.cost = cost;
        }
    }
}
