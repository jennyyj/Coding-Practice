# p3_jacob_jenny.py

import csv

def add_user(sn: dict, username: str, fullname: str) -> bool:
    
    try:
        if username in sn:
            print(f"Error: User '{username}' already exists.")
            return False
        sn[username] = (fullname, [])
        return True
    except Exception as e:
        print(f"Error adding user: {e}")
        raise

def add_friend(sn: dict, user1: str, user2: str) -> bool:
    
    try:
        if user1 not in sn or user2 not in sn:
            print("Error: One or both users not found.")
            return False
        sn[user1][1].append(user2)
        sn[user2][1].append(user1)
        return True
    except Exception as e:
        print(f"Error adding friend: {e}")
        raise

def get_friends(sn: dict, user1: str, distance: int) -> list:
    
    try:
        if user1 not in sn or distance < 1:
            print("Error: Invalid username or distance.")
            return []

        visited = set()
        friends = set(sn[user1][1])

        for _ in range(distance - 1):
            new_friends = set()
            for friend in friends:
                if friend not in visited:
                    visited.add(friend)
                    new_friends.update(sn[friend][1])
            friends = new_friends

        return list(friends)
    except Exception as e:
        print(f"Error getting friends: {e}")
        raise

def save_network(filename: str, sn: dict) -> None:
    
    try:
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for username, (fullname, friends) in sn.items():
                csvwriter.writerow([username, fullname] + friends)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        raise
    except Exception as e:
        print(f"Error saving network: {e}")
        raise

def load_network(filename: str) -> dict:
    
    try:
        sn = {}
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                username = row[0]
                fullname = row[1]
                friends = row[2:]
                sn[username] = (fullname, friends)
        return sn
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        raise
    except Exception as e:
        print(f"Error loading network: {e}")
        raise

def main():
    try:
        social_network = {'alice': ('Alice Smith', ['maria']),
                          'maria': ('Maria Cortez', ['alice', 'joe', 'david']),
                          'joe': ('Joseph Adams', ['maria', 'eve']),
                          'eve': ('Evelyn Cooper', ['joe']),
                          'david': ('David Benson', ['maria'])}

        print("Initial Social Network:")
        print(social_network)

        # a) Test add_user function
        add_user(social_network, 'bob', 'Bob Johnson')

        # b) Test add_friend function
        add_friend(social_network, 'bob', 'maria')

        # c) Test get_friends function
        print("Friends of 'alice' at distance 2:", get_friends(social_network, 'alice', 2))

        # d) Test save_network and load_network functions
        save_network('social_network.csv', social_network)
        loaded_network = load_network('social_network.csv')
        print("Loaded Social Network:")
        print(loaded_network)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


