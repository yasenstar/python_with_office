def handle_file(count, cost_time):
    print(f"You will process {count} documents, and estimate to take {cost_time} minutes")

handle_count = 5

handle_file(30, handle_count ) # prevent like this

handle_file(cost_time=30, count=handle_count)