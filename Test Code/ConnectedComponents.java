import java.util.*;
import java.io.*;

public class ConnectedComponents {
    private Map<Integer, List<Integer>> graph;
    private boolean[] visited;
    private int numVertices;
    
    public ConnectedComponents(int numVertices) {
        this.numVertices = numVertices;
        this.graph = new HashMap<>();
        this.visited = new boolean[numVertices];
        
        for (int i = 0; i < numVertices; i++) {
            graph.put(i, new ArrayList<>());
        }
    }
    
    // Add edge to undirected graph / 무방향 그래프에 간선 추가
    public void addEdge(int u, int v) {
        graph.get(u).add(v);
        graph.get(v).add(u);
    }
    
    // DFS to find connected component / 연결된 구성 요소 찾기
    private void dfs(int vertex, List<Integer> component) {
        visited[vertex] = true;
        component.add(vertex);
        
        for (int neighbor : graph.get(vertex)) {
            if (!visited[neighbor]) {
                dfs(neighbor, component);
            }
        }
    }
    
    // Find all connected components / 모든 연결된 구성 요소 찾기
    public List<List<Integer>> findConnectedComponents() {
        Arrays.fill(visited, false);
        List<List<Integer>> components = new ArrayList<>();
        
        for (int i = 0; i < numVertices; i++) {
            if (!visited[i]) {
                List<Integer> component = new ArrayList<>();
                dfs(i, component);
                components.add(component);
            }
        }
        
        return components;
    }
    
    // Print connected components / 연결된 구성 요소 출력
    public void printConnectedComponents() {
        List<List<Integer>> components = findConnectedComponents();
        
        // Remove empty component (vertex 0 only) / 빈 구성 요소 제거
        components.removeIf(component -> component.size() == 1 && component.contains(0));
        
        System.out.println("Connected components: " + components.size());
        System.out.println("------------------------");
        
        for (int i = 0; i < components.size(); i++) {
            List<Integer> component = components.get(i);
            System.out.print("Component " + (i + 1) + ": ");
            
            Collections.sort(component);
            for (int j = 0; j < component.size(); j++) {
                System.out.print(component.get(j));
                if (j < component.size() - 1) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
        System.out.println();
    }
    
    // Read graph from file / 파일에서 그래프 읽기
    public static ConnectedComponents readFromFile(String filename) {
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            br.readLine(); // Skip first line / 첫 번째 줄 건너뛰기
            br.readLine(); // Skip second line / 두 번째 줄 건너뛰기
            
            List<int[]> edges = new ArrayList<>();
            int maxVertex = 0;
            String line;
            
            while ((line = br.readLine()) != null && !line.trim().isEmpty()) {
                String[] parts = line.trim().split("\\s+");
                if (parts.length >= 2) {
                    int u = Integer.parseInt(parts[0]);
                    int v = Integer.parseInt(parts[1]);
                    edges.add(new int[]{u, v});
                    maxVertex = Math.max(maxVertex, Math.max(u, v));
                }
            }
            
            ConnectedComponents cc = new ConnectedComponents(maxVertex + 1);
            for (int[] edge : edges) {
                cc.addEdge(edge[0], edge[1]);
            }
            
            return cc;
            
        } catch (IOException e) {
            System.err.println("File read error: " + e.getMessage());
            return null;
        }
    }
    
    // Process test file / 테스트 파일 처리
    public static void processFile(String filename) {
        System.out.println("File: " + filename);
        ConnectedComponents cc = readFromFile(filename);
        
        if (cc != null) {
            cc.printConnectedComponents();
        } else {
            System.out.println("Error reading file");
        }
    }
    
    public static void main(String[] args) {
        System.out.println("Test Files");
        System.out.println();
        
        String[] testFiles = {
            "s-1-9-10.txt",
            "s-2-54-50.txt", 
            "s-3-96-100.txt",
            "s-4-2450-100.txt"
        };
        
        for (String filename : testFiles) {
            processFile(filename);
        }
    }
}