from utils.payment import Payment


def main():
    dir = "./employees"
    folder_result = Payment.read_folder(dir)
    for i in folder_result:
        employee_payment: tuple = Payment.calculate_payment(i)
        print(f"The amount to pay {employee_payment[0]} is: \
        {employee_payment[1]}USD")


if __name__ == "__main__":
    main()
