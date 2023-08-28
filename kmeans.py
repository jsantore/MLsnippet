import math
import random
import readData


def pick_centroids(k: int, data: list[tuple]) -> list[tuple]:
    centroids = []
    i = 0
    while i < k:
        ith_centroid = (random.choice(data))
        if ith_centroid in centroids:
            continue
        centroids.append(ith_centroid)
        i += 1
    return centroids


def assign_cluster(data: list[tuple], k: int) -> list[list]:
    clusters = []
    for i in range(k):  # start out with k empty clusters
        clusters.append([])
    for data_item in data:
        cluster_assigned: list = random.choice(clusters)
        cluster_assigned.append(data_item)
    return clusters


def assignment_step(clusters: list[list], centroids: list[tuple]):
    print("assignment step")
    done = True  # k-means assumes we are done unless we need to move an observation
    for cluster in clusters:
        for observation in cluster:
            nearest_centroid_index = find_nearest_cluster(observation, centroids)
            if not nearest_centroid_index == clusters.index(cluster):
                cluster.remove(observation)
                clusters[nearest_centroid_index].append(observation)
                done = False
    return done


def update_centroids(clusters: list[list]) -> list[tuple]:
    new_centroids = []
    for cluster in clusters:
        github_sum = 0
        stackoverflow_sum = 0
        for observation in cluster:
            github_sum+=observation[2]
            stackoverflow_sum += observation[1]
        centroid = ("New Centroid", stackoverflow_sum/len(cluster),
                    github_sum/len(cluster))
        new_centroids.append(centroid)
    return new_centroids



def find_nearest_cluster(observation: tuple, centroids: list[tuple]) -> int:
    closest = centroids[0]
    for centroid in centroids:
        # use euclidean distance as distance metric
        current_dist = math.sqrt(pow(observation[1] - centroid[1], 2) +
                                 pow(observation[2] - centroid[2], 2))
        closest_dist = math.sqrt(pow(observation[1] - closest[1], 2) +
                                 pow(observation[2] - closest[2], 2))
        if current_dist < closest_dist:
            closest = centroid
    return centroids.index(closest)


def kmeans(dataset: list[tuple], k: int) -> list[list]:
    # initialize
    centroids = pick_centroids(k, dataset)
    clusters = assign_cluster(dataset, k)
    done = False
    while True:
        done = assignment_step(clusters, centroids)
        if done:
            break
        update_centroids(clusters)
    return clusters


def main():
    dataset = readData.read_data("data.txt")
    clusters = kmeans(dataset, 4)
    for cluster in clusters:
        print("Begin cluster++++++++++++++++++++++++++++++++")
        for language in cluster:
            print(language[0])
        print("====================================End cluster")
        print()


if __name__ == '__main__':
    main()
