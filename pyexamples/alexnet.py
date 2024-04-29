import sys

sys.path.append('../')
from pycore.tikz import *

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    to_Conv("conv1", offset="(0,0,0)", to="(0,0,0)", height=24, depth=24, width=2),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)", height=18, depth=18, width=2),
    to_Conv("conv2", offset="(0,0,0)", to="(pool1-east)", height=18, depth=18, width=4),
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=12, depth=12, width=4),
    to_Conv("conv3", offset="(0,0,0)", to="(pool2-east)", height=12, depth=12, width=6),
    to_Conv("conv4", offset="(0,0,0)", to="(conv3-east)", height=12, depth=12, width=6),
    to_Conv("conv5", offset="(0,0,0)", to="(conv4-east)", height=12, depth=12, width=6),
    to_Pool("pool3", offset="(0,0,0)", to="(conv5-east)", height=5, depth=5, width=6),
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
