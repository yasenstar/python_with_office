def handle_file(count, cost_time=30, *args, **kwargs):
    print(f"You will process {count} documents, and estimate to take {cost_time} minutes")
    print("args: ", type(args), args)
    print("kwargs: ", type(kwargs), kwargs)

handle_count = 5

handle_file(handle_count)

handle_file(handle_count, 60, 80, 90, name="Pan", are=18)