#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """creates an object from a Json file"""
    with open(filename, "r", encoding="utf-8") as file1:
        return(json.load(file1))
