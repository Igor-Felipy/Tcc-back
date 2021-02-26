from . import controllers

@controllers.route('/')
def main():
    return "main"