import sys

sys.path.append('../')
from pycore.tikz import *

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    to_Conv("conv1", offset="(0,0,0)", to="(0,0,0)", height=24, depth=32, width=2),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)", height=18, depth=14, width=2),
    to_Conv("conv2", offset="(0,0,0)", to="(pool1-east)", height=14, depth=12, width=3),
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=10, depth=10, width=3),
    to_Conv("conv3", offset="(0,0,0)", to="(pool2-east)", height=8, depth=8, width=4),
    to_Conv("conv4", offset="(0,0,0)", to="(conv3-east)", height=8, depth=8, width=4),
    to_Conv("conv5", offset="(0,0,0)", to="(conv4-east)", height=4, depth=4, width=8),
    to_Pool("pool3", offset="(0,0,0)", to="(conv5-east)", height=2, depth=2, width=8),
    to_Pool("pool4", offset="(0,0,0)", to="(pool3-east)", height=1, depth=1, width=8),
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
