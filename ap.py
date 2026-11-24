users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"},
    {"name": "David"},
    {"name": "Eve", "role": "moderator"}
]


""" for user in users: 
    if not "role" in user:
        if user ["role"] == "admin":
            print(user) """

for user in users: 
    try:
        if user ["role"] == "admin":
            print(user)
    except KeyError:
        continue