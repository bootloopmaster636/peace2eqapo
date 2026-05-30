import click
from loguru import logger

from engine import apo_generator, peace_parser


@click.command()
@click.argument("input")
@click.argument("output")
def main(input: str, output: str):
    try:
        with open(input, "r") as f:
            file_content = f.read()

        parser_result = peace_parser.parse_peace(file_content)
        eqapo_result = apo_generator.generate_apo(parser_result)

        with open(output, "w") as f:
            f.write("\n".join(eqapo_result))

        logger.info(f"The result file has been written to {output}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
