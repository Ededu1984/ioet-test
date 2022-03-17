from datetime import datetime, timedelta
import os


class Payment:

    @staticmethod
    def read_folder(dir: str) -> list:
        result: list = []
        for root, dirs, files in os.walk(dir):
            if files != []:
                for file in files:
                    if file.endswith(".txt"):
                        filename: str = file
                        with open(root + '/' + str(filename)) as f:
                            try:
                                lines: list = f.readlines()
                                result.append(lines)
                            except Exception as error:
                                print(error)
                                result = ["Something went wrong, please check\
                                 the content of the text file"]

                return result
            else:
                result = ["The folder is empty."]
                return result

    @staticmethod
    def calculate_payment(hours: list) -> tuple:
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

        return employee_name, total_payment
