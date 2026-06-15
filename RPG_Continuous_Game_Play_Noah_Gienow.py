#RPG Continuous Game Play - Noah Gienow
#June 17, 2026

#This program is a playable text based game with various responses based on the user input
#It uses lists to keep track of information and can be looped endlessly


import sys  # Import sys module for system-specific functions like sys.exit()
import time  # Import time module for creating delays in output

# Define a function to print text slowly character by character for dramatic effect
def slow_print(text):
    for char in text:  # Loop through each character in the text
        print(char, end="", flush=True)  # Print the character without a newline, flush output buffer
        time.sleep(0.02)  # Pause briefly to create the slow typing effect
    print()  # Print a newline after the entire text has been printed

# Define a function to handle the death scenario
def death():
    death_text = [
        "\nYou have died, would you like to play again?\n"  # Message indicating player has died
    ]
    choices = [
        "1. play again",  # Option to restart the game
        "2. Quit game"      # Option to exit the game
    ]
    for line in death_text:  # Loop through each line in death_text
        slow_print(line)  # Print each line slowly
    for option in choices:  # Loop through each choice
        slow_print(option)  # Print each choice slowly
    choice = input(">")  # Prompt player for input
    if choice == "1":  # If player chooses to play again
        start()  # Call the start() function to restart the game
    elif choice == "2":  # If player chooses to quit
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()  # Exit the program
    else:  # If input is invalid
        slow_print("\nInvalid choice")  # Inform the player
        death()  # Restart the death scenario

# Define a function for victory scenario
def victory():
    victory_text = [
        "\nYou have escaped the forest! Would you like to play again?\n"  # Victory message
    ]
    choices = [
        "1. play again",  # Option to restart
        "2. Quit game"      # Option to exit
    ]
    for line in victory_text:  # Loop through victory message
        slow_print(line)  # Print message slowly
    for option in choices:  # Loop through options
        slow_print(option)  # Print options
    choice = input(">")  # Get player input
    if choice == "1":  # Restart game if chosen
        start()  # Call start() function
    elif choice == "2":  # Exit game if chosen
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()  # Exit program
    else:  # Handle invalid input
        slow_print("\nInvalid choice")  # Notify invalid input
        victory()  # Restart victory scenario

# Define the main starting function of the game
def start():
    intro_text = [
        "You notice something lurking in the darkness just out of sight.",  # Introductory message
        "\nWhat will you do?\n"  # Prompt for player action
    ]
    choices = [
        "1. Sprint immediately in the opposite direction",  # Player can choose to sprint
        "2. Continue moving as if you saw nothing",  # Or ignore and keep moving
        "3. Call your superiors to report the anomaly",  # Or report the anomaly
        "4. Stand completely still",  # Or stand still
        "5. Quit game"  # Or quit the game
    ]
    for line in intro_text:  # Loop through intro text
        slow_print(line)  # Print each line slowly
    for option in choices:  # Loop through choices
        slow_print(option)  # Print options
    choice = input("> ")  # Get player's choice
    if choice == "1":  # If choice is to sprint
        sprint()  # Call sprint() function
    elif choice == "2":  # If choice is to continue moving
        moving()  # Call moving() function
    elif choice == "3":  # If reporting to superiors
        call()  # Call call() function
    elif choice == "4":  # If standing still
        stand()  # Call stand() function
    elif choice == "5":  # If quitting
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()  # Exit the game
    else:  # For invalid input
        slow_print("\nInvalid choice")  # Notify invalid input
        start()  # Restart the start() function

# Function for sprinting action
def sprint():
    sprint_text = [
        """You sprint through the forest, stumbling on loose branches but
never stopping to look back. Eventually you collapse, completely
drained of energy. You finally look back and see it approaching in
the distance, slowly closing the gap you created.
        \nWhat will you do?\n"""  # Description of sprinting scenario
    ]
    choices = [
        "1. Keep Moving",  # Player can keep moving
        "2. Take a minute to catch your breath and think through the situation",  # Or pause
        "3. Quit game"  # Or quit
    ]
    for line in sprint_text:  # Loop through sprint description
        slow_print(line)  # Print slowly
    for option in choices:  # Loop through options
        slow_print(option)  # Print options
    choice = input("> ")  # Player input
    if choice == "1":  # If player chooses to keep moving
        keep_moving()  # Call keep_moving() function
    elif choice == "2":  # If player chooses to catch breath
        catch_breath()  # Call catch_breath() function
    elif choice == "3":  # If player quits
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()  # Exit game
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid input
        sprint()  # Repeat sprint()

