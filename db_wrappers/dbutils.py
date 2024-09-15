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
        data["rewards"] = 0
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

def update_user_record(query, data):
    try:
        db_connection = ConnectCluster()
        collection = db_connection.get_collection("betteryou", "users")

        # Ensure the query is a dictionary
        if not isinstance(query, dict):
            raise ValueError("Query must be a dictionary")

        # Ensure the data is a dictionary
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")

        # Check the type and prepare the update document
        if data.get("type") == "diet_plan":
            update_doc = {"$set": {"diet_plan": data.get("diet_plan")}}
        elif data.get("type") == "workout_plan":
            update_doc = {"$set": {"workout_plan": data.get("workout_plan")}}
        else:
            raise ValueError("Invalid type. Must be 'diet_plan' or 'workout_plan'")

        # Perform the update
        result = collection.update_one(query, update_doc)

        if result.matched_count > 0:
            return "Record updated successfully"
        return "No matching record found"

    except Exception as e:
        raise Exception(f"Unknown Error occurred: {e}", 500)

    finally:
        db_connection.close_connection()

def update_ngrok_url(url):
    try:
        db_connection = ConnectCluster()
        collection = db_connection.get_collection("betteryou", "ngrok")

        # Ensure the data is a dictionary
        if not isinstance(url, dict):
            raise ValueError("URL must be a dictionary")

        # Perform the update
        result = collection.update_one({}, {"$set": url}, upsert=True)

        if result.matched_count > 0:
            return "URL updated successfully"
        return "No matching record found"

    except Exception as e:
        raise Exception(f"Unknown Error occurred: {e}", 500)

    finally:
        db_connection.close_connection()


def insert_or_update_tasks(user_name,tasks):
    try:
        db_connection = ConnectCluster()

        collection = db_connection.get_collection("betteryou","tasks")
        task_query = {"user_name": user_name}
        update_query = {}
        for date, task_list in tasks.items():
            update_query[f"tasks.{date}"] = task_list  # Set tasks for the specific date

        # Perform the upsert operation (insert if doesn't exist, update if exists)
        result = collection.update_one(
            task_query,                # Find the document by user ID
            {"$set": update_query},    # Set the tasks for each date
            upsert=True                # Insert if the document does not exist
        )

        return "tasks updated successfully"

    except Exception as e:
        raise Exception(f"Unknown Error occurred i.e {e}", 500)

    finally:
        db_connection.close_connection()



def get_task_for(user_name):
    try:
        db_connection = ConnectCluster()

        collection = db_connection.get_collection("betteryou","tasks")
        task_query = {"user_name": user_name}
        
        user_document = collection.find_one(task_query)

        return user_document

    except Exception as e:
        raise Exception(f"Unknown Error occurred i.e {e}", 500)

    finally:
        db_connection.close_connection()

def get_task_by_date(user_name,date):
    try:
        db_connection = ConnectCluster()

        collection = db_connection.get_collection("betteryou","tasks")
        task_query = {"user_name": user_name}
        
        user_document = collection.find_one(task_query).get("tasks",[])

        return dict(user_document).get(date)

    except Exception as e:
        raise Exception(f"Unknown Error occurred i.e {e}", 500)

    finally:
        db_connection.close_connection()


def remove_task(user_name,date,task_name,point):
    try:
        db_connection = ConnectCluster()

        query = {"user_name": user_name}
        collection = db_connection.get_collection("betteryou","users")
        collection.update_one(query, {"$set": {"rewards": str(int(get_user_profile(query)["rewards"])+int(point)) }})
        collection = db_connection.get_collection("betteryou","tasks")
        
        collection.update_many(
            {
                "user_name": user_name,
                f"tasks.{date}.task_name": task_name
            },
            {
                "$pull": {
                    f"tasks.{date}": { "task_name": task_name }
                }
            }
        )
        # task_query = {"user_name": user_name}
        
        # user_document = collection.find_one(task_query).get("tasks",[])

        # collection.updateMany(
        # task_query,  
        # { "$pull": { "tasks.date": { task_name:  task_name} } })

        return "removed successfully"

    except Exception as e:
        raise Exception(f"Unknown Error occurred i.e {e}", 500)

    finally:
        db_connection.close_connection()