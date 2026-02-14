import ast
import networkx as nx
def extract_dependencies(code):
    deps = []
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                deps.append(name.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                deps.append(node.module)
    return deps
def build_dependency_graph(chunks):
    graph = nx.DiGraph()
    for c in chunks:
        module = c["file"]
        graph.add_node(module)
        deps = extract_dependencies(c["content"])
        for d in deps:
            graph.add_edge(module, d)
    return graph
