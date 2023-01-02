from neo4j import GraphDatabase


# input name_x relation
# name_x-relation->name_y
# return name_y
def name_x_relation_query_name_y(tx, name_x, relation):
    query = "Match(n: Entity {name: \"%s\"})-[r: `%s`]->(m:Entity) return m.name AS name" % (name_x, relation)
    result = tx.run(query)
    result = list(result)
    names = [record["name"] for record in result]
    return names


# input name_y relation
# name_x-relation->name_y
# return name_x
def relation_name_y_query_name_x(tx, relation, name_y):
    query = "Match(n: Entity)-[r: `%s`]->(m:Entity {name: \"%s\"}) return n.name AS name" % (relation, name_y)
    result = tx.run(query)
    result = list(result)
    names = [record["name"] for record in result]
    return names


if __name__ == '__main__':
    driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "123456"))
    with driver.session() as session:
        print(session.execute_read(name_x_relation_query_name_y, name_x="灶门祢豆子", relation="大哥"))
        print(session.execute_read(relation_name_y_query_name_x, relation="性别", name_y="男"))
