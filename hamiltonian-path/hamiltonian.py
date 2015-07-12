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

    def generate_paths(self):
        current_paths = [[x] for x in range(self.length)]
        finished_paths = []
        while len(current_paths) > 0:
            path = current_paths.pop(0)
            available_steps = self.available_steps(path)
            if len(available_steps):
                for step in available_steps:
                    current_paths.append(path + [step])
            else:
                finished_paths.append(path)

        return finished_paths

    def paths_and_cycles(self, finished_paths):
        paths = []
        cycles = []
        for path in finished_paths:
            if len(path) == self.length:
                paths.append(path)
                if path[0] in self.graph[path[-1]]:
                    cycles.append(path)
        return (paths, cycles)

    def available_steps(self, path):
        return [x for x in self.graph[path[-1]] if x not in path]

    def repeated_subpath(self, subpath, paths):
        for path in paths:
            for step in range(len(subpath)):
                if subpath[step] != path[step]:
                    break

            if step == len(subpath) and subpath[step] == path[step]:
                return True

        return False

if __name__ == "__main__":
    dodecaedron_graph = [
        [1, 4, 5], [0, 2, 7], [1, 3, 9], [2, 4, 11], [3, 0, 13],
        [0, 6, 14], [5, 7, 15], [6, 8, 1], [7, 9, 16], [8, 10, 2],
        [9, 11, 17], [10, 12, 3], [11, 13, 18], [12, 14, 4], [13, 5, 19],
        [16, 19, 6], [15, 17, 8], [16, 18, 10], [17, 19, 12], [18, 15, 14]
    ]
    dodecaedron = HamiltonianPath(dodecaedron_graph)
    generated_paths = dodecaedron.generate_paths()
    (paths, cycles) = dodecaedron.paths_and_cycles(generated_paths)
    print "Paths:\n%s" % str(paths)
    print "Cycles:\n%s" % str(cycles)
    print "\nThere are %d paths and %d cycles" % (len(paths), len(cycles))
