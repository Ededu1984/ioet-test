from datetime import datetime, timedelta
import os


class Payment:

    @staticmethod
    def read_folder(dir: str) -> list:
        # Creating an empty list
        result: list = []
        # Loop over the folder to read the text files
        for root, dirs, files in os.walk(dir):
            if files != []:
                for file in files:
                    if file.endswith(".txt"):
                        filename: str = file
                        with open(root + '/' + str(filename)) as f:
                            try:
                                lines: list = f.readlines()
                                result.append(lines)
                            except ValueError:
                                # Returning message if something went wrong
                                result = ["Something went wrong, please check the text file"]
            else:
                # Returning message in case the folder is empty
                result = ["The folder is empty."]
        return result

    @staticmethod
    def calculate_payment(hours: list) -> list:
        try:
            if hours != 'The folder is empty.':
                # Assigning variables
                employee_hours: list = hours[0].split(",")
                employee_name: str = employee_hours[0].split("=")[0]
                first_item: str = employee_hours[0].split("=")[1]
                employee_hours[0] = first_item
                total_payment: int = 0
                for i in employee_hours:
                    # Variables related to the time
                    interval: list = i[2:].split("-")
                    start: datetime = datetime.strptime(interval[0], "%H:%M")
                    end: datetime = datetime.strptime(interval[1], "%H:%M")
                    total_hours: timedelta = end - start
                    # Conditional statement to calculate the payment
                    if i[:2] in ['SA', 'SU']:
                        if start > datetime.strptime("00:00", "%H:%M") \
                                and (start <= datetime.strptime("09:00", "%H:%M")):
                            payment: int = int(str(total_hours)[0]) * 30
                        elif start > datetime.strptime("09:00", "%H:%M") \
                                and (start <= datetime.strptime("18:00", "%H:%M")):
                            payment: int = int(str(total_hours)[0]) * 20
                        else:
                            payment: int = int(str(total_hours)[0]) * 25
                    else:
                        if start > datetime.strptime("00:00", "%H:%M") \
                                and (start <= datetime.strptime("09:00", "%H:%M")):
                            payment: int = int(str(total_hours)[0]) * 25
                        elif start > datetime.strptime("09:00", "%H:%M") \
                                and (start <= datetime.strptime("18:00", "%H:%M")):
                            payment: int = int(str(total_hours)[0]) * 15
                        else:
                            payment: int = int(str(total_hours)[0]) * 20
                    total_payment += payment
                # Returning message with the total payment
                result: list = [f"The amount to pay {employee_name} is: {total_payment}USD"]
                return result

        except ValueError:
            # Returning message of error
            result: list = ["Something went wrong, please check the text file"]
            return result