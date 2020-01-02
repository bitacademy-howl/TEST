from tqdm import tqdm

x = []

for i in tqdm(range(10000)):
    for j in range(10000):
        x.append(i)