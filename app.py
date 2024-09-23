import logging

def main(req):
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        name = "World"

    return f"Hello {name}!"
