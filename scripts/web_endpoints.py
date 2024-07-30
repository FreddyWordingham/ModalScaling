from modal import App, web_endpoint

app = App()


@app.function()
@web_endpoint()
def f():
    return "Hello world!"
