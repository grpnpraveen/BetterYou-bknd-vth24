from db_wrappers.connect_cluster import ConnectCluster

def find_record(query):
    try:
        db_connection = ConnectCluster()

        collection = db_connection.get_collection("betteryou","users")
        res = len(collection.find(query))

        if res > 0:
            return "old"
        return "new"

    except e:
        raise CustomErrors(f"Unknown Error occurred i.e {e}", 500)

    finally:
        db_connection.close_connection()


def add_user(data):
    try:
        db_connection = ConnectCluster()
        collection = db_connection.get_collection("betteryou","users")
        res = collection.insert_one(data)
        print(res)
    except e:
        raise CustomErrors(f"Unknown Error occurred i.e {e}", 500)

    finally:
        db_connection.close_connection()

def get_user_profile(query):
    try:
        db_connection = ConnectCluster()

        collection = db_connection.get_collection("betteryou","users")
        res = len(collection.find(query))

        if res > 0:
            return res
        return None

    except e:
        raise CustomErrors(f"Unknown Error occurred i.e {e}", 500)

    finally:
        db_connection.close_connection()