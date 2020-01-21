
def earliest_ancestor(ancestors, starting_node):
    # Define a list that will hold all possible earliest ancestors
    possible_anc = []
    # Using recursion, we will search
    def recur_anc(node, counter = 0):
        # Create a list of all parent child relationships for the
        # given node where the node is the child
        node_rels = [rel for rel in ancestors if rel[1] == node]
        # If the node has no parents
        if node_rels == [] and counter > 0:
            # Append the node and the amount of recursions to keep
            # track of how far back we went to find said node
            possible_anc.append([node, counter])
            return
        # If no parents were found, and we haven't gone back any steps
        # the starting node has no parents so we want to return -1
        elif node_rels == [] and counter == 0:
            possible_anc.append([-1, 0])
            return
        # Otherwise, the node has parents so we want to check each of them
        # as well, and increase the counter to keep track of how far back
        # we have gone
        else:
            for rel in node_rels:
                parent = rel[0]
                counter += 1
                return recur_anc(parent, counter)
    # Call our recursive function on the starting node
    recur_anc(starting_node)
    # Using the variable "earliest", loop over the possible earliest ancestors
    # list and find the one with the highest counter attached. This will give us
    # the ancestor that is furthest back.
    earliest = None
    if possible_anc:
        # Start earliest at the first index
        earliest = possible_anc[0]
    else:
        # If list is empty throw an error
        return print("Error finding possible ancestors")
    for anc in possible_anc:
        if anc[1] > earliest[1]:
            earliest = anc
    # Return the earliest node
    return earliest[0]