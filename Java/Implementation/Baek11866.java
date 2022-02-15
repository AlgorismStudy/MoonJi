import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.LinkedList;

public class Baek11866 {

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Queue<Integer> q = new LinkedList<>();
        for(int i=1; i <= n; i++) {
            q.add(i);
        }

        System.out.print("<");
        while(true) {
            for(int i = 1; i < k; i++) q.offer(q.poll());
            System.out.print(q.poll());

            if (!q.isEmpty()) System.out.print(", ");
            else break;
        }
        System.out.print(">");
    }

}
