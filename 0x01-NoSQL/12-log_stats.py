#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def log_stats(mongo_collection):
    """ Provides some stats about Nginx logs stored in MongoDB """
    # Number of documents
    print("{} logs".format(mongo_collection.count_documents({})))

    # Number of documents with method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("\tmethod {}: {}".format(method, mongo_collection.count_documents({"method": method})))

    # Number of documents with method GET and path /status
    print("{} status check".format(mongo_collection.count_documents({"method": "GET", "path": "/status"})))


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017')
    logs_collection = client.logs.nginx
    log_stats(logs_collection)
