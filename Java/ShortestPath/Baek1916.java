import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Baek1916 {
    static int N;
    static int[] dist;
    static ArrayList<node>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        graph = new ArrayList[N+1];
        dist = new int[N+1];

        Arrays.fill(dist, Integer.MAX_VALUE);

        for(int i = 0; i < N + 1; i++)
            graph[i] = new ArrayList<>();


        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            graph[a].add(new node(b, cost));
        }

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        dijkstra(start);
        System.out.println(dist[end]);
    }

    static void dijkstra(int start) {
        PriorityQueue<node> pq = new PriorityQueue<>();
        pq.offer(new node(start, 0));
        dist[start] = 0;

        while(!pq.isEmpty()) {
            node cur = pq.poll();

            for(node next: graph[cur.n]) {
                if(dist[cur.n] + next.w < dist[next.n]) {
                    dist[next.n] = dist[cur.n] + next.w;
                    pq.offer(new node(next.n, dist[next.n]));
                }
            }
        }
    }

    static class node implements Comparable<node> {
        int n;
        int w;

        node(int n, int w) {
            this.n = n;
            this.w = w;
        }

        @Override
        public int compareTo(node o) {
            return this.w - o.w;
        }
    }
}
