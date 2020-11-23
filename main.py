# import anytree


def sum_distances(distances):
    return sum(distances)


def calculate_matrix_value(distance, total_distance_1, total_distance_2, length):
    return distance - ((total_distance_1 + total_distance_2) / length)


def modify_matrix(nodes, distances, distance_sums):
    if len(nodes) > 2:
        minimum_distance = 0
        minimum_node_1 = ''
        minimum_node_2 = ''
        i = 0
        for value in range(len(nodes)):
            j = 0
            for value in range(len(distances)):
                value = calculate_matrix_value(distances[i][j], distance_sums[i], distance_sums[j], len(nodes))
                if value < minimum_distance and distances[i][j] != 0:
                    minimum_distance = value
                    minimum_node_1 = nodes[i]
                    minimum_node_2 = nodes[j]
                j += 1
            i += 1
        return minimum_node_1, minimum_node_2
    else:
        return nodes[0], nodes[1]


def calculate_distance_to_node(distance, dist_sum_1, dist_sum_2, length):
    distance_1 = (float(distance) / 2) + ((dist_sum_1 - dist_sum_2) / float((2 * (length - 2))))
    distance_2 = distance - distance_1
    return distance_1, distance_2


def calculate_distance_from_node(distance_1, distance_2, distance_3):
    return (distance_1 + distance_2 - distance_3) / float(2)


def reassign_distances(distances, node_indices, node_1, node_2, dist_nodes, nodes):
    i = 0
    j = 0
    for distance in distances:
        if (nodes[i] not in [node_1, node_2]):
            del distance[node_indices[node_1]]
            del distance[node_indices[node_2] - 1]
            distance.append(dist_nodes[j])
            j += 1
        i += 1


def reassign_indices(nodes):
    node_indices = {}
    i = 0
    for node in nodes:
        node_indices[node] = i
        i += 1
    return node_indices


def main():
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    distances = [[0, 5, 4, 7, 6, 8], [5, 0, 7, 10, 9, 11], [4, 7, 0, 7, 6, 8], [7, 10, 7, 0, 5, 8], [6, 9, 6, 5, 0, 8],
                 [8, 11, 8, 8, 8, 0]]
    node_indices = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
    modified_matrix = []
    tree = []
    while (len(modified_matrix) != 1 and len(nodes) > 2):
        distance_sums = []
        i = 0
        for value in range(len(nodes)):
            distance_sums.append(sum_distances(distances[i]))
            i += 1

        node_1, node_2 = modify_matrix(nodes, distances, distance_sums)

        distance_1, distance_2 = calculate_distance_to_node(distances[node_indices[node_1]][node_indices[node_2]],
                                                            distance_sums[node_indices[node_1]],
                                                            distance_sums[node_indices[node_2]], len(nodes))

        dist_nodes = []
        for node in nodes:
            if node not in [node_1, node_2]:
                dist_nodes.append(calculate_distance_from_node(distances[node_indices[node_1]][node_indices[node]],
                                                               distances[node_indices[node]][node_indices[node_2]],
                                                               distances[node_indices[node_1]][node_indices[node_2]]))

        reassign_distances(distances, node_indices, node_1, node_2, dist_nodes, nodes)
        nodes.remove(node_1)
        nodes.remove(node_2)
        temp1 = distances[node_indices[node_1]]
        temp2 = distances[node_indices[node_2]]
        distances.remove(temp1)
        distances.remove(temp2)

        nodes.append(node_1 + node_2)
        dist_nodes.append(0)
        distances.append(dist_nodes)
        node_indices = reassign_indices(nodes)

        tree.append([node_1, node_1 + node_2, distance_1])
        tree.append([node_2, node_1 + node_2, distance_2])

    if len(nodes[0]) < len(nodes[1]):
        tree.append([nodes[0], nodes[0] + nodes[1], distances[0][1]])
        tree.append([nodes[1], nodes[0] + nodes[1], distances[0][0]])
    else:
        tree.append([nodes[0], nodes[0] + nodes[1], distances[0][0]])
        tree.append([nodes[1], nodes[0] + nodes[1], distances[0][1]])
    print(tree)


main()