
import sys
sys.path.append('../')
from aicmder import import_parent
import_parent(__file__)
from pathlib import Path
from pycore.blocks import *
from pycore.tikzeng import *
import pycore
from aicmder.utils import WorkingDirectory

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    to_Conv("conv1", '', '', offset="(0,-5,0)", to="(0,0,0)", height=64, depth=64, width=2, caption="Conv1"),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    to_Conv("conv2", '', '', offset="(4,0,0)", to="(pool1-east)", height=32, depth=32, width=2, caption="Conv2"),
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
    to_connection("pool1", "conv2"),
    to_Node(name="dot", offset="(2.5,0,0)", to="(pool2-east)", radius=1.8,
            opacity=0.8, logo="...", caption="Othter Layers", fill="\GreyColor"),
    to_connection("pool2", "dot"),
    to_SoftMax("soft1", 10, "(2.5,0,0)", "(dot-east)", caption="softmax2"),
    to_connection("dot", "soft1"), 


    to_Conv("siamese_conv1", '', '', offset="(0,5,0)", to="(0,5,0)", height=64, depth=64, width=2, caption="Conv1"),
    to_Pool("siamese_pool1", offset="(0,0,0)", to="(siamese_conv1-east)"),
    to_Conv("siamese_conv2", '', '', offset="(4,0,0)", to="(siamese_pool1-east)", height=32, depth=32, width=2, caption="Conv2"),
    to_Pool("siamese_pool2", offset="(0,0,0)", to="(siamese_conv2-east)", height=28, depth=28, width=1),
    to_connection("siamese_pool1", "siamese_conv2"),
    to_Node(name="siamese_dot", offset="(2.5,0,0)", to="(siamese_pool2-east)", radius=1.8,
            opacity=0.8, logo="\cdots", caption="Othter Layers", fill="\GreyColor"),
    to_connection("siamese_pool2", "siamese_dot"),
    to_SoftMax("siamese_soft1", 10, "(2.5,0,0)", "(siamese_dot-east)", caption="softmax1"),
    to_connection("siamese_dot", "siamese_soft1"),

    # to_skip("siamese_pool1", "siamese_soft1"),

    to_Node(name="max", offset="(2.5,7.5,0)", to="(soft1-east)", radius=3,
            opacity=0.8, logo="\max", caption="All Max"), 
    
    to_connection_triangle("siamese_soft1", "max"),
    to_connection_triangle("soft1", "max", dest="south"),

    # to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
    # to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
    # to_connection("pool2", "soft1"),
    # to_Sum("sum1", offset="(1.5,0,0)", to="(soft1-east)", radius=2.5, opacity=0.6),
    # to_connection("soft1", "sum1"),
    to_end()
]

# Settings
FILE = Path(__file__).resolve()
# print(FILE, __file__, FILE.parents[0])
ROOT = FILE.parents[0]


@WorkingDirectory(ROOT)
def main():
    # namefile = str(sys.argv[0]).split('.')[0]
    namefile = "test"
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
