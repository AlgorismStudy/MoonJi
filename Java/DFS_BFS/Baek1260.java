import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Baek1260 {
    static int N, M, V;
    static int[][] graph;
    static boolean[] visit;

    public static void dfs(int i) {
        visit[i] = true;
        System.out.print(i + " ");
        for(int j = 0; j < N+1; j++) {
            if(graph[i][j] == 1 && visit[j] == false) {
                dfs(j);
            }
        }
    }

    public static void bfs(int i) {
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(i);
        visit[i] = true;

        while(!q.isEmpty()) {
            int cur = q.poll();
            System.out.print(cur + " ");

            for(int j=0; j < N+1; j++) {
                if(graph[cur][j] == 1 && visit[j] == false) {
                    q.offer((j));
                    visit[j] = true;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt((st.nextToken()));
        M = Integer.parseInt((st.nextToken()));
        V = Integer.parseInt((st.nextToken()));

        graph = new int[N+1][N+1];
        visit = new boolean[N+1];
        for(int i = 0; i < N; i++) Arrays.fill(graph[i],0);
        Arrays.fill(visit, false);

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt((st.nextToken()));
            int b = Integer.parseInt((st.nextToken()));
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        dfs(V);
        System.out.println();
        Arrays.fill(visit, false);
        bfs(V);

    }
}
