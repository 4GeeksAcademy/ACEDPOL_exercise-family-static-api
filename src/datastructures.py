
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "name": "John Jackson",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "name": "Jane Jackson",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "name": "Jimmy Jackson",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)


    def add_member(self, member):
        # añade al nuevo miembro
        return self._members.append(member)


    def delete_member(self, id):
        # busca el miembro con el id y lo elimina
        for member in self._members:
            if member["id"] == id:
                return self._members.remove(member)
        pass # si no lo encuentra


    def get_member(self, id):
        # busca al miembro y lo devuelve
        for member in self._members:
            if member["id"] == id:
                return member
        pass # si no lo encuentra


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
