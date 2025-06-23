
import random

## OPENING JOURNAL.TXT FILE IF IT DOES NOT EXIST
with open("Journal.txt", "a", encoding="utf-8"):
    pass

## JOURNAL -- LIST OF ENTRIES
Journal = []

## ENCOURAGEMENT QUOTES
encouragement_quotes = [
    "You've made it this far — and that's something to be proud of 💪❤️",
    "Even on your worst days, you're still growing 🌱 and becoming.",
    "Whatever you're feeling, it's okay. Just don't give up on yourself 🫂✨",
    "You're not alone — God's got you, even in the quiet moments 🙏🌌",
    "Some days are heavy 💭… but you don't have to carry them alone 💞",
    "Your worth isn't based on how productive you feel today 🧠💤",
    "The fact that you're still trying says so much about your strength 💖🔥",
    "You can rest and still be powerful — rest is part of the journey 🛌⚡",
    "Even small victories count — celebrate them 🎉 no matter how tiny.",
    "There's light ahead — even if you can't see it yet, keep moving 🚶‍♂️🌤️",
    "Breathe. You're doing better than you think 😌🌈",
    "Tired doesn't mean defeated — it just means you've been fighting 🥷💤",
    "Tears don't mean weakness 😢 — they mean you care deeply. That's strength.",
    "God hasn't forgotten you 📖🕊️ — your time is coming.",
    "You are allowed to feel it all and still move forward one step at a time 👣💫",
    "Some breakthroughs start with just breathing and staying 💭🌱",
    "You're more than what's stressing you out right now 🧠💥",
    "Let joy find you, even in small moments — a smile, a song, a breath 😊🎶",
    "Everything doesn't have to be perfect for it to be beautiful 🌷💖",
    "You've survived 100 percent of your hardest days. That's undefeated 💯🛡️",
    "Not feeling okay doesn't mean you're broken — it means you're human 🫶",
    "There's grace for today — and fresh hope for tomorrow 🕊️🌄",
    "You don't need to have it all figured out to take the next step 🗺️🚶‍♀️",
    "Let go of what you can't control and rest in what you can 🎈🧘",
    "God is still writing your story 📝 — and the plot twist is coming 🔁✨",
    "Even if no one sees it, your effort matters. Keep going 💼💙",
    "You were created on purpose, for a purpose — never doubt that 👑💡",
    "Healing isn't linear — be gentle with yourself 🩹🕊️",
    "There is still beauty to find, even here, even now 🌸🪞",
    "You're allowed to pause, but don't quit — you're worth the fight 🛑💥➡️🏁"
]

## ENTRY -- CLASS FOR ENTRIES INTO JOURNAL
class Entry:
    def __init__(self, title, date, mood, thoughts, to_do_list=None):
        self.title = title
        self.date = date
        self.mood = mood
        self.thoughts = thoughts
        self.to_do_list = to_do_list if to_do_list else []
        Journal.append(self)

    def display(self):
        print(f"\nDate: {self.date}")
        print(f"Title: {self.title}")
        print(f"Mood: {self.mood}")
        print("Thoughts:")
        print(self.thoughts)
        print("***To-do List***")
        for i, item in enumerate(self.to_do_list, start=1):
            print(f"{i}. {item}")

## SAVING -- FUNCTION FOR UPDATING TO FILE
def SaveFile():
    with open("Journal.txt", "w", encoding="utf-8") as saved_file:
        for item in Journal:
            saved_file.write(f"TITLE🧾:{item.title}\nDATE📅:{item.date}\nMOOD👶:{item.mood}\n")
            saved_file.write("YOUR THOUGHTS TODAY🧠:\n")
            saved_file.write(f"{item.thoughts}\n")
            saved_file.write("TO-DO LIST TODAY✍:\n")
            for task in item.to_do_list:
                saved_file.write(f"✔{task}\n")
            saved_file.write("......\n\n\n")

## LOADING ENTRIES FROM FILE
def LoadEntries():
    with open("Journal.txt", "r", encoding="utf-8") as file:
        content = file.read().strip()
        entries_raw = content.split("......")
        for raw in entries_raw:
            lines = raw.strip().split("\n")
            if len(lines) < 4:
                continue
            title = lines[0].replace("TITLE🧾:", "").strip()
            date = lines[1].replace("DATE📅:", "").strip()
            mood = lines[2].replace("MOOD👶:", "").strip()
            thoughts = []
            to_do_list = []
            section = None
            for line in lines[3:]:
                if "YOUR THOUGHTS TODAY🧠" in line.upper():
                    section = "thoughts"
                    continue
                elif "TO-DO LIST TODAY✍" in line.upper():
                    section = "todo"
                    continue
                elif section == "thoughts":
                    thoughts.append(line.strip())
                elif section == "todo":
                    if line.strip().startswith("✔"):
                        to_do_list.append(line.strip().replace("✔", "").strip())
            Entry(title, date, mood, "\n".join(thoughts), to_do_list)

## PROGRAM START
print("😊😊😊 JOURNAL MANAGEMENT SYSTEM 😊😊😊")
LoadEntries()

while True:
    print("\nWhat would you like to do?\n")
    print("1. ✍ Write a new journal entry")
    print("2. 🧾 View past entries")
    print("3. 🔍 Search entries by mood")
    print("4. ❎ Exit")
    
    try:
        choice = int(input(": "))
        if choice < 1 or choice > 4:
            raise ValueError
    except ValueError:
        print("❌ INVALID ENTRY")
        continue

    # CHOICE 1 -- WRITING A NEW JOURNAL ENTRY
    if choice == 1:
        name = input("Enter the title of the entry: ")
        date = input("Enter date (dd/mm/yyyy): ")
        mood = input("What's your mood today? ")
        thoughts = input("Thoughts? 🤔 What's on your mind:\n")
        entries = []
        try:
            num = int(input("How many things are you adding to the list? "))
        except ValueError:
            print("❌ INVALID NUMBER. Skipping to-do list.")
            num = 0
        for i in range(num):
            listing = input(f"Enter entry {i+1}: ")
            entries.append(listing)
        Entry(name, date, mood, thoughts, entries)
        SaveFile()
        print("✅ Entries successfully saved!")

    # CHOICE 2 -- VIEWING PAST ENTRIES
    elif choice == 2:
        print("*** OPENING THE WHOLE JOURNAL ***\n\n")
        with open("Journal.txt", "r", encoding="utf-8") as display_file:
            print(display_file.read())

    # CHOICE 3 -- SEARCHING ENTRIES BY MOOD
    elif choice == 3:
        mood = input("Enter the mood you wish to look up: ").strip()
        matches = [entry for entry in Journal if entry.mood.lower() == mood.lower()]
        if matches:
            print(f"\n📓 Entries for mood '{mood}':\n")
            for entry in matches:
                entry.display()
        else:
            print(f"❌ No entries found for mood: {mood}")

    # CHOICE 4 -- EXITING THE PROGRAM
    elif choice == 4:
        print("🙏 Have a nice day ahead of you!")
        print(f"Today's quote 😎\n➡ {random.choice(encouragement_quotes)}")
        break

##CodeName -- BoldWhiteWidow
