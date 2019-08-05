import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--app-name", default="power-bi-client", dest="appName", help="Power BI Client side app name.")
    parser.add_argument("--api-name", default="power-bi-api", dest="apiName", help="Power BI server side api app name.")

    return parser.parse_args()
