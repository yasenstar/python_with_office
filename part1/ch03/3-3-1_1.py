def handle_file(count, cost_time):
    print(f"You will process {count} documents, and estimate to take {cost_time} minutes")

handle_count = 5

handle_file(handle_count, 30)

handle_file(handle_count * 3, 30 * 2)