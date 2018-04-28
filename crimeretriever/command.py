from argparse import ArgumentParser


def process():
    print("Processing commands")
    parser = ArgumentParser(description="London Crime Retriever Parser")
    parser.add_argument('action')
    parser.add_argument('--parameter', '-p', type=int)

    arguments = parser.parse_args()

    action = arguments.action
    parameter = arguments.parameter

    print(action)
    print(parameter)


if __name__ == "__main__":
    process()