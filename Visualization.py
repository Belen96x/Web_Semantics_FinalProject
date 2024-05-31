import rdflib
import networkx as nx
import matplotlib.pyplot as plt

# Load RDF data
g = rdflib.Graph()
g.parse("Conceptualisation.ttl", format="ttl")

# Create a NetworkX graph
G = nx.DiGraph()

# Helper function to get the prefixed name
def get_prefixed_name(node, graph):
    if isinstance(node, rdflib.URIRef):
        qname = graph.qname(node)
        if ':' in qname:
            return qname.split(':', 1)[1]  # Return only the local part
        else:
            return qname
    else:
        return str(node)

# Add triples to the NetworkX graph
for subj, pred, obj in g:
    G.add_edge(get_prefixed_name(subj, g), get_prefixed_name(obj, g), label=get_prefixed_name(pred, g))

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# Draw edges
nx.draw_networkx_edges(G, pos, width=2)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

# Draw edge labels
edge_labels = dict([((u, v,), d['label']) for u, v, d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Display the graph
plt.show()
