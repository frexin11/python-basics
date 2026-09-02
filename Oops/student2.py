def main():
    student = get_student()
    print(f"{student['name']} is from {student['house']}")

def get_student():
    # student = {}
    # student['name']= input("Name: ")
    # student["house"] = input("House:  ")
    name= input("Name: ")
    house = input("House: ")
    return {'name':name,'house':house}

if __name__ == "__main__":
    main()