# Function for continuing to move after sprint
def keep_moving():
    keepmoving_text = [
        """You push through the utter exhaustion and slowly stumble
your way through the forest, you spot a small cabin in the distance.
        \nWhat will you do?\n"""  # Description of pushing forward
    ]
    choices = [
        "1. Continue to push yourself and get to the cabin",  # Move towards cabin
        "2. Give in to your exhaustion",  # Or give up
        "3. Quit game"  # Or quit
    ]
    for line in keepmoving_text:  # Loop through description
        slow_print(line)
    for option in choices:  # Loop through options
        slow_print(option)
    choice = input("> ")  # Player input
    if choice == "1":  # Player chooses to push on
        # Player collapses, leading to death
        slow_print("""You force yourself to keep moving. You have to
get to this cabin. However as you move you notice the cabin never
gets closer. You walk for as long as you can but never make any
progress. Eventually your body can't take it anymore and you
collapse onto the ground. The creature does not stop its
pursuit. Your body will not be found.""")
        death()  # Call death() function
    elif choice == "2":  # Player gives up
        # Player passes out, leading to death
        slow_print("""The second you decide to stop moving your body
falls to the ground, you close your eyes and immediately lose
consciousness. Your body will not be found.""")
        death()
    elif choice == "3":  # Player quits
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid input
        keep_moving()  # Repeat keep_moving()

# Function for player moving at a slow pace, observing clues
def catch_breath():
    catchbreath_text = [
        """You move at a slow pace, making sure to stay just out of range
of the creature still lurking behind you and think back to your
mission. You were sent here to search for any anomalies and now
that you have found one you need to report it to your superiors
and get out quickly. You call them but surprisingly they
tell you to walk up to the creature instead of getting out of
the forest.
        \nWhat will you do?\n"""  # Scenario description
    ]
    choices = [
        "1. Ignore them and continue with your previous mission",  # Ignore orders
        "2. Listen and approach the creature",  # Approach creature
        "3. Quit game"  # Quit
    ]
    for line in catchbreath_text:
        slow_print(line)  # Print description
    for option in choices:
        slow_print(option)  # Print options
    choice = input("> ")  # Player input
    if choice == "1":  # Ignore superiors
        ignore()  # Call ignore()
    elif choice == "2":  # Approach creature
        # Approaching leads to death
        slow_print("""As you approach your mind goes numb. You see that your
superiors were right, you need to be with the creature. You have no
problem remaining in this forest forever. Your body will not be found.""")
        death()
    elif choice == "3":  # Quit game
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()  # Exit program
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid input
        catch_breath()  # Repeat catch_breath()

# Function if player ignores superiors and continues moving
def ignore():
    ignore_text = [
        """You ignore the advice from your superiors and begin
searching for a way to leave the forest. The creature keeps following
you, now a little closer than before.
        \nWhat will you do?\n"""  # Scenario description
    ]
    choices = [
        "1. Keep Moving, you can tell your close to the exit",  # Keep moving
        "2. Quickly throw something at the creature",  # Distract creature
        "3. Quit game"  # Quit
    ]
    for line in ignore_text:
        slow_print(line)  # Print scenario
    for option in choices:
        slow_print(option)  # Print choices
    choice = input("> ")  # Player input
    if choice == "1":  # Keep moving towards exit
        # Player gets attacked and dies
        slow_print("""The creature can tell you are getting close and attacks
you quickly without any time to run. Your body will not be found.""")
        death()
    elif choice == "2":  # Throw object at creature
        quick_throw()  # Call quick_throw()
    elif choice == "3":  # Quit game
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()  # Exit program
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid input
        ignore()  # Repeat ignore()

