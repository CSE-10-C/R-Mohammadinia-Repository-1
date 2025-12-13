import random


# ----- FUNCTIONS -----


# these are the definitions
def make_title(genre, character, place):
   return genre.upper() + " STORY ABOUT " + character.upper() + " IN " + place.upper()


def make_story(character, place, action):
   return character + " was in " + place + " and decided to " + action + "."


def filter_actions_by_genre(actions, genre):
   filtered = []


   for action in actions:
       a = action.lower()


       if genre == "Silly" and ("dance" in a or "laugh" in a or "prank" in a):
           filtered.append(action)


       elif genre == "Urban fantasy" and ("magic" in a or "city" in a or "spell" in a):
           filtered.append(action)


       elif genre == "Mysterious" and ("investigate" in a or "secret" in a or "follow" in a):
           filtered.append(action)


       elif genre == "Scary" and ("run" in a or "hide" in a or "scream" in a):
           filtered.append(action)


       elif genre == "Fantasy" and ("dragon" in a or "quest" in a or "sword" in a):
           filtered.append(action)


       elif genre == "Romance" and ("love" in a or "kiss" in a or "date" in a):
           filtered.append(action)


   # fallback if nothing matches
   if len(filtered) == 0:
       filtered = actions


   return filtered




# ----- MAIN PROGRAM -----


def main():
   print("Welcome to the Random Story Generator!")


   # Characters
   while True:
    try:
        num_chars = int(input("How many characters? Minimum 1: "))
        if num_chars >= 1:
            break
        print("Must be at least 1.")
    except ValueError:
        print("Please enter a number.")
  
   characters = []
   for i in range(num_chars):
       characters.append(input("Character " + str(i + 1) + ": "))


   # Places 
   num_places = int(input("How many places? Minimum 2: "))
   while num_places < 2:
       num_places = int(input("Enter at least 2: "))


   places = []
   for i in range(num_places):
       places.append(input("Place " + str(i + 1) + ": "))


   # Showing Actions list
   actions = [
       "dance on a table",
       "cast a magic spell",
       "investigate a secret room",
       "run from a shadow",
       "go on a quest with a dragon",
       "fall in love",
       "play a prank",
       "hide in the dark",
       "go on a date"
   ]


   print("\nAvailable actions:")
   for i in range(len(actions)):
       print(str(i + 1) + ".", actions[i])


   # User selects actions from the list
   chosen_actions = []
   while len(chosen_actions) < 2:
       picks = input("\nChoose at least 2 actions by number (comma separated): ")
       indexes = picks.split(",")


       chosen_actions = []
       for idx in indexes:
           if idx.strip().isdigit():
               num = int(idx) - 1
               if 0 <= num < len(actions):
                   chosen_actions.append(actions[num])


       if len(chosen_actions) < 2:
           print("You must choose at least 2 valid actions.")


   # Genre list is shown
   genres = ["Silly", "Urban fantasy", "Mysterious", "Scary", "Fantasy", "Romance"]


   print("\nAvailable genres:")
   for g in genres:
       print(g)


# genres chosen
   genre = input("\nChoose one genre: ")
   while genre not in genres:
       genre = input("Choose a valid genre: ")


   # Filter actions based on genre
   final_actions = filter_actions_by_genre(chosen_actions, genre)


   # Random selections
   character = random.choice(characters)
   place = random.choice(places)
   action = random.choice(final_actions)


   # output


   title = make_title(genre, character, place)
   story = make_story(character, place, action)


   print("\nGenerated Title:")
   print(title)


   print("\nGenerated Story:")
   print(story)




if __name__ == "__main__":
   main()
