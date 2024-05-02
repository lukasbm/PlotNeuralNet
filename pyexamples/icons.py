import sys

sys.path.append('../')
from pycore.tikz import *

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    to_Sum("icon", radius=2.5, opacity=1.0, logo="\mu"),
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
