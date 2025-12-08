n =int(input("Enter the number of messages: "))
messages = []
user_msgs = {}
for i in range(n):
    line = input().rstrip()
    parts = line.split(":", 1)
    if len(parts) < 2:
        name = parts[0].strip()
        msg = ""
    else:
        name = parts[0].strip()
        msg = parts[1].strip()
    full = name + ": " + msg
    messages.append(full)
    if name in user_msgs:
        user_msgs[name].append(msg)
    else:
        user_msgs[name] = [msg]

c = {
    1: 'Count total number of messages',
    2: 'Identify unique users in the chat',
    3: 'Count total words in the chat',
    4: 'Calculate average words per message',
    5: 'Find the longest message sent',
    6: 'Find the most active user',
    7: 'Get message count for a specific user',
    8: 'Find the most frequently used word by a specific user',
    9: 'Retrieve the first and last message sent by a user',
    10: 'Check if a user is present in the chat',
    11: 'Find commonly repeated words',
    12: 'Identify the user with the longest average message length',
    13: 'Count how many messages mention a specific user',
    14: 'Remove duplicate messages',
    15: 'Sort messages alphabetically',
    16: 'Extract all questions asked in the chat',
    17: 'Calculate the reply ratio between two users',
    18: 'Check for deleted messages'
}

