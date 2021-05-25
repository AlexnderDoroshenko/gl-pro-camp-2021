import time


def execution_time_delta(function):
    start_execution_time = time.time()
    function()
    print(f"--- seconds : {time.time() - start_execution_time} ---")