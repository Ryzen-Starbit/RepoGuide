import time
def benchmark(retrieve_func, query):
    start = time.time()
    results = retrieve_func(query)
    end = time.time()
    return {
        "time": round(end - start, 3),
        "results": len(results)
    }
