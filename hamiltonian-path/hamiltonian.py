class HamiltonianPath():
    def __init__(self, graph):
        self.length = len(graph)
        if self.length < 3:
            raise ValueError("Graph should have at least 3 vertex")

        self.graph = graph
        self.vertex = [x for x in range(self.length)]

    def get_vertex(self):
        return self.vertex

    def graph_walk(self, path):
        pending_vertex = [x for x in range(self.length)]
        for step in range(len(path)):
            if step > 0 and path[step] not in self.graph[path[step - 1]]:
                return False
            pending_vertex.remove(path[step])

        return len(pending_vertex) == 0

    def generate_paths(self, start):
        paths = []
        path = [start]
        next_steps = self.available_steps(start, path)
        while len(next_steps):
            for step in next_steps:
                if self.repeated_subpath(path + [step], paths):
                    continue

            path += [step]
            next_steps = self.available_steps(step, path)
        paths.append(path)

        return paths

    def available_steps(self, current, path):
        return [x for x in self.graph[current] if x not in path]

    def repeated_subpath(self, subpath, paths):
        for path in paths:
            for step in range(len(subpath)):
                if subpath[step] != path[step]:
                    break

            if step == len(subpath) and subpath[step] == path[step]:
                return True

        return False
