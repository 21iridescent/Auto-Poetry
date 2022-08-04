import jionlp as jio
xiehouyu_list = jio.xiehouyu_loader()
print(type(xiehouyu_list))
chinese_idioms = jio.chinese_idiom_loader()
world_location = jio.world_location_loader()
#print(world_location['亚洲'])
china_location = jio.china_location_loader()

import random
key = random.choice(list(world_location.keys()))
key_chinese_idioms = random.choice(list(chinese_idioms.keys()))
#print(key)
#print(key_chinese_idioms)
#value = dict_list.get(key)

def get_random_idioms():
    return  random.choice(list(chinese_idioms.keys()))

def get_batch_idioms():
    list_batch = list(chinese_idioms.keys())
    idioms = random.sample(list_batch, random.randint(20, 30))
    idioms = " ".join(idioms)
    return  idioms

def get_random_loc():
    return random.choice(list(flated_location_list))

def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

a = {'a': {1: {1: 2, 3: 4}, 2: {5: 6}}}

location_list = []

for key, value in recursive_items(world_location):
    location_list.append(value)
flated_location_list = []

for i in location_list:
    #rint(type(i))
    if (type(i).__name__=='list'):
        for j in i:
            flated_location_list.append(j)
    else:
        flated_location_list.append(i)

#print(flated_location_list)

text = get_random_idioms()
text2 = get_random_loc()

print(text)
print(text2)

k = get_batch_idioms()
print(k)