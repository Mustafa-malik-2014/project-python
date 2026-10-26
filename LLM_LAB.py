# this is main

import random


# this is where I'll be learning machine learning and AI.

# lab 1 : this guy is the OG the ORIGINAL the GRAMPS and he can learn the next word of a sentence ( IDK the accuracy ).

def learn_next_word(text=None):
    if text is None:
        text = input("text : ")
    text = text.lower().split()
    learnings = {}
    previous = None
    for i in text:
        i = i.strip("'',.;:\"!?<>()1234567890-_[]{}=+#$%^&*\\|/`~")
        if i == "" or i == " ":
            continue
        if previous is not None:
            if previous not in learnings:
                learnings[previous] = {}
            if i not in learnings[previous]:
                learnings[previous][i] = 1
            elif i in learnings[previous]:
                learnings[previous][i] += 1
        previous = i
    return learnings


# lab 2 : this guy is him. just believe me.

def predict_next(model=None, word=None, training_data=None):
    if training_data is None:
        training_data = input("training data : ")
    if model is None:
        model = learn_next_word(text=training_data)
    if word is None:
        word = input("word : ")
    word = word.lower()
    if word not in model:
        return None
    full_stop = random.choices([True, False], weights=[0.05, 0.95])[0]
    if full_stop:
        return "."
    best = 0
    best_words = []
    for i in model[word]:
        if model[word][i] > best:
            best = model[word][i]
            best_words = [i]
        elif model[word][i] == best:
            best_words.append(i)
    return random.choice(best_words)


# lab 3 : this guy uses lab 2 ( and lab 2 uses lab 1 ) to make sentence through teamwork.

# noinspection unsupported-operator
def sentence_generator(seed_word=None, training_data=None):
    if seed_word is None:
        seed_word = input("seed word : ")
    if training_data is None:
        training_data = input("training data : ")
    memory = []
    model = learn_next_word(text=training_data)
    cap = 1
    sentence = seed_word
    while True:
        if seed_word.lower() not in model:
            seed_word = input("seed word : ")
            continue
        else:
            memory.append(seed_word)
            break
    while True:
        word = predict_next(word=seed_word, training_data=training_data, model=model)
        if word is None:
            return seed_word + "."
        else:
            memory.append(word)
            break
    sentence += " " + word
    while True:
        word2 = predict_next(word=memory[-1], training_data=training_data, model=model)
        if word2 is None:
            return sentence
        else:
            if word2 not in memory and word2 != ".":
                sentence += " " + word2
                cap += 1
                if len(memory) < 5:
                    memory.append(word2)
                else:
                    del memory[0]
                    memory.append(word2)
            elif word2 == ".":
                sentence += word2
                if len(memory) < 5:
                    memory.append(word2)
                else:
                    del memory[0]
                    memory.append(word2)
                return sentence
            elif word2 in memory and len(model[memory[-1]]) == 1:
                sentence += " " + word2
                cap += 1
                if len(memory) < 5:
                    memory.append(word2)
                else:
                    del memory[0]
                    memory.append(word2)
        if cap == 10:
            sentence += "."
            return sentence


# lab 4 : ok this guy is the BEGINNING of shakespear just believe me.

def learn_next_2(text=None):
    if text is None:
        text = input("text : ")
    text = text.replace("\u2014", " ")
    text = text.lower().split()
    learnings = {}
    previous1 = None
    previous2 = None
    for i in text:
        i = i.strip("'',.;:\"!?<>()1234567890-_[]{}=+#$%^&*\\|/`~\u201c\u201d\u2018\u2019\u2014")
        if i == "" or i == " ":
            continue
        if previous1 is not None and previous2 is not None:
            if (previous2, previous1) not in learnings:
                learnings[previous2, previous1] = {}
            if i not in learnings[previous2, previous1]:
                learnings[previous2, previous1][i] = 1
            elif i in learnings[previous2, previous1]:
                learnings[previous2, previous1][i] += 1
        previous2 = previous1
        previous1 = i
    return learnings


# lab 5 : this is leading somewhere just believe me.

def predict_next_2(model=None, word1=None, word2=None, training_data=None):
    if training_data is None:
        training_data = input("training data : ")
    if model is None:
        model = learn_next_2(text=training_data)
    if word1 is None:
        word1 = input("word1 : ")
    if word2 is None:
        word2 = input("word2 : ")
    word1 = word1.lower()
    word2 = word2.lower()
    if (word1, word2) not in model:
        return None
    full_stop = random.choices([True, False], weights=[0.05, 0.95])[0]
    if full_stop:
        return "."
    best = 0
    best_words = []
    for i in model[word1, word2]:
        if model[word1, word2][i] > best:
            best = model[word1, word2][i]
            best_words = [i]
        elif model[word1, word2][i] == best:
            best_words.append(i)
    return random.choice(best_words)


# ok this one is sentence generator's older cousin ,and he's better cuz he looks back MORE.

# apparently he's considered an NLP AI , so I'll name him Lexicon

# noinspection unsupported-operator
def sentence_generator_2(seed_word1=None, seed_word2=None, training_data=None):
    if seed_word1 is None:
        seed_word1 = input("seed word1 : ")
    if seed_word2 is None:
        seed_word2 = input("seed word2 : ")
    if training_data is None:
        training_data = input("training data : ")
    model = learn_next_2(text=training_data)
    memory = []
    cap = 2
    sentence = seed_word1 + " " + seed_word2
    print("hi I'm Lexicon want a banger ? here ya go ! \n")
    while True:
        if (seed_word1.lower(), seed_word2.lower()) not in model:
            seed_word1 = input("seed word1 : ")
            seed_word2 = input("seed word2 : ")
            continue
        else:
            memory.append(seed_word1)
            memory.append(seed_word2)
            break
    while True:
        word = predict_next_2(word1=memory[-2], word2=memory[-1], model=model, training_data=training_data)
        if word is None:
            return sentence + "."
        else:
            if word == ".":
                return sentence + "."
            elif word in memory:
                continue
            else:
                if len(memory) < 5:
                    memory.append(word)
                    sentence += " " + word
                    cap += 1
                else:
                    del memory[0]
                    memory.append(word)
                    sentence += " " + word
                    cap += 1

        if cap == 10:
            return sentence + "."


if __name__ == "__main__":
    while True:
        try:
            func = int(input("function no. : "))
        except ValueError:
            print("input a number : ")
            continue
        funcs = {1: sentence_generator,
                 2: sentence_generator_2}
        if func in funcs:
            print(funcs[func]())
            break
        else:
            print("wrong input : ")
