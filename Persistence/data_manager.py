#!/usr/bin/python3
from .IPersistence import IPersistenceManager
import json
import os

class DataManager(IPersistenceManager):
    """
    DataManager class is responsible for managing the persistence of entities.

    Attributes:
        storage_file (str): The path to the storage file.

    Methods:
        __init__(self, storage_file="data.json"): Initializes a DataManager instance.
        _load_data(self): Loads data from the storage file.
        _write_data(self, data): Writes data to the storage file.
        save(self, entity): Saves an entity to the storage file.
        get(self, entity_id, entity_type): Retrieves an entity from the storage file.
        update(self, entity): Updates an entity in the storage file.
        delete(self, entity_id, entity_type): Deletes an entity from the storage file.
    """

    def __init__(self, storage_file="data.json"):
        """
        Initializes a DataManager instance.

        Args:
            storage_file (str): The path to the storage file.
        """
        self.storage_file = storage_file
        if not os.path.exists(storage_file):
            with open(storage_file, "w") as f:
                f.write("{}")

    def _load_data(self):
        """
        Loads data from the storage file.

        Returns:
            dict: The loaded data.
        """
        with open(self.storage_file, "r") as f:
            return json.load(f)

    def _write_data(self, data):
        """
        Writes data to the storage file.

        Args:
            data (dict): The data to be written.
        """
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=4)

    def save(self, entity):
        """
        Saves an entity to the storage file.

        Args:
            entity: The entity to be saved.
        """
        with open(self.storage_file, "r") as f:
            data = json.load(f)
        entity_id = getattr(entity, "id")
        entity_type = type(entity).__name__
        if entity_type not in data:
            data[entity_type] = {}
        data[entity_type][entity_id] = entity.__dict__
        self._write_data(data)
        print(f"Entity {entity_type} with id {entity_id} saved.")

    def get(self, entity_id = "", entity_type = ""):
        """
        Retrieves an entity from the storage file.

        Args:
            entity_id: The ID of the entity to be retrieved.
            entity_type: The type of the entity to be retrieved.

        Returns:
            dict: The retrieved entity.
        """
        data = self._load_data()
        if entity_type in data and str(entity_id) in data[entity_type]:
            return data[entity_type][str(entity_id)]
        else:
            print(f"Entity {entity_type} with id {entity_id} not found.")

    def get_all(self, entity_type):
            '''
            Retrieve all entities of a given type from the data manager.

            Args:
                entity_type (str): The type of entity to retrieve.

            Returns:
                list: A list of entities of the given type.
            '''
            data = self._load_data()

            if entity_type in data:
                return data(entity_type)

    def update(self, entity):
        """
        Updates an entity in the storage file.

        Args:
            entity: The entity to be updated.
        """
        data = self._load_data()
        entity_id = getattr(entity, "id")
        entity_type = type(entity).__name__
        if entity_type in data and str(entity_id) in data[entity_type]:
            data[entity_type][entity_id] = entity.__dict__
            self._write_data(data)
            print(f"Entity {entity_type} with id {entity_id} updated.")
        else:
            print(f"Entity {entity_type} with id {entity_id} not found.")

    def delete(self, entity_id, entity_type):
        """
        Deletes an entity from the storage file.

        Args:
            entity_id: The ID of the entity to be deleted.
            entity_type: The type of the entity to be deleted.
        """
        data = self._load_data()
        if entity_type in data and str(entity_id) in data[entity_type]:
            del data[entity_type][str(entity_id)]
            self._write_data(data)
            print(f"Entity {entity_type} with id {entity_id} deleted.")
        else:
            print(f"Entity {entity_type} with id {entity_id} not found.")
