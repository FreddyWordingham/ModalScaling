from modal import App


app = App("example-hello-world")


@app.function()
def my_func(i):
    if i % 2 == 0:
        print(f"Computing square of even number: {i}")
    return i * i


@app.local_entrypoint()
def main():
    # # run the function locally
    # print(my_func.local(1000))

    # # run the function remotely on Modal
    # print(my_func.remote(1000))

    # run the function in parallel and remotely on Modal
    num_parallel_containers = 5
    total = 0
    for result in my_func.map(range(num_parallel_containers)):
        total += result

    print(
        f"Total of square numbers between 0 and {num_parallel_containers} is: {total}"
    )
