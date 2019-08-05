import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db-directory", default="/var/lib/postgresql/11/data", dest="dbDirectory", help="Database directory.")
    parser.add_argument("--port", default="5432", dest="port", help="Port to connect to DB")

    return parser.parse_args()
