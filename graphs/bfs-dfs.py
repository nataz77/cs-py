from .node import GraphNode
import queue


def main():
    """Driver program"""
    graph = sample_graph()
    bfs(graph)

    dfsgraph = sample_graph()
    dfs(dfsgraph[0])
    input()


def bfs(graph):
    """Executes a breadth-first search on a graph"""
    q = queue.Queue()
    q.put(graph[0])
    graph[0].mark_discovered()
    while q.qsize() != 0:
        item = q.get()
        for n in item.neightbours:
            if not n.data.Discovered:
                print(f"Found node via BFS {n.data.ID}")
                n.data.mark_discovered()
                q.put(n.data)
    return


def dfs(node):
    """Executes a depth-first search on a graph"""
    node.mark_discovered()
    for n in node.neightbours:
        if not n.data.Discovered:
            print(f"Found node via DFS {n.data.ID}")
            dfs(n.data)
        else:
            continue


def sample_graph():
    """Generates a sample graph"""
    graph = []
    for i in range(8):
        graph.append(GraphNode(i))

    graph[0].add_neighbour([
        graph[1],
        graph[6],
        graph[7]
    ])

    graph[1].add_neighbour([
        graph[2],
        graph[4],
        graph[7]
    ])

    graph[2].add_neighbour([
        graph[1],
        graph[5]
    ])

    graph[3].add_neighbour([
        graph[0],
        graph[1],
        graph[5]
    ])

    graph[4].add_neighbour([
        graph[1],
        graph[7]
    ])

    graph[5].add_neighbour([
        graph[2],
        graph[3]
    ])

    graph[6].add_neighbour([graph[0]])

    graph[7].add_neighbour([
        graph[0],
        graph[1],
        graph[4]
    ])

    return graph


if __name__ == "__main__":
    main()
