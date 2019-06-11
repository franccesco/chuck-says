import os
import click
import random
from .cowsay import cowsay


@click.command()
@click.option('-n', '--no-cow', is_flag=True, help='Output not wrapped by cowsay.')
def main(no_cow):
    '''Chuck Norris would be ashamed of this Docstring.'''

    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_dir}/assets/curated_facts', 'r') as facts_file:
        facts_list = facts_file.read().splitlines()
        random_fact = random.choice(facts_list)
    print(random_fact) if no_cow else print(cowsay(random_fact))


if __name__ == '__main__':
    main(None)
