#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ar = []
    for run in range(list_length):
        a = 0
        try:
            a = my_list_1[run] / my_list_2[run]
        except (IndexError):
                print("Out of range")
        except (ZeroDivisionError):
                print("division by 0")
        except (TypeError):
                print("wrong type")
        finally:
                ar.append(a)
    return (ar)
