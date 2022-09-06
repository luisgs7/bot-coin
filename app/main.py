'''Main project file.'''
from search import request_data
from utils import constants

def main() -> None:
    request_data.RequestData(url=constants.URL).data()

main()