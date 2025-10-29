from datetime import datetime
from functools import wraps
from typing import Any


def log(filename: str = "") -> Any:
    """
    Декоратор логирования выполнения функции
    """

    def decorator(func) -> Any:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start_run = datetime.now()
            func_name = func.__name__
            str_args = str(args)
            str_kwargs = str(kwargs)
            error_data_bool = False

            try:
                result = func(*args, **kwargs)
            except Exception as error_:
                error_data_bool = True
                error_data = str(error_)

            stop_run = datetime.now()
            if filename:
                with open(filename, "w", encoding="utf-8") as file_:
                    file_.write("Время начала - " + start_run.strftime("%Y-%m-%d %H:%M:%S") + "\n")
                    file_.write("Время окончания - " + stop_run.strftime("%Y-%m-%d %H:%M:%S") + "\n")
                    if error_data_bool:
                        file_.write(func_name + " error: " + error_data + " Inputs: " + str_args + " - " + str_kwargs)
                    else:
                        file_.write(func_name + " ok\n")
                        file_.write("Результат выполнения - " + str(result))
                        return result
            else:
                print("Время начала - " + start_run.strftime("%Y-%m-%d %H:%M:%S"))
                print("Время окончания - " + stop_run.strftime("%Y-%m-%d %H:%M:%S"))
                if error_data_bool:
                    print(func_name + " error: " + error_data + " Inputs: " + str_args + " - " + str_kwargs)
                else:
                    print(func_name + " ok")
                    print("Результат выполнения - " + str(result))
                    return result

        return wrapper

    return decorator
