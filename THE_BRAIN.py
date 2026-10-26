from math import *


# ok 1 thing you need to know is :

# or means at least 1,and means both,nand means not both,and xor means both are different

# this is the place for me to learn ML , neural networks , etc.

# we'll be using this later in the code.

# also fyi this guy squishes AAANNNNYYY number to a number from 1-0 which is useful :)
def sigmoid(x):
    return 1 / (1 + exp(-x))


# neuron1 (noob).

# this guy stinks cuz he needs weights and biases from us and gives back only 1 or 0.

def neuron1(inputs=None, weights=None, bias=None):
    if inputs is None:
        inputs = input("inputs : ").replace(",", " ").split()
        inputs = list(map(float, inputs))
    if weights is None:
        weights = input("weights : ").replace(",", " ").split()
        weights = list(map(float, weights))
    if bias is None:
        bias = float(input("bias : "))
    total = 0
    for i in range(len(inputs)):
        check = inputs[i] * weights[i]
        total += check
    if total + bias > 0:
        return 1
    else:
        return 0


# neuron1 (sensei).

# now this guy can help lil tinny neuron1 to figure out its own weights and biases.

games = {
    "and": [([0, 0], 0), ([0, 1], 0), ([1, 0], 0), ([1, 1], 1)],
    "or": [([0, 0], 0), ([0, 1], 1), ([1, 0], 1), ([1, 1], 1)],
    "nand": [([0, 0], 1), ([0, 1], 1), ([1, 0], 1), ([1, 1], 0)],
}


def train1(data=None, epochs=20, rate=0.1):
    if data is None:
        while True:
            game = input("game --> and/or/nand : ").lower().strip()
            if game in games:
                data = games[game]
                break
            else:
                print("wrong input : ")
    weights = [0] * len(data[0][0])
    bias = 0
    for i in range(1, epochs + 1):
        for inputs, answer in data:
            guess = neuron1(inputs=inputs, weights=weights, bias=bias)
            if guess != answer:
                error = answer - guess
                for j in range(len(weights)):
                    weights[j] += rate * error * inputs[j]
                bias += rate * error
    return weights, bias


# newer and better neuron1 AKA neuron2 (also noob ... for now ...).

# also this guy is a one man(/neuron lol) network.

# also this guy uses the sigmoid thing at the top so he's cool and doesn't stick to 1 or 0.

def neuron2(inputs=None, weights=None, bias=None):
    if inputs is None:
        inputs = input("inputs : ").replace(",", " ").split()
        inputs = list(map(float, inputs))
    if weights is None:
        weights = input("weights : ").replace(",", " ").split()
        weights = list(map(float, weights))
    if bias is None:
        bias = float(input("bias : "))
    total = 0
    for i in range(len(inputs)):
        check = inputs[i] * weights[i]
        total += check
    return sigmoid(total + bias)


# OMG GUYS THE NEURON NETWORK IS OUT , featuring the brand new neuron2(yes it's also noob ... for now ...).

# this guy can tell if 2 inputs aren't the same / they're different or not thus the name xor.

def xor_net(a=None, b=None):
    if a is None:
        a = float(input("a : "))
    if b is None:
        b = float(input("b : "))
    h1 = neuron2(inputs=[a, b], weights=[-20, -20], bias=30)
    h2 = neuron2(inputs=[a, b], weights=[20, 20], bias=-10)
    return neuron2(inputs=[h1, h2], weights=[20, 20], bias=-30)


# who's he you ask huh he's the club's security guard.only club members allowed.

# for the nerdy people , this guy only plays this program if you run this file directly which is useful if I ever import mr.big_chungus here.

if __name__ == "__main__":
    while True:
        try:
            func = int(input("function no. : "))
        except ValueError:
            print("input a non-decimal-point-positve_number : ")
            continue
        funcs = {
            1: train1,
            2: xor_net, }
        if func in funcs:
            print(funcs[func]())
            break
        else:
            print("wrong input : ")

# you say you're bored huh well here's a joke, what's the blood type of good people ... B-POSITIVE.
