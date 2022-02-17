import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Baek1012 {
    static int[][] graph;
    static int N, M;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for(int i=0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            graph = new int[M][N];
            for(int k=0; k<M; k++) Arrays.fill(graph[k], 0);

            for(int j=0; j<K; j++) {
                st = new StringTokenizer(br.readLine());
                int X = Integer.parseInt(st.nextToken());
                int Y = Integer.parseInt(st.nextToken());
                graph[X][Y] = 1;
            }

            int count = 0;
            for(int x=0; x<M; x++) {
                for(int y=0; y<N; y++) {
                    if(graph[x][y] == 1) {
                        bfs(x, y);
                        count++;
                    }
                }
            }
            System.out.println(count);
        }
    }

    static void bfs(int X, int Y) {
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, -1, 0, 1};

        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(X, Y));
        graph[X][Y] = -1;

        while(!q.isEmpty()) {
            Point cur = q.poll();

            for(int i=0; i<4; i++){
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if(nx>=0 && nx < M && ny >=0 && ny < N) {
                    if(graph[nx][ny] == 1) {
                        q.offer(new Point(nx, ny));
                        graph[nx][ny] = -1;
                    }
                }
            }
        }
    }
}
