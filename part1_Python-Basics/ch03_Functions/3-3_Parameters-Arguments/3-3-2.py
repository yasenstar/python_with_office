def handle_file(count, cost_time=30):
    print(f"You will process {count} documents, and estimate to take {cost_time} minutes")

handle_count = 5

handle_file(handle_count)

handle_file(handle_count, 60)