import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add the users to the db
        for i in range(num_users):
            self.add_user(F"User {i + 1}")
        # Declare a list to hold all possible friendship combinations
        possible_friends = []
        # Find all possible friendships for each user
        for user_id in self.users:
            # This range avoids duplicate friendships by making sure the first id is
            # smaller than the second id
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friends.append((user_id, friend_id))
        # Shuffle the combos and select the first n friends to add where n is the avg number of friends
        random.shuffle(possible_friends)
        # Get the number of total number of friendships, and then divide by two since technically 2 are
        # created by add_friendship
        total_friendships = num_users * avg_friendships // 2
        for i in range(total_friendships):
            friendship = possible_friends[i]
            self.add_friendship(friendship[0], friendship[1])



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # Implement a BFT and store the paths as we go
        # When an unvisited node is reached, add the path to the visited dictionary
        q = Queue()
        q.enqueue([user_id])
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                # We can do this here so that the path won't overwrite the short paths
                # already in the visited dictionary
                visited[v] = path
                for f in self.friendships[v]:
                    new_path = [*path]
                    new_path.append(f)
                    q.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
