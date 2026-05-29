import click

from engine import peace_parser


@click.command()
@click.argument("input")
def main(input: str):
    with open(input, "r") as f:
        file_content = f.read()

    result = peace_parser.parse_peace(file_content)
    print(result)


if __name__ == "__main__":
    main()