while True:
    print("\nMenu:")
    for i in range(1, 19):
        print(str(i) + ". " + c[i])
    print("19. End program")

    ch_input = input("Enter the choice: ").strip()

    if ch_input == "":
        print("Invalid input. Try again.")
        continue

    if ch_input.isdigit():
        ch = int(ch_input)
    else:
        print("Invalid choice (not a number). Try again.")
        continue
    if ch == 1:
        print("Total messages:", len(messages))

    elif ch == 2:
        unique = []
        for name in user_msgs:
            unique.append(name)
        print("Unique users in the chat: {" + ", ".join(["'"+u+"'" for u in unique]) + "}")

    elif ch == 3:
        total_words = 0
        for full in messages:
            parts = full.split(":", 1)
            if len(parts) > 1:
                msg = parts[1].strip()
            else:
                msg = ""
            if msg == "":
                continue
            words = msg.split()
            total_words = total_words + len(words)
        print("Total words in the chat:", total_words)

    elif ch == 4:
        total_words = 0
        for full in messages:
            parts = full.split(":", 1)
            if len(parts) > 1:
                msg = parts[1].strip()
            else:
                msg = ""
            if msg == "":
                continue
            words = msg.split()
            total_words = total_words + len(words)
        total_msgs = len(messages)
        if total_msgs == 0:
            avg = 0.0
        else:
            avg = float(total_words) / float(total_msgs)
        print("Average words per message: {:.2f}".format(avg))

    elif ch == 5:
        if len(messages) == 0:
            print("No messages.")
        else:
            longest = messages[0]
            longest_len = 0
            for full in messages:
                parts = full.split(":", 1)
                msg = ""
                if len(parts) > 1:
                    msg = parts[1].strip()
                if len(full) > longest_len:
                    longest_len = len(full)
                    longest = full
            print('Longest message: "{}"'.format(longest))

    elif ch == 6:
        if len(user_msgs) == 0:
            print("No users.")
        else:
            top_user = None
            top_count = -1
            for name in user_msgs:
                count = 0
                for m in user_msgs[name]:
                    count = count + 1
                if count > top_count:
                    top_count = count
                    top_user = name
            print("Most active user: {} ({} messages)".format(top_user, top_count))

    elif ch == 7:
        q = input("Input user name: ").strip()
        if q in user_msgs:
            cnt = 0
            for _ in user_msgs[q]:
                cnt = cnt + 1
            print("Messages sent by {}: {}".format(q, cnt))
        else:
            print("User '{}' not found in the chat.".format(q))

    elif ch == 8:
        q = input("Input user name: ").strip()
        if q not in user_msgs:
            print("User '{}' not found in the chat.".format(q))
        else:
            counts = {}
            for msg in user_msgs[q]:
                words = msg.split()
                for w in words:
                    w2 = w.strip().lower()
                    while w2 != "" and (w2[0] in ".,!?\"'()[]{}:;"):
                        w2 = w2[1:]
                    while w2 != "" and (w2[-1] in ".,!?\"'()[]{}:;"):
                        w2 = w2[:-1]
                    if w2 == "":
                        continue
                    if w2 in counts:
                        counts[w2] = counts[w2] + 1
                    else:
                        counts[w2] = 1
            if len(counts) == 0:
                print("No words found for user {}.".format(q))
            else:
                top_word = None
                top_ct = -1
                for ww in counts:
                    if counts[ww] > top_ct:
                        top_ct = counts[ww]
                        top_word = ww
                print('Most frequent word used by {}: "{}"'.format(q, top_word))

    elif ch == 9:
        q = input("Input user name: ").strip()
        if q not in user_msgs:
            print("User '{}' not found in the chat.".format(q))
        else:
            msgs = user_msgs[q]
            if len(msgs) == 0:
                print("No messages by {}.".format(q))
            else:
                first = q + ": " + msgs[0]
                last = q + ": " + msgs[-1]
                print('First message by {}: "{}"'.format(q, first))
                print('Last message by {}: "{}"'.format(q, last))

    elif ch == 10:
        q = input("Input user name: ").strip()
        if q in user_msgs:
            print("User '{}' found in the chat.".format(q))
        else:
            print("User '{}' not found in the chat.".format(q))

    elif ch == 11:
        counts = {}
        for full in messages:
            parts = full.split(":", 1)
            msg = ""
            if len(parts) > 1:
                msg = parts[1].strip()
            if msg == "":
                continue
            words = msg.split()
            for w in words:
                w2 = w.strip().lower()
                while w2 != "" and (w2[0] in ".,!?\"'()[]{}:;"):
                    w2 = w2[1:]
                while w2 != "" and (w2[-1] in ".,!?\"'()[]{}:;"):
                    w2 = w2[:-1]
                if w2 == "":
                    continue
                if w2 in counts:
                    counts[w2] = counts[w2] + 1
                else:
                    counts[w2] = 1
        repeated = []
        for w in counts:
            if counts[w] > 1:
                repeated.append(w)
        if len(repeated) == 0:
            print("Common repeated words: {}")
        else:
            print("Common repeated words: {" + ", ".join(["'"+x+"'" for x in repeated]) + "}")


    elif ch == 12:
        best_user = None
        best_avg = 0.0
        for name in user_msgs:
            total_w = 0
            total_m = 0
            for msg in user_msgs[name]:
                words = msg.split()
                total_w = total_w + len(words)
                total_m = total_m + 1
            if total_m == 0:
                avg = 0.0
            else:
                avg = float(total_w) / float(total_m)
            if best_user is None or avg > best_avg:
                best_user = name
                best_avg = avg
        if best_user is None:
            print("No users/messages.")
        else:
            print("User with longest average message: {} (avg {:.1f} words)".format(best_user, best_avg))

    elif ch == 13:
        q = input("Input user name to check mentions: ").strip()
        mention_count = 0
        q_low = q.lower()
        for full in messages:
            if q_low in full.lower():
                parts = full.split(":", 1)
                if len(parts) > 1:
                    msg = parts[1].strip().lower()
                    if q_low in msg:
                        mention_count = mention_count + 1
        print("Messages mentioning '{}': {}".format(q, mention_count))

    elif ch == 14:
        unique_list = []
        seen = {}
        for full in messages:
            if full not in seen:
                seen[full] = True
                unique_list.append(full)
        print("Unique messages count:", len(unique_list))
        print("Unique messages (chronological):")
        for um in unique_list:
            print(um)

    elif ch == 15:
        sorted_msgs = []
        for m in messages:
            sorted_msgs.append(m)
        sorted_msgs.sort()
        print("Messages sorted A-Z:")
        for m in sorted_msgs:
            print(m)

    elif ch == 16:
        qmsgs = []
        for full in messages:
            if "?" in full:
                qmsgs.append(full)
        if len(qmsgs) == 0:
            print("No questions found in the chat.")
        else:
            print("Questions found:")
            for qm in qmsgs:
                print(qm)

    elif ch == 17:
        a = input("Input the first user (e.g., Alice): ").strip()
        b = input("Input the second user (who replies) (e.g., Bob): ").strip()
        replies = 0
        for i in range(0, len(messages) - 1):
            cur = messages[i].split(":", 1)[0].strip()
            nxt = messages[i+1].split(":", 1)[0].strip()
            if cur == a and nxt == b:
                replies = replies + 1
        print("Reply ratio from {} to {}: {} replies".format(b, a, replies))

    elif ch == 18:
        cnt = 0
        for full in messages:
            parts = full.split(":", 1)
            msg = ""
            if len(parts) > 1:
                msg = parts[1].strip()
            if msg == "This message was deleted":
                cnt = cnt + 1
        if cnt == 0:
            print("Deleted messages found: 0")
        else:
            print("Deleted messages found:", cnt)

    elif ch == 19:
        print("End of the program")
        break

    else:
        print("INVALID CHOICE")