# Player throws rocks to distract or scare the creature
def quick_throw():
    quickthrow_text = [
        """You throw a light rock where the creature is but it passes right
through. Now you remember what you're up against. Before you left
you were briefed on what you may encounter. One of the predictions
was that the unknown creature could cause minor hallucinations
in its prey that grew stronger the closer it got to you. How
could you forget something so important?
        \nWhat will you do?\n"""  # Scene description
    ]
    choices = [
        "1. Continue attacking the creature, now that you know what it is you might be able to kill it.",  # Fight
        "2. run as far away as you can and call your superiors again.",  # Retreat
        "3. Quit game"  # Quit
    ]
    for line in quickthrow_text:
        slow_print(line)  # Print scene description
    for option in choices:
        slow_print(option)  # Print options
    choice = input("> ")  # Player input
    if choice == "1":  # Fight
        # Player fails and dies
        slow_print("""You throw more rocks at the creature, this time heavier
but they still have no effect. The creature suddenly disappears
and you hope you've scared it off. However you then see it
multiply, approaching from all directions at once. It seems
it has caught on and is now ending this game of cat and
mouse. You have no choice and run into one of them, hoping
it's not the real one but you are sorely mistaken. Your
body will not be found.""")
        death()
    elif choice == "2":  # Retreat and call back
        call_back()
    elif choice == "3":  # Quit game
        slow_print("\nThanks for playing!")
        sys.exit()
    else:  # Invalid input
        slow_print("\nInvalid choice")
        quick_throw()

# Function to call for rescue help from superiors
def call_back():
    callback_text = [
        """You quickly dash through the trees and call them, they answer
immediately. "Hello! Why haven't you answered any of our calls? Whats
the situation out there??" You explain what happened and that you
need an immediate rescue. They assure you help is on the way.
        \nWhat will you do?\n"""  # Dialogue and situation
    ]
    choices = [
        "1. Keep running and hope they arrive quickly.",  # Keep moving
        "2. Attempt to climb a nearby tree and wait out the creature.",  # Climb and wait
        "3. Quit game"  # Quit
    ]
    for line in callback_text:
        slow_print(line)  # Print dialogue
    for option in choices:
        slow_print(option)  # Print options
    choice = input("> ")  # Player input
    if choice == "1":  # Keep running
        # Player gets exhausted and is pounced upon
        slow_print("""You once again begin running but are out of energy.
The creature senses your desperation and finally pounces.
Your body will not be found.""")
        death()
    elif choice == "2":  # Climb tree
        climb_tree()  # Call climb_tree()
    elif choice == "3":  # Quit
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()  # Exit game
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid
        call_back()  # Repeat call_back()

# Player climbs a tree to escape or find something
def climb_tree():
    climbtree_text = [
        """Miraculously you manage to climb the tree and the creature seems
unable to follow. It stays at the base when suddenly a though
enters your head. You need to go down immediately and get
something important.
        \nWhat will you do?\n"""  # Scene description
    ]
    choices = [
        "1. Ignore your thoughts and keep waiting for rescue.",  # Wait
        "2. Quickly go down and find whatever you lost.",  # Descend
        "3. Quit game"  # Quit
    ]
    for line in climbtree_text:
        slow_print(line)  # Print scene
    for option in choices:
        slow_print(option)  # Print options
    choice = input("> ")  # Player input
    if choice == "1":  # Ignore thoughts and wait
        # Player waits and is rescued
        slow_print("""You push all thoughts to the back of your mind and wait.
 Finally a helicopter soars overhead and drops a ladder right in front
 of you. You grad hold and fly out of the forest.""")
        victory()  # Call victory()
    elif choice == "2":  # Go down to find lost item
        # Player tries to descend but is caught
        slow_print("""You jump down and try to run but it's too late. The creature
catches you. What were you even looking for? Either way, your body will not be found.""")
        death()
    elif choice == "3":  # Quit game
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()  # Exit game
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid
        climb_tree()  # Repeat climb_tree()

# Player chooses to stand still
def stand():
    stand_text = [
        """You stand still, not moving a muscle, the creature begins to approach you.
        \nWhat will you do?\n"""  # Scene description
    ]
    choices = [
        "1. Continue standing still",  # Stand still
        "2. Sprint immediately in the opposite direction",  # Run away
        "3. Quit game"  # Quit
    ]
    for line in stand_text:
        slow_print(line)  # Print scene
    for option in choices:
        slow_print(option)  # Print options
    choice = input("> ")  # Player input
    if choice == "1":  # Continue standing
        # Player is caught and dies
        slow_print("""As the distance closes your mind goes numb, you see
that there was never a point in running at all. You have no
problem with remaining in this forest forever. Your body
will not be found.""")
        death()
    elif choice == "2":  # Sprint away
        sprint()  # Call sprint()
    elif choice == "3":  # Quit game
        slow_print("\nThanks for playing!")  # Thank you
        sys.exit()  # Exit game
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid
        stand()  # Repeat stand()

