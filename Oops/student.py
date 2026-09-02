def main():
    # name = get_name()
    # house = get_house()
    name, house = get_student()
    print(f"{name} from {house}")

# def get_name():
#     name = input("Name = ")
#     return name
# def get_house():
#     house = input("House = ")
#     return house
def get_student():
    name = input("Name = ")
    house = input("House = ")
    return name, house

if __name__ == "__main__":
    main()