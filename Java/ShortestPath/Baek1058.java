import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baek1058 {
    static int n;
    static int[][] graph;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];

        for(int i=0; i<n; i++) {
            String s = br.readLine();
            for(int j=0; j < n; j++) {
                if(s.charAt(j) == 'Y')
                    graph[i][j] = 1;
                else
                    graph[i][j] = 100;
            }
        }
        floyd_warshall();
        int result = 0;
        for(int i=0; i<n; i++) {
            int tmp = 0;
            for(int j=0; j<n; j++) {
                if(i != j) {
                    if(graph[i][j] <= 2) tmp++;
                }
            }
            if(tmp > result) result = tmp;
        }
        System.out.println(result);
        br.close();
    }

    static void floyd_warshall() {
        for(int k=0; k<n; k++) {
            for(int i=0; i<n; i++) {
                for(int j=0; j<n; j++) {
                    if(graph[i][j] > graph[i][k] + graph[k][j])
                        graph[i][j] = graph[i][k] + graph[k][j];
                }
            }
        }
    }
}
