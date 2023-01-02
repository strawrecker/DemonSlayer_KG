from neo4j import GraphDatabase


def merge_node_tx(tx, name):
    query = "MERGE (p: Entity{name: $name})"
    result = tx.run(query, name=name)
    # record = result.single()
    # return record["node_id"]


def match_node_tx(tx, name_x, name_y, relation_x2y):
    query = ("MATCH(x: Entity), (y: Entity) \
            WHERE x.name= '%s' AND y.name= '%s'\
            MERGE(x)-[:%s]->(y)" % (name_x, name_y, relation_x2y))
    result = tx.run(query)


if __name__ == "__main__":
    driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "123456"))
    with open("../data/DemonSlayer_relations_clean.csv") as f:
        for line in f.readlines():
            relation = line.strip("\n").split(",")
            with driver.session() as session:
                session.execute_write(merge_node_tx, relation[0])
                session.execute_write(merge_node_tx, relation[1])
                session.execute_write(match_node_tx, relation[0], relation[1], relation[2])
    driver.close()
