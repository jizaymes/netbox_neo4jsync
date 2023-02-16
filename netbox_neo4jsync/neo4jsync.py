from .models import Neo4jSyncDataModel
from neo4j import GraphDatabase
from rich import inspect


NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "sdfsfsdf"

class Neo4jSync:
    neo4j_driver = False

    def __init__(self, DEBUG: bool):

        self.DEBUG = DEBUG
        try:
            self._initNeo4j()
        except Exception as e:
            return


    def __del__(self):
        if self.neo4j_driver:
            self.neo4j_driver.close()


    def process_data(self, data: Neo4jSyncDataModel):
        if not self.neo4j_driver:
            return False

        if self.DEBUG:
            inspect(data)

        if data.action not in [ 'create', 'update', 'delete']:
            raise SystemError("Should never get here")

        with self.neo4j_driver.session(database="neo4j") as session:
            session.execute_write(self.update_node, data=data)
        
        session.close()


    def _initNeo4j(self):
        with GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD)) as driver:
            driver.verify_connectivity()

        self.neo4j_driver = driver


    def update_node(self, tx, data):
        if data.action == "update" or data.action == "create":
            cypher_query = f"MERGE (node:{data.class_name} {{object_id: {data.object_id}}}) SET node = {{object_id: {data.object_id}, {data.field_name}: '{data.value}'}} RETURN (node)"
        elif data.action == "delete":
            cypher_query = f"MATCH (node:{data.class_name} {{object_id: {data.object_id}}}) DELETE (node)"

        if self.DEBUG:
            print(cypher_query)
        result = tx.run(cypher_query)
        records = list(result)
        summary = result.consume()
        return records, summary