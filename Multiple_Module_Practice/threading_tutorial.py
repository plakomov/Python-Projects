# threading tutorial
# threading is good way to speed up processing when dealing with the web
import time
import threading
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping in {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done sleeping...{seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2 , 1]
    results = executor.map(do_something, seconds) # returns the result not a futures object
    for result in results:
        print(result)



    #results = [executor.submit(do_something, sec) for sec in seconds]
    #for f in concurrent.futures.as_completed(results):
     #   print(f.result())

    #f1 = executor.submit(do_something, 1) # Creates a future object
    #f2 = executor.submit(do_something, 1)
    #print(f1.result()) # returns the result of the method
    #print(f2.result())

# threads = []
# for _ in range(10):  # _ is throwaway variable
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()

# t1 = threading.Thread(target=do_something)  # We are creating a thread 1
# t2 = threading.Thread(target=do_something)  # We are creating a thread 2

# t1.start()
# t2.start()

# t1.join() # This allows to do the calculation of time_counter at the; otherwise, we start the method, sleep, but
# while the methods sleep, time_code below is ran, but we don't needt
# t2.join()

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} seconds(s)')
