#!/usr/bin/python3

from pathlib import Path
import re
import json
from datetime import datetime


class FileStorage:
    """
    Serialize instances to JSON and Deserialize JSON to instance
    """

    __file_path = "file.json"
    __objects = {}
    __objects_dict = {}

    def all(self):
        """
        Returns all objects
        """

        return self.__objects

    def new(self, obj):
        """
        Sets objects ith obj class name
        """

        obj_id = obj.id
        obj_cls = obj.__class__.__name__
        key = obj_cls + "." + obj.id
        self.__objects[key] = obj.__str__()
        self.__objects_dict[key] = obj.to_dict()

    def save(self):
        """
        Serialize objects to JSON
        """

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(self.__objects_dict, file)

    def reload(self):
        """
        deserialize JSON to objects
        """

        path = Path(self.__file_path)
        if path.exists():
            with open(path, "r", encoding="utf-8") as obj_file:
                dict_ = json.load(obj_file)
                obj_dicts = {}
                for key, value in dict_.items():
                    inner_dict = {}
                    self.__objects_dict[key] = value
                    for key__, val_ in value.items():
                        if key_ == "created_at" or key_ == "updated_at":
                            val_ = datetime.strptime(
                                    val_, "Y-%m-%dT%H:%S.%f"
                                    )
                            if key_ == "__class__":
                                continue
                            inner_dict[ket_] = val_
                        obj_desc = "[{}] ({}) {}".format(
                                dict_[key]["__class__"],
                                inner_dict["id"],
                                inner_dict
                                )
                        obj_dicts[key] = obj_decs
                    self.__objects = obj_dicts

    def update_objects(self, dict_):
        """
        Updates objects with new instances
        """

        self.__objects = dict_
        keys_in_objects = set(self.__objects.keys())
        keys_in_objects_dict = set(self.__objects_dict.keys())
        deleted_key = list(keys_in_objects_dict - keys_in_objects)[0]
        del self.__objects_dict[deleted_key]

    def get_path(self):
        """
        Retrieves file storage path
        """
        return self.__file_path
