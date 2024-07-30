from typing import Dict

from modal import App, web_endpoint

app = App()


@app.function()
@web_endpoint(method="POST")
def square(item: Dict):
    return {"square": item["x"] ** 2}