# Player walking through forest, noticing clues
def moving():
    moving_text = [
        """As you walk carefully through the forest you notice a teared piece
of clothing and a light trail of blood.
        \nWhat will you do?\n"""  # Scene description
    ]
    choices = [
        "1. Keep moving in the direction you were before",  # Continue forward
        "2. Change course and follow it",  # Follow trail
        "3. Quit game"  # Quit
    ]
    for line in moving_text:
        slow_print(line)  # Print scene
    for option in choices:
        slow_print(option)  # Print choices
    choice = input("> ")  # Player input
    if choice == "1":  # Continue in same direction
        keep_moving()  # Call keep_moving()
    elif choice == "2":  # Change course
        change()  # Call change()
    elif choice == "3":  # Quit game
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()  # Exit game
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid
        moving()  # Repeat moving()

# Player attempts to approach or avoid the creature based on instructions
def call():
    call_text = [
        """Your superiors respond calmly, as if expecting this. They tell you
not to be concerned and to approach the creature
        \nWhat will you do?\n"""  # Dialogue prompt
    ]
    choices = [
        "1. Listen to them and slowly approach the creature",  # Approach
        "2. Ignore your superiors and begin moving in the opposite direction",  # Avoid
        "3. Quit game"  # Quit
    ]
    for line in call_text:
        slow_print(line)  # Print dialogue
    for option in choices:
        slow_print(option)  # Print options
    choice = input("> ")  # Player input
    if choice == "1":  # Approach creature
        # Approaching leads to death
        slow_print("""As the distance closes your mind goes numb. You see that
there was never a point in running at all. You have no problem with
remaining in this forest forever. Your body will not be found.""")
        death()
    elif choice == "2":  # Avoid
        moving()  # Continue moving
    elif choice == "3":  # Quit
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()  # Exit game
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid
        call()  # Repeat call()

# Player follows orders to approach the creature
def keep_moving():
    keepmoving_text = [
        """You continue walking calmly in the same direction when suddenly you
get a call from your superiors. "What are you doing unit 07
follow the mission objectives and approach the creature to
collect data." However you are almost certain the mission
objectives were to search for any anomalies and get out
fast if any were found.
        \nWhat will you do?\n"""  # Mission description
    ]
    choices = [
        "1. Follow their command and approach the creature",  # Approach
        "2. Ignore your superiors and keep moving",  # Ignore
        "3. Quit game"  # Quit
    ]
    for line in keepmoving_text:
        slow_print(line)  # Print scenario
    for option in choices:
        slow_print(option)  # Print options
    choice = input("> ")  # Player choice
    if choice == "1":  # Approach creature
        # Player approaches and dies
        slow_print("""At first you are apprehensive but the closer you get the
less you worry. You realize that it was pointless to run away,
you run towards the creature happily. Your mind goes blank.
Your body will not be found.""")
        death()
    elif choice == "2":  # Ignore orders
        ignore()  # Call ignore()
    elif choice == "3":  # Quit
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()  # Exit game
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid
        keep_moving()  # Repeat keep_moving()

# Player finds items along the trail
def change():
    change_text = [
        """As you follow the trail more items appear, first a notebook then
a backpack and finally, a body with a note clutched
in its hand.
        \nWhat will you do?\n"""  # Scene description
    ]
    choices = [
        "1. Take the note",  # Pick up note
        "2. Leave the body and keep walking",  # Leave body
        "3. Quit game"  # Quit
    ]
    for line in change_text:
        slow_print(line)  # Print scene
    for option in choices:
        slow_print(option)  # Print options
    choice = input("> ")  # Player input
    if choice == "1":  # Take note
        # Player takes note and proceeds to scream
        slow_print("""You pry the note from the bodies hand and see a messy scratch
of writing "None of it is real, do not trust them, do not
trust yourself, keep moving". """)
        scream()  # Call scream()
    elif choice == "2":  # Leave body
        # Player ignores note and walks on, then screams
        slow_print("""The sun has almost completely set, you ignore the body and
        wonder how much further this forest goes on for.""")
        scream()  # Call scream()
    elif choice == "3":  # Quit game
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()  # Exit
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid
        change()  # Repeat change()

