import os
import random
from .cowsay import cowsay


def main():
    '''Chuck Norris would be ashamed of this Docstring.'''

    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_dir}/assets/curated_facts', 'r') as file:
        facts = file.read().splitlines()
        random_fact = random.choice(facts)
        print(cowsay(random_fact))


if __name__ == '__main__':
    main()
