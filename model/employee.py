class Employee:
    def __init__(self,id,firstname,lastname,department,number,position):
        self.id=id
        self.firstname=firstname
        self.lastname=lastname
        self.department=department
        self.number=number
        self.position=position

    def __str__(self):
        return f"Id:{self.id} Firstname:{self.firstname:10} Lastname:{self.lastname:10} Department:{self.department} Position:{self.position} Number:{self.number}"
