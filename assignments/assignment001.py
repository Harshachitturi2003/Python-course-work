# ====================================================
# WHATSAPP CHAT ANALYZER
# ====================================================

# -----------------------------
# Helper: Parse message to user and text
# -----------------------------
def parse_message(msg):
    if ":" not in msg:
        return None, msg
    user, text = msg.split(":", 1)
    return user.strip(), text.strip()


# ====================================================
# ANALYSIS FUNCTIONS
# ====================================================

def total_messages(messages):
    return len(messages)


def unique_users(messages):
    users = {parse_message(m)[0] for m in messages}
    return users


def total_words(messages):
    return sum(len(parse_message(m)[1].split()) for m in messages)


def average_words_per_message(messages):
    if not messages:
        return 0
    return total_words(messages) / len(messages)


def longest_message(messages):
    return max(messages, key=lambda m: len(parse_message(m)[1]))


def most_active_user(messages):
    from collections import Counter
    users = [parse_message(m)[0] for m in messages]
    count = Counter(users)
    user, msg_count = count.most_common(1)[0]
    return user, msg_count


def user_message_count(messages, username):
    return sum(1 for m in messages if parse_message(m)[0].lower() == username.lower())


def most_frequent_word_by_user(messages, username):
    from collections import Counter
    words = []
    for m in messages:
        user, text = parse_message(m)
        if user.lower() == username.lower():
            words.extend(text.lower().split())
    if not words:
        return None
    return Counter(words).most_common(1)[0][0]


def first_last_message_by_user(messages, username):
    user_msgs = [m for m in messages if parse_message(m)[0].lower() == username.lower()]
    if not user_msgs:
        return None, None
    return user_msgs[0], user_msgs[-1]


def user_present(messages, username):
    return username in unique_users(messages)


def commonly_repeated_words(messages):
    from collections import Counter
    all_words = []
    for m in messages:
        all_words.extend(parse_message(m)[1].lower().split())
    freq = Counter(all_words)
    return {w for w, c in freq.items() if c > 1}


def longest_avg_message_user(messages):
    from collections import defaultdict
    word_count = defaultdict(list)

    for m in messages:
        user, text = parse_message(m)
        word_count[user].append(len(text.split()))

    avg_lengths = {u: sum(w)/len(w) for u, w in word_count.items()}
    user = max(avg_lengths, key=avg_lengths.get)
    return user, avg_lengths[user]


def messages_mentioning_user(messages, username):
    username = username.lower()
    return sum(1 for m in messages if username in parse_message(m)[1].lower())


def remove_duplicate_messages(messages):
    unique = list(dict.fromkeys(messages))
    return unique


def sort_messages(messages):
    return sorted(messages)


def extract_questions(messages):
    return [m for m in messages if "?" in parse_message(m)[1]]


def reply_ratio(messages, user1, user2):
    """
    Count how many times user2 messages immediately follow user1's.
    """
    count = 0
    for i in range(len(messages) - 1):
        u1, _ = parse_message(messages[i])
        u2, _ = parse_message(messages[i + 1])
        if u1.lower() == user1.lower() and u2.lower() == user2.lower():
            count += 1
    return count


def deleted_messages_count(messages):
    return sum(1 for m in messages if parse_message(m)[1] == "This message was deleted")


# ====================================================
# MAIN PROGRAM
# ====================================================

print("=== WhatsApp Chat Analyzer ===")

n = int(input("Enter the number of messages: "))
messages = [input() for _ in range(n)]

# Menu
while True:
    print("\nChoose analysis option:")
    print("""
1. Count total messages
2. Identify unique users
3. Count total words
4. Average words per message
5. Find longest message
6. Most active user
7. Message count for a specific user
8. Most frequent word by user
9. First and last message by user
10. Check if user is present
11. Common repeated words
13. User with longest avg message length
14. Count messages mentioning a user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract questions
18. Reply ratio between two users
19. Check for deleted messages
20. Exit
""")

    choice = int(input("Enter option number: "))

    if choice == 1:
        print("Total messages:", total_messages(messages))

    elif choice == 2:
        print("Unique users:", unique_users(messages))

    elif choice == 3:
        print("Total words:", total_words(messages))

    elif choice == 4:
        print("Average words per message:", round(average_words_per_message(messages), 2))

    elif choice == 5:
        print("Longest message:", longest_message(messages))

    elif choice == 6:
        user, count = most_active_user(messages)
        print(f"Most active user: {user} ({count} messages)")

    elif choice == 7:
        u = input("Enter username: ")
        print(f"Messages sent by {u}: {user_message_count(messages, u)}")

    elif choice == 8:
        u = input("Enter username: ")
        print("Most frequent word:", most_frequent_word_by_user(messages, u))

    elif choice == 9:
        u = input("Enter username: ")
        f, l = first_last_message_by_user(messages, u)
        print("First:", f)
        print("Last:", l)

    elif choice == 10:
        u = input("Enter username: ")
        if user_present(messages, u):
            print(f"User '{u}' is present.")
        else:
            print(f"User '{u}' not found in chat.")

    elif choice == 11:
        print("Common repeated words:", commonly_repeated_words(messages))

    elif choice == 13:
        user, avg = longest_avg_message_user(messages)
        print(f"User with longest average message: {user} ({avg} words)")

    elif choice == 14:
        u = input("Enter username: ")
        print(f"Messages mentioning '{u}':", messages_mentioning_user(messages, u))

    elif choice == 15:
        unique = remove_duplicate_messages(messages)
        print("Unique message count:", len(unique))
        print("\n".join(unique))

    elif choice == 16:
        print("Sorted messages:")
        print("\n".join(sort_messages(messages)))

    elif choice == 17:
        print("Questions found:")
        print("\n".join(extract_questions(messages)))

    elif choice == 18:
        u1 = input("User 1: ")
        u2 = input("User 2: ")
        print(f"Reply ratio from {u2} to {u1}: {reply_ratio(messages, u1, u2)} replies")

    elif choice == 19:
        print("Deleted messages found:", deleted_messages_count(messages))

    elif choice == 20:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
