def display_main_menu():
    print("Enter some temperature numbers")

def get_user_input():
    x = input("Please Input Your Name: ")
    print("Hello: " +  str(x))

def testing():
    string_list = ["1.5", "2.3", "4.0", "3.2"]
    float_list = []
    for x in string_list:
        float_list.append(float(x))
    print(float_list)

    return float_list

def getaverage():
    tem = input("Input a few temperatures with a space: ")
    temp = tem.split(" ")

    float_list = []
    for x in temp:
        float_list.append(float(x))

    total = sum(float_list)
    average = total/len(float_list)
    print("Average is: " + str(average))

    return average

def calc_min_max():
    temperature = input("Input a few temperature with a space: ")
    temp = temperature.split(" ")

    float_list = []
    for x in temp:
        float_list.append(float(x))
    print("Max: " +  str(max(float_list)))
    print("Min: " +  str(min(float_list)))
    
calc_min_max()

# getaverage()
# testing()
# if __name__ == "__main__":
#     display_main_menu()
#     get_user_input()