# define filename as a constant
FILE_INPUT = 'input.txt'
FILE_LL = 'll.txt'
FILE_LR = 'lr.txt'
nested_dict = {}



def LL(input):
    counter = 0
    column = []

    initial_key = ""
    #first line of FILE_LL assign to column array
    with open(FILE_LL, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace(" ", "")
            line = line.replace('\n', '').split(";")
            if (counter == 0):
                line.pop(0)
                column = line
            else:

                outer_dict = {}
                nested_dict.update({line[0]: {}})
                key1 = line.pop(0)

                if (counter == 1):
                    initial_key = key1

                for i in range(len(column)):
                    outer_dict.update({column[i]: line[i]})

                nested_dict[key1] = outer_dict

            counter = counter + 1

    order_no = 0
    temp_stack = []
    temp_string = ""
    input_stack = []
    main_stack = []
    main_stack.append("$")
    cnt_no = 1
    action_temp_stack = []

    #The input string is split by looking at the values in the column array and transferred to the stack
    for i in range(len(input)):
        temp_string = temp_string + input[i]

        if (column.__contains__(temp_string) == True):
            temp_stack.append(temp_string)
            temp_string = ""

    #reversing stack
    for i in range(len(temp_stack)):
        input_stack.append(temp_stack.pop())

    print(f"{'NO' : <4}{'|' : <15}{'STACK' : <30}{'|' : <15}{'INPUT' : <30}{'|' : <15}{'ACTION' : <30}")

    while True:

        order_no = order_no + 1
        temp_input_stack = input_stack.pop()
        temp_main_stack = main_stack.pop()


        if (temp_main_stack == temp_input_stack): #if the elements of the stack and input are the same, they are deleted
            str_print1 = ""
            str_print2 = ""
            input_stack.append(temp_input_stack)
            main_stack.append(temp_main_stack)
            str_print1 = str_print1.join(main_stack)
            str_print2 = str_print2.join(reversed(input_stack))
            print(f"{order_no : <4}{'|' : <15}{str_print1 : <30}{'|' : <15}{str_print2 : <30}{'|' : <15}{f'Match and remove {temp_main_stack}'  : <30}")
            input_stack.pop()
            main_stack.pop()
        else:#If it is not the same, its equivalent in the dictionary is checked and the action is determined
            input_stack.append(temp_input_stack)

            if (cnt_no == 1):
                main_stack.append(temp_main_stack)
                action = nested_dict[initial_key][column[0]]
                #action is written according to the first column of the first element of the table

                if (action == ""):#rejected state for the first situation
                    str_print1 = ""
                    str_print2 = ""
                    str_print1 = str_print1.join(main_stack)
                    str_print2 = str_print2.join(reversed(input_stack))
                    print(f"{order_no : <4}{'|' : <15}{str_print1 : <30}{'|' : <15}{str_print2 : <30}{'|' : <15}{'Rejected' : <30}")
                    break
                else:
                    str_print1 = ""
                    str_print2 = ""
                    str_print1 = str_print1.join(main_stack)
                    str_print2 = str_print2.join(reversed(input_stack))
                    print(f"{order_no : <4}{'|' : <15}{str_print1 : <30}{'|' : <15}{str_print2 : <30}{'|' : <15}{action : <30}")


            else: #by taking the last element of the stack and the last element of the input, its equivalent in the dictionary is checked and the action is selected
                action = nested_dict[temp_main_stack][temp_input_stack]
                if (action == ""):#reject situation
                    str_print1 = ""
                    str_print2 = ""
                    main_stack.append(temp_main_stack)
                    str_print1 = str_print1.join(main_stack)
                    str_print2 = str_print2.join(reversed(input_stack))
                    print(f"{order_no : <4}{'|' : <15}{str_print1 : <30}{'|' : <15}{str_print2 : <30}{'|' : <15}{'Rejected' : <30}")
                    main_stack.pop()
                    break
                else:#normal situation
                    str_print1 = ""
                    str_print2 = ""
                    main_stack.append(temp_main_stack)
                    str_print1 = str_print1.join(main_stack)
                    str_print2 = str_print2.join(reversed(input_stack))
                    print(f"{order_no : <4}{'|' : <15}{str_print1 : <30}{'|' : <15}{str_print2 : <30}{'|' : <15}{action : <30}")
                    main_stack.pop()
            cnt_no = cnt_no + 1
            action_str = action.split('>')[1]
            temp_str2 = ""

            for char_counter in range(len(action_str)):
            #separating terminal or non-terminal when selecting the elements of the action
                if (action_str[char_counter].isupper() == False):
                    temp_str2 = temp_str2 + action_str[char_counter]
                    if (column.__contains__(temp_str2) == True):
                        action_temp_stack.append(temp_str2)
                        temp_str2 = ""
                else:
                    action_temp_stack.append(action_str[char_counter])

            for item in range(len(action_temp_stack)):
                main_stack.append(action_temp_stack.pop())


        if (len(input_stack) == 1): #accepted situation
            if (len(main_stack) == 1):
                str_print1 = ""
                str_print2 = ""
                str_print1 = str_print1.join(main_stack)
                str_print2 = str_print2.join(reversed(input_stack))
                print(f"{order_no + 1 : <4}{'|' : <15}{str_print1 : <30}{'|' : <15}{str_print2 : <30}{'|' : <15}{'ACCEPT' : <30}")
                break


def LR(input):
    counter = 0
    column = []
    global nested_dict
    nested_dict = {}
    order_no = 0

    initial_key = ""
    #filling dictionary
    with open(FILE_LR, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace(" ", "")
            line = line.replace('\n', '').split(";")
            if (counter == 1):
                line.pop(0)
                column = line
            elif (counter != 0 and counter != 1):

                outer_dict = {}
                nested_dict.update({line[0]: {}})
                key1 = line.pop(0)

                if (counter == 2):
                    initial_key = key1

                for i in range(len(column)):
                    outer_dict.update({column[i]: line[i]})

                nested_dict[key1] = outer_dict

            counter = counter + 1

    input_stack = []
    main_stack = []
    main_stack.append(initial_key)
    temp_main_stack = ""
    action = ""

    flag = False
    print(f"{'NO' : <4}{'|' : <15}{'STATE STACK' : <30}{'|' : <15}{'READ' : <30}{'|' : <15}{'INPUT' : <30}{'|' : <15}{'ACTION' : <30}")
    while True:

        counter_wh = 0
        while (counter_wh != len(input)):#reading input according to counter_wh
            order_no += 1
            temp_main_stack = main_stack.pop()

            main_stack.append(temp_main_stack)

            if (temp_main_stack == ""):#rejected situation
                str_print1 = ""
                str_print2 = ""
                str_print1 = str_print1.join(main_stack)
                str_print2 = str_print2.join(reversed(input_stack))
                print(f"{order_no : <4}{'|' : <15}{str_print1 : <30}{'|' : <15}{input[counter_wh] : <30}{'|' : <15}{input : <30}{'|' : <15}{'Rejected' : <30}")
                flag = True
                break
            else:
                str_print1 = ""
                str_print2 = ""
                str_print1 = str_print1.join(main_stack)
                str_print2 = str_print2.join(reversed(input_stack))
                if(order_no==1):#In the first time, the action is determined according to the first element in the table and the first element of the input.
                    action=nested_dict[initial_key][input[0]]
                    if(action==""):#rejected situation
                        print(f"{order_no : <4}{'|' : <15}{str_print1 : <30}{'|' : <15}{input[counter_wh] : <30}{'|' : <15}{input : <30}{'|' : <15}{'REJECTED': <30}")
                        flag = True
                        break
                    else:#normal situation
                        print(f"{order_no : <4}{'|' : <15}{str_print1 : <30}{'|' : <15}{input[counter_wh] : <30}{'|' : <15}{input : <30}{'|' : <15}{action : <30}")
                else:
                    action = nested_dict[temp_main_stack][input[counter_wh]]
                    print(f"{order_no : <4}{'|' : <15}{str_print1 : <30}{'|' : <15}{input[counter_wh] : <30}{'|' : <15}{input : <30}{'|' : <15}{action : <30}")

            if ("->" in action):#splitting action
                action_list = action.split("->")
                input = input.replace(action_list[1], action_list[0])
                for k in range(len(action_list[1])):
                    main_stack.pop()
                    counter_wh = counter_wh - 1
            else:
                if (action != "Accept"):
                    main_stack.append(action)
                counter_wh = counter_wh + 1

        if (action == "Accept"):
            break
        if (flag == True):
            break


def main():
    f = open(FILE_INPUT, 'r')
    file = f.readlines()

    input = [item.split(';', 1)[1] for item in file]
    derivation = [item.split(';', 1)[0] for item in file]
    input.pop(0)
    derivation.pop(0)
    input = [it.split('\n')[0] for it in input]
    derivation = [it.strip() for it in derivation]
    input = [it.strip() for it in input]
    print(f"Read LL(1) parsing table from file {FILE_LL}.")
    print(f"Read LR(1) parsing table from file {FILE_LR}.")
    print(f"Read input strings from file {FILE_INPUT}.")

    #inputs read from the file are sent to functions
    for i in range(len(input)):
        if (derivation[i] == "LL"):
            print(f"\nProcessing input string {input[i]} for LL(1) parsing table.")
            LL(input[i])
            print("")
        elif (derivation[i] == "LR"):
            print(f"\nProcessing input string {input[i]} for LR(1) parsing table.")
            LR(input[i])
            print("")


main()