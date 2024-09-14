from db_wrappers.connect_cluster import ConnectCluster
from bson import ObjectId

def serialize_document(document):
    """Convert ObjectId to string to make it JSON serializable."""
    if document is not None:
        document["_id"] = str(document["_id"])  # Convert ObjectId to string
    return document

def find_record(query):
    try:
        db_connection = ConnectCluster()

        collection = db_connection.get_collection("betteryou","users")
        res = collection.count_documents(query)

        if res > 0:
            return "old"
        return "new"

    except Exception as e:
        raise Exception(f"Unknown Error occurred i.e {e}", 500)

    finally:
        db_connection.close_connection()


def add_user(data):
    try:
        db_connection = ConnectCluster()
        collection = db_connection.get_collection("betteryou","users")
        res = collection.insert_one(data)
        print(res)
    except Exception as e:
        raise Exception(f"Unknown Error occurred i.e {e}", 500)

    finally:
        db_connection.close_connection()

def get_user_profile(query):
    try:
        db_connection = ConnectCluster()

        # Ensure the query is a dictionary
        if not isinstance(query, dict):
            raise ValueError("Query must be a dictionary")

        collection = db_connection.get_collection("betteryou", "users")

        # Debug: Print the query
        # print(f"Query: {query}")

        # Debug: Print all documents in the collection
        # for doc in collection.find():
        #     print(f"Document: {doc}")

        res = collection.count_documents(query)

        # Debug: Print the count result
        # print(f"Count result: {res}")

        if res > 0:
            return serialize_document(collection.find_one(query))
        return None

    except Exception as e:
        raise Exception(f"Unknown Error occurred: {e}", 500)

    finally:
        db_connection.close_connection()