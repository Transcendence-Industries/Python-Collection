import time
import random
import pygame
import matplotlib.pyplot as plt
from itertools import cycle
from matplotlib import style

style.use("ggplot")

ARRAY_SIZE = 50
MIN_NUMBER = 1
MAX_NUMBER = 500
DELAY = 0.01
ALGORITHMS = ("bubble", "insertion", "selection", "quick")

SCREEN_SIZE = (1280, 720)
TEXT_COLOR = (255, 255, 255)
COLORS = (
    (0, 0, 0),  # Background
    (255, 255, 255),  # Elements
    (255, 0, 0),  # Marker
    (0, 255, 0)  # Swapper
)


class Sorter:
    def __init__(self):
        self.running = False
        self.array = []
        self.marker = ()
        self.swapper = ()
        self.algorithms = cycle(ALGORITHMS)
        self.method = next(self.algorithms)

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.font = pygame.font.Font(pygame.font.get_default_font(), 30)
        pygame.display.set_caption("Sort Visualizer")

        print()
        print("R - Random array")
        print("A - Change algorithm")
        print("S - Start sort")
        print("C - Compare algorithms")
        print()

    def main_loop(self):
        while True:
            # Handle key-events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                elif event.type == pygame.KEYDOWN and not self.running:
                    if event.key == pygame.K_r:
                        self.random_array()
                    elif event.key == pygame.K_a:
                        self.method = next(self.algorithms)
                    elif event.key == pygame.K_s and len(self.array) > 0:
                        self.sort()
                    elif event.key == pygame.K_c and len(self.array) > 0:
                        self.compare()
            self.update_screen(None)

    def update_screen(self, array):
        if not array:
            array = self.array

        self.screen.fill(COLORS[0])
        if len(array) > 0:
            for index, element in enumerate(array):
                bar = (SCREEN_SIZE[0] // (len(array) * 2 + 1) * (index * 2 + 1),
                       SCREEN_SIZE[1] - SCREEN_SIZE[1] // max(array) * element,
                       SCREEN_SIZE[0] // (len(array) * 2 + 1),
                       SCREEN_SIZE[1])

                if index in self.marker:
                    pygame.draw.rect(self.screen, COLORS[2], bar)
                elif index in self.swapper:
                    pygame.draw.rect(self.screen, COLORS[3], bar)
                else:
                    pygame.draw.rect(self.screen, COLORS[1], bar)

        text = self.font.render("Algorithm: " + self.method, True, TEXT_COLOR)
        self.screen.blit(text, (10, 10))
        pygame.display.flip()

    def random_array(self):
        self.array.clear()
        for _ in range(ARRAY_SIZE):
            self.array.append(random.randint(MIN_NUMBER, MAX_NUMBER))
        self.update_screen(None)

    def sort(self):
        # print(sorted(self.array))
        print("Algorithm:", self.method)
        self.running = True
        start_time = time.time()

        if self.method == "bubble":
            self.bubble_sort()
        elif self.method == "insertion":
            self.insertion_sort()
        elif self.method == "selection":
            self.selection_sort()
        elif self.method == "quick":
            self.array = self.quick_sort(self.array.copy())

        end_time = time.time()
        runtime = end_time - start_time
        self.running = False
        print("Runtime:", round(runtime, 5), "s")
        # print(self.array)
        return runtime

    def compare(self):
        cache = self.array.copy()
        runtimes = {}

        for algo in ("bubble", "insertion", "selection", "quick"):
            self.array = cache.copy()
            self.update_screen(None)
            self.method = algo
            runtime = self.sort()
            runtimes[algo] = round(runtime, 5)

        print("Runtimes:", runtimes)
        self.update_screen(None)

        x, y = zip(*sorted(runtimes.items()))
        plt.plot(x, y)
        plt.show()

    def bubble_sort(self):
        for i in range(len(self.array)):
            for j in range(len(self.array) - 1):
                # Visualization
                self.marker = (j, j + 1)
                self.swapper = ()
                self.update_screen(None)
                time.sleep(DELAY)

                if self.array[j] > self.array[j + 1]:
                    cache = self.array[j]
                    self.array[j] = self.array[j + 1]
                    self.array[j + 1] = cache

                    # Visualization
                    self.marker = ()
                    self.swapper = (j, j + 1)
                    self.update_screen(None)
                    time.sleep(DELAY)

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            cache = self.array[i]
            j = i

            while j > 0 and self.array[j - 1] > cache:
                self.array[j] = self.array[j - 1]
                j -= 1

                # Visualization
                self.marker = (i, j)
                self.swapper = ()
                self.update_screen(None)
                time.sleep(DELAY)
            self.array[j] = cache

            # Visualization
            self.marker = ()
            self.swapper = (i, j)
            self.update_screen(None)
            time.sleep(DELAY)

    def selection_sort(self):
        high_index = len(self.array)
        insert_index = 0

        while insert_index < high_index:
            min_position = insert_index

            for i in range(insert_index + 1, high_index):
                # Visualization
                self.marker = (i,)
                self.swapper = ()
                self.update_screen(None)
                time.sleep(DELAY)

                if self.array[i] < self.array[min_position]:
                    min_position = i

            # Visualization
            self.marker = ()
            self.swapper = (min_position, insert_index)
            self.update_screen(None)
            time.sleep(DELAY)

            cache = self.array[min_position]
            self.array[min_position] = self.array[insert_index]
            self.array[insert_index] = cache
            insert_index += 1

    def quick_sort(self, array):
        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0]
            for i in array:
                if i < pivot:
                    less.append(i)
                elif i == pivot:
                    equal.append(i)
                elif i > pivot:
                    greater.append(i)

            # Visualization
            self.update_screen(array)
            time.sleep(DELAY)
            return self.quick_sort(less) + equal + self.quick_sort(greater)
        else:
            return array


if __name__ == "__main__":
    pygame.init()
    sorter = Sorter()
    sorter.main_loop()
