import Button
import pygame
import tkinter as tk
import Duck
import Goose
import HandGestureInterpreter
import random
import Rock
import ScoreCounter
import Timer
import RPSGame


def game_instruction_popup():
    """
    Summon the game instructions in a popup window.
    Blocks pygame events until the popup is closed.
    """
    tk_popup = tk.Tk()
    tk_popup.title('Game Instructions and Rules')
    scrollbar = tk.Scrollbar(tk_popup)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text = tk.Text(tk_popup, height=10, width=30, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text.configure(font=("Comic Sans MS", 18))
    text.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar.config(command=text.yview)
    text.insert(tk.END, "You are a duck.\n")
    text.insert(tk.END, "You like to eat peas.\n")
    text.insert(tk.END, "There are rocks on your path to the peas. Avoid the rocks by jumping.")
    text.insert(tk.END, "To jump, point up with 1 finger.\n")
    text.insert(tk.END,
                "You may encounter geese along the way. The geese are mean and charge a toll to pass them.\n")
    text.insert(tk.END, "You may pay peas to the geese or challenge them to rock paper scissors.\n")
    text.insert(tk.END, "If you win, the geese will give you some peas.\n")
    text.insert(tk.END, "However, if you lose, the geese will take a lot of your peas.\n")
    text.insert(tk.END, "Obtain as many peas as possible within the time limit.\n")
    text.configure(state='disabled')
    tk.mainloop()


def game_end_popup(score, status):
    """
    Generate the popup for the end of the game
    :param score: The number of peas you have at the end of the game
    :param status: A string, either 'time', 'peas', or 'rock'
    """
    tk_popup = tk.Tk()
    tk_popup.title('Game Over')
    scrollbar = tk.Scrollbar(tk_popup)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text = tk.Text(tk_popup, height=10, width=30, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text.configure(font=("Comic Sans MS", 18))
    text.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar.config(command=text.yview)
    if status == 'time':
        text.insert(tk.END, "Time's up!\n")
    elif status == 'peas':
        text.insert(tk.END, "You ran out of peas!\n")
    else:
        text.insert(tk.END, "You ran into a rock!\n")
    text.insert(tk.END, "Final score: " + str(score))
    text.configure(state='disabled')
    tk.mainloop()


class Game:

    def __init__(self, screen, win_width, win_height):
        # These variables are needed for the game, but not the start screen
        self.hand_seer = None
        self.rocks = None
        self.game_timer = None
        self.score_counter = None

        self.timer = pygame.time.get_ticks()
        self.state = 1  # 1 = home screen, 2 = game screen, 3 = end screen
        self.win_width = win_width
        self.win_height = win_height
        self.screen = screen

        # Create Button objects
        self.start_button = Button.Button(int(win_width / 6), int(3 * win_height / 4), 'Start')
        self.help_button = Button.Button(int(win_width / 3), int(3 * win_height / 4), 'Instructions')
        self.quit_button = Button.Button(10, 10, 'Quit')
        self.quit_button.set_inactive()

        # Create duck object
        self.duck = Duck.Duck(win_width/2-200, win_height/2-25)

        # Create goose variable
        self.goose = Goose.Goose(self.win_width, self.win_height-300)

    def start_screen_setup(self):
        """
        Draws the start screen
        """
        self.screen.fill((185, 122, 87))

        # Calculate width and height of game banner
        # Then draw the game banner
        game_banner_img = pygame.image.load('gameBanner.png')
        game_banner_ratio = 1
        game_banner_width = int(self.win_width * game_banner_ratio)
        game_banner_height = int(game_banner_img.get_height() * game_banner_width / game_banner_img.get_width())
        game_banner = pygame.transform.scale(game_banner_img, (game_banner_width, game_banner_height))
        self.screen.blit(game_banner, (int(self.win_width / 2 - game_banner_width / 2), 0))

        # Draw the buttons
        self.start_button.draw(self.screen)
        self.help_button.draw(self.screen)

    def start_init(self):
        self.state = 1

        # Set buttons active/inactive
        self.quit_button.set_inactive()
        self.start_button.set_active()
        self.help_button.set_active()

        # Draw the screen
        self.start_screen_setup()

    def game_init(self):
        """
        Initialize the game screen
        """
        self.state = 2
        self.start_button.set_inactive()
        self.help_button.set_inactive()
        self.quit_button.set_active()

        # Make the hand seeing object
        self.hand_seer = HandGestureInterpreter.HandGestureInterpreter()

        # Set up the obstacle arrays
        self.rocks = []

        # Initialize the timer for obstacle generation
        self.timer = pygame.time.get_ticks()

        # Initialize the timer for the game
        self.game_timer = Timer.Timer(self.win_width-320, 10)

        # Make score counter
        self.score_counter = ScoreCounter.ScoreCounter(self.win_width / 2 - 300, 10)

        # Draw things
        self.screen.fill((185, 122, 87))
        self.quit_button.draw(self.screen)
        self.duck.draw(self.screen)

    def generate_obstacles(self):
        """
        If a certain number of milliseconds have passed, have a certain chance of generating peas or rocks
        Requires that game_init() is called first
        """
        if pygame.time.get_ticks() - self.timer > 1400:
            rand_num = random.randint(1, 100)
            if rand_num <= 30:
                self.rocks.append(Rock.Rock(self.win_width, self.win_height-50, False))
            elif rand_num <= 50 and not self.goose.exists:
                self.goose.set_exist()
            elif rand_num <= 90:
                self.rocks.append(Rock.Rock(self.win_width, self.win_height - 50, True))
            self.timer = pygame.time.get_ticks()

    def update_game_screen(self):
        """
        Update the game by drawing a new frame. Requires that game_init() is called first
        """
        self.screen.fill((182, 243, 255))
        pygame.draw.rect(self.screen, (185, 122, 87), pygame.Rect(0, self.win_height-75, self.win_width, 75))
        self.quit_button.draw(self.screen)
        if self.hand_seer.get_hand_gesture() == 'Pointing_Up':
            self.duck.jump()
        elif self.duck.jumping:
            self.duck.end_jump()
        self.duck.draw(self.screen)

        self.generate_obstacles()
        self.goose.draw(self.screen)

        if self.goose.check_collision(self.duck.get_rect()):
            rps_game = RPSGame.RPSGame(self.score_counter, self.hand_seer)
            rps_game.rock_paper_scissors_popup()
            self.goose.set_nonexist()

        rocks_to_delete = []
        for rock in self.rocks:
            if not rock.exists:
                rocks_to_delete.append(rock)
                break
            else:
                rock.draw(self.screen)
            if rock.check_collision(self.duck.get_rect()):
                print("You hit something")
                rock.exists = False
                rocks_to_delete.append(rock)
                if rock.is_peas:
                    self.score_counter.change_score(5)
                else:
                    game_end_popup(self.score_counter.score, 'rock')
                    self.end_game()
                    return

        for rock in rocks_to_delete:
            self.rocks.remove(rock)

        self.game_timer.draw(self.screen)
        self.score_counter.draw(self.screen)

    def end_game(self):
        """
        End the game and return to the start screen
        """
        self.hand_seer.stop_video()
        self.hand_seer = None
        self.rocks = None
        self.game_timer = None
        self.score_counter = None
        self.start_init()

    def abort_game(self):
        """
        Use this method if the X is pressed in the pygame window to close the program
        """
        if self.hand_seer is not None:
            self.hand_seer.stop_video()

    def screen_update(self):
        """
        Update the screen
        """
        if self.state == 1:
            if self.start_button.is_pressed():
                self.game_init()

            if self.help_button.is_pressed():
                game_instruction_popup()
                self.help_button.set_active()

        if self.state == 2:
            if self.quit_button.is_pressed():
                self.end_game()
            elif self.score_counter.score <= 0:
                game_end_popup(self.score_counter.score, 'peas')
                self.end_game()
            elif self.game_timer.time_left <= 0:
                game_end_popup(self.score_counter.score, 'time')
                self.end_game()
            else:
                self.update_game_screen()
