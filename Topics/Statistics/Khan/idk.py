import numpy as np
import pandas as pd
from collections import Counter
from emoji import EMOJI_DATA
import random

### Unit 1

## Lesson 1

# Pictographs

def get_emojis():
    return [emoji for emoji in EMOJI_DATA.keys() if len(emoji) < 5]

def get_random_emoji():
    emojis = get_emojis()
    boundary = len(emojis)-1
    return emojis[random.randint(0,boundary)]

def pictograph_key():
    emoji = get_random_emoji()
    val = random.randint(1,5)

    return emoji, val

def generate_pictograph_data():
    emoji, factor = pictograph_key()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    num_groups = random.randint(3,5)
    group_data = [random.randint(0,10) * factor for i in np.arange(num_groups)]
    groups = [''] * num_groups
    # I should do a while loop
    for i in np.arange(num_groups):
        letter = letters[random.randint(0,25)]
        if letter in groups:
            i -= 1
        groups[i] = letter
    return group_data, groups, emoji, factor

# Measures of Central Tendency

def _midrange(_list):
    return np.mean([np.max(_list), np.min(_list)])

def _range(_list):
    return np.max(_list) - np.min(_list)

def _mode(_list):
    counter = Counter(_list)
    counts = list(counter.values())

    # Can return early to forgo any further computation
    if np.all(counts == counts[0]):
        return 'There is no mode'

    max_count = np.max(counts)
    # There can be more than one mode
    mode_items = [k for k,v in counter.items() if v == max_count]
    return f'The mode of the dataset is/are: {mode_items}'

# Bar Graphs

# Venn Diagrams

# Two way tables / Two way relative frequency tables

def generate_random_data(n):
    categories = [''] * n
    cat_1_out = [0] * n
    cat_2_out = [0] * n
    for i in np.arange(n):
        if random.randint(0,1) == 0:
            categories[i] = 'category 1'
        else:
            categories[i] = 'category 2'

        if random.randint(0,1) == 0:
            cat_1_out[i] = 1
        else:
            cat_1_out[i] = 0

        if random.randint(0,1) == 0:
            cat_2_out[i] = 1
        else:
            cat_2_out[i] = 0
    
    return pd.DataFrame({'Category': categories, 'Cat 1': cat_1_out, 'Cat 2': cat_2_out})

# Data types:

def generate_random_data_type():
    rand = random.randint(0,3)

    if rand == 0: # Integer
        return {'type': 'Integer', 'data': [random.randint(0,10) for r in np.arange(10)]}
    elif rand == 1: # Float
        return {'type': 'Float', 'data': [random.randint(0,10) / random.randint(1,10) for r in np.arange(10)]}
    elif rand == 2: # Nominal
        nominal_data = {
            'cars': [
                'Camaro',
                'Porche',
                'Ferrari'
            ],
            'planes': [
                'Jet',
                'Biplane',
                'Paper'
            ]
        }
        nominal_items = list(nominal_data.keys())
        num_items = len(nominal_items)
        return {'type': 'Nominal', 'data': nominal_data[nominal_items[random.randint(0,num_items - 1)]]}
    elif rand == 3: # Ordinal
        ordinal_data = {
            'years': [
                2000,
                2001,
                2002
            ],
            'place': [
                '1st',
                '2nd',
                '3rd'
            ]
        }
        ordinal_items = list(ordinal_data.keys())
        num_items = len(ordinal_items)
        return {'type': 'Ordinal', 'data': ordinal_data[ordinal_items[random.randint(0,num_items - 1)]]}

print(generate_random_data(10))
print([0]*3)
generate_random_data_type()