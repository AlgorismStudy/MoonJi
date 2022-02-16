import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Baek2606 {
    static int[][] computer;
    static boolean [] visited;
    static int count = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int v = Integer.parseInt(st.nextToken());

        computer = new int[n+1][n+1];
        visited = new boolean[n+1];
        for(int i=0; i <= n; i++) Arrays.fill(computer[i], 0);
        Arrays.fill(visited, false);

        for(int i=0; i<v; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            computer[a][b] = 1;
            computer[b][a] = 1;
        }

        Queue<Integer> q = new LinkedList<>();
        q.offer(1);
        visited[1] = true;
        while(!q.isEmpty()) {
            int cur = q.poll();
            count++;

            for(int i=0; i <= n; i++) {
                if(computer[cur][i] == 1 && visited[i] == false) {
                    q.offer(i);
                    visited[i] = true;
                }
            }
        }
        System.out.println(count - 1);
    }
}
