from utils.payment import Payment
import os


def main():
    # Gettting the root directory and including the employee folder
    dir = os.getcwd() + "/employees"
    dir = dir.replace("\\", "/")
    folder_result = Payment.read_folder(dir)
    # Conditional statement to define the returning message
    if folder_result != ['The folder is empty.']:
        for i in folder_result:
            result: tuple = Payment.calculate_payment(i)
            print(result[0])
    else:
        print(folder_result[0])


if __name__ == "__main__":
    main()
