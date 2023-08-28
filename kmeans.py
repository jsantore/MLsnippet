import random


def pick_centroids(k:int)->list[tuple]:
    centroids = []
    for i in range(k):
        name = f"centroid {i}"
        stackoverflow = random.randint(100000, 999000)
        github = random.randint(100000, 999000)
        ith_centroid = (name, stackoverflow, github)
        centroids.append(ith_centroid)
    return centroids

def main():
    random_centroids = pick_centroids(4)


if __name__ == '__main__':
    main()