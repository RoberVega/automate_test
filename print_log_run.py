import argparse

parser = argparse.ArgumentParser(description="Adds information on the run")

parser.add_argument('pull_request_tag',
                    metavar="pull_request_tag",
                    type=str,
                    help="Enter the tag of the pull request")
args = parser.parse_args()

pull_request_tag = args.pull_request_tag

if __name__ == "__main__":
    print(pull_request_tag)