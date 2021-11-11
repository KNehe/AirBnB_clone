#!/usr/bin/python3

"""This class model defines all common attributes/methods for other classes"""

import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """defines attributes"""
    
        def __init__(self, *args, **kwargs):
            if kwargs:
                for key, value in kwargs.items():
                    if key == "created_at":
                        self.created_at = datetime.strptime
                        (kwags["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    elif key = "updated_at":
                        self.created_at = datetime.strptime(
                                 kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    elif key == "__class__":
                        continue
                    else:
                        self.__dict__[key] = value

            else:
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                self.id = str(uuid4())

        def __str__(self):
            """Returns a string representation of the base model"""
            return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

        def save(self):
             """Updates the attribute updated_at with the current datetime"""

             self.update_at = datetime.now()
             """models.storage.save()"""

        def to_dict(self):
            """"Returns a dictionary representation of the keys/values of the instance"""

            x_dict = self.__dict__.copy()
            x_dict["created_at"] = self.created_at.isoformat()
            x_dict["updated_at"] = self.updated_at.isoformat()
            x_dict["__class__"] = __class__.__name__
            return x_dict