# A scream is heard, player chooses to help or ignore
def scream():
    scream_text = [
        """Suddenly you hear a scream in the distance and see a girl come sprinting
towards you calling for help.
        \nWhat will you do?\n"""  # Scene description
    ]
    choices = [
        "1. Rush to help the girl",  # Help
        "2. Ignore her entirely and keep moving",  # Ignore
        "3. Quit game"  # Quit
    ]
    for line in scream_text:
        slow_print(line)  # Print scene
    for option in choices:
        slow_print(option)  # Print options
    choice = input("> ")  # Player input
    if choice == "1":  # Help girl
        cooked()  # Call cooked()
    elif choice == "2":  # Ignore girl
        ignore_girl()  # Call ignore_girl()
    elif choice == "3":  # Quit
        slow_print("\nThanks for playing!")  # Thank player
        sys.exit()  # Exit game
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid
        scream()  # Repeat scream()

# Player approaches the girl, but she vanishes, creature appears behind
def cooked():
    cooked_text = [
        """You rush towards the terrified girl but when you reach her she
completely vanishes. You stand there dazed. You look behind and
see the creature standing directly behind you, waiting. You
have no choice, your body moves on its own.
        \nHow will you die?\n"""  # Scene description
    ]
    choices = [
        "1. Approach the creature",  # Approach
        "2. Approach the creature",  # Repeated options for some reason
        "3. Approach the creature",
        "4. Quit game"
    ]
    for line in cooked_text:
        slow_print(line)  # Print scene
    for option in choices:
        slow_print(option)  # Print options
    choice = input("> ")  # Player input
    if choice == "1":  # Approach
        slow_print("your body will not be found.")  # Player dies
        death()
    elif choice == "2":  # Repeat
        slow_print("your body will not be found.")  # Player dies
        death()
    elif choice == "3":  # Repeat
        slow_print("your body will not be found.")  # Player dies
        death()
    elif choice == "4":  # Quit
        slow_print("\nThanks for playing!")  # Thank player
        sys.exit()
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid
        cooked()  # Repeat cooked()

# If player ignores the girl and walks away, she disappears and they reach a clearing
def ignore_girl():
    ignoregirl_text = [
        """You keep walking and notice her screams disappear, there
is a clearing up ahead.
        \nWhat will you do?\n"""  # Scene description
    ]
    choices = [
        "1. Keep moving forwards towards it",  # Move towards clearing
        "2. Stay within the forest",  # Stay inside
        "3. Quit game"  # Quit
    ]
    for line in ignoregirl_text:
        slow_print(line)  # Print scene
    for option in choices:
        slow_print(option)  # Print options
    choice = input("> ")  # Player input
    if choice == "1":  # Move towards clearing
        clearing()  # Call clearing()
    elif choice == "2":  # Stay in forest
        # Player gets attacked and dies
        slow_print("""The second you turn away from the clearing the creature
pounces. You try to run but you are struck down and mauled.
Your body will not be found.""")
        death()
    elif choice == "3":  # Quit
        slow_print("\nThanks for playing!")  # Thank player
        sys.exit()  # Exit game
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid
        ignore_girl()  # Repeat ignore_girl()

# Player reaches the edge of a cliff in the clearing
def clearing():
    clearing_text = [
        """You walk through the clearing and see you are on the edge
of a cliff. The creature stands still awaiting your decision.
        \nWhat will you do?\n"""  # Scene description
    ]
    choices = [
        "1. Re-enter the forest",  # Turn back
        "2. Jump",  # Jump off
        "3. Quit game"  # Quit
    ]
    for line in clearing_text:
        slow_print(line)  # Print scene
    for option in choices:
        slow_print(option)  # Print options
    choice = input("> ")  # Player input
    if choice == "1":  # Re-enter forest
        # Player tries to go back but gets attacked
        slow_print("""The second you turn away from the cliffs edge the
creature pounces. You try to run but are struck down and mauled.
Your body will not be found.""")
        death()
    elif choice == "2":  # Jump
        # Player jumps and escapes, reaching victory
        slow_print("""You close your eyes and throw yourself off the edge.
However you land much sooner than you were expecting. When
you open your eyes the terrain is completely different than
it was before. The forest is now behind you and the
The creature is nowhere to be seen. You are finally out of
the forest.""")
        victory()
    elif choice == "3":  # Quit
        slow_print("\nThanks for playing!")  # Thank the player
        sys.exit()  # Exit game
    else:  # Invalid input
        slow_print("\nInvalid choice")  # Notify invalid
        clearing()  # Repeat clearing()

# Call the start() function to begin the game
start()