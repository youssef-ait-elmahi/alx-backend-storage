#!/usr/bin/env python3
"""function that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """ Insert a new document in a collection based on kwargs """
    document = kwargs
    result = mongo_collection.insert_one(document)
    return result.inserted_id
