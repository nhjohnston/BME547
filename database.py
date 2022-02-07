class Patient:

    def __init__(self, patient_name, patient_id, age):
        self.name = patient_name
        self.id = patient_id
        self.age = age
        self.test = []
    
    def __repr__(self):
        return "Patient: {}, {}".format(self.name, self.id)
    
    def output_patient(self):
        output_string = "Name: {}\n".format(self.name)
        output_string += "ID: {}\n".format(self.id)
        output_string += "Age: {}\n".format(self.age)
        output_string += "Test: {}\n".format(self.test)


def add_patient(patient_name, patient_id, age):
    new_patient = Patient(patient_name, patient_id, age)
    return new_patient


def main():
    db = []
    x = add_patient("Ann Ables", 342, 40)
    db.append(x)
    y = add_patient("Bob Boyles", 50, 50)
    db.append(y)
    z = add_patient("Chris Columbus", 111, 35)
    db.append(z)
    db.append(add_patient("David Dinkins", 22, 72))
    found_patient = find_patient(db, 111)
    print(found_patient.output_patient())
    # output_database(db)
    add_test_to_patient(db, 111, "HDL", 100)
    # print(db)
    return db


def output_database(db):
    for patient in db:
        output_patient(patient)


def find_patient(db, id_no):
    for patient in db:
        if patient.id == id_no:
            return patient
    return


def add_test_to_patient(db, id_no, test_name, test_result):
    patient = find_patient(db, id_no)
    test_tuple = (test_name, test_result)
    patient.test.append(test_tuple)


def print_directory(db):
    rooms = ['Room 13', 'Room 12', 'Room 99', 'Room 3']
    for room, patient in zip(rooms, db):
        print("Name: {}  Room: {}".format(patient.name, room))


def create_id_tag_string(patient):
    id_string = "{}: {}".format(patient.name, patient.id)
    return id_string


if __name__ == "__main__":
    db = main()
    # print_directory(db)
    # print(create_id_tag_string(find_patient(db, 111)))
