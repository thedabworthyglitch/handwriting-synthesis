import numpy as np
from handwriting_synthesis import Hand
import random
from textwrap import wrap

styles = []
biases = []
lines = []

stbi = {
    0: [.9,.7,1.0],
    1: [.4,1.05],
    3: [.65,.9],
    4: [.9],
    7: [.9],
    8: [.9],
    9: [.75,.8,.9,1.0,1.05],
    12: [.75,.9,1],
}


def splitter(text, max_length = 90):
    lines = []
    line = ""
    for line in text.split("\n"):
        wr = wrap(line, max_length)
        if wr == []:
            lines.append("")
        else:
            lines.extend(wr)
    return lines
arr_splitter = lambda arr, size: [arr[x:x+size] for x in range(0, len(arr), size)]
linesPerPage = 40

if __name__ == '__main__':
    hand = Hand()
    lines = splitter(open('towrite.txt').read())
    # usage demo
    # stroke_widths = [random.choice([1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5])] * len(lines)

    for i in stbi:
        for j in stbi[i]:
            print(f"==========================================================================================")
            print(f"Style: {i}, Bias: {j}")
            print(f"==========================================================================================")
            stroke_width = random.choice([1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5])
            lines_sp = arr_splitter(lines, linesPerPage)
            for k, line_pg in enumerate(lines_sp):
                hand.write(
                    filename=f'img/usage_demo_st{i}_bias{j}-pg{k}.svg',
                    lines=line_pg,
                    biases=[j] * len(line_pg),
                    styles=[i] * len(line_pg),
                    stroke_widths=[stroke_width + random.choice([-0.1, -0.05, 0, 0.05, 0.1]) for _ in range(len(lines))],
                    alignCenter=False
                )