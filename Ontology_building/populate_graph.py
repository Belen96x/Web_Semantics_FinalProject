from rdflib import Graph, Literal, RDF, URIRef, Namespace
import pandas as pd

# Load your ontology
g = Graph()
g.parse(fr"C:\Users\belen\Desktop\Université de Lorraine\Second semester\Web_semantics_FinalProject\Web_Semantics_FinalProject\Ontology_building\Final_version_ont_ufo.ttl", format="ttl")

# Define namespaces
EX = Namespace("http://example.org/")
ONT = Namespace("http://www.semanticweb.org/belen/ontologies/2023/2/untitled-ontology-8#")

# Load your dataset
df = pd.read_csv(fr"C:\Users\belen\Desktop\Université de Lorraine\Second semester\Web_semantics_FinalProject\Web_Semantics_FinalProject\Dataset\ufo_uk_data.csv")

# Add your dataset to the graph
for index, row in df.iterrows():
    sighting = EX[f"sighting/{index}"]
    location = EX[f"location/{index}"]
    witness = EX[f"witness/{index}"]
    
    g.add((sighting, RDF.type, ONT.Sighting))
    g.add((location, RDF.type, ONT.Location))
    g.add((witness, RDF.type, ONT.Witness))
    
    g.add((sighting, ONT.hasLocation, location))
    g.add((sighting, ONT.hasWitness, witness))
    g.add((sighting, ONT.hasShape, Literal(row['ufo_shape'])))
    g.add((sighting, ONT.hasDate, Literal(row['date'])))
    g.add((sighting, ONT.hasTime, Literal(row['time'])))
    g.add((sighting, ONT.hasLength, Literal(row['encounter_length'])))
    
    g.add((location, ONT.city_area, Literal(row['city_area'])))
    g.add((location, ONT.state, Literal(row['state'])))
    g.add((location, ONT.country, Literal(row['country'])))
    g.add((location, ONT.latitude, Literal(row['latitude'])))
    g.add((location, ONT.longitude, Literal(row['longitude'])))
    
    g.add((witness, ONT.occupation, Literal(row['witness_occupation'])))
    
# Save the graph to a file
g.serialize(destination="ufo_data_output.ttl", format="ttl")

g = Graph()
g.parse("ufo_data_output.ttl", format="ttl")

# Convert to GraphML
g.serialize(destination="ufo_data_output.graphml", format="graphml")
