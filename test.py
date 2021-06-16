import pygame
pygame.init()

HEIGHT = 700
WIDTH = 700

Display = pygame.display.set_mode((HEIGHT, WIDTH))

def main():
    run = True
    x_a = 50
    y_a = 650
    x_b = 150
    y_b = 650
    x_c = 250
    y_c = 650
    x_d = 350
    y_d = 650
    x_e = 450
    y_e = 650
    x_f = 550
    y_f = 650
    x_g = 650
    y_g = 650
    move_a = 1
    move_b = 2
    move_c = 3
    move_d = 4
    move_e = 5
    move_f = 6
    move_g = 7
    player_turn = 1
    player_one = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]
    player_two = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42]
    one_moves = []
    two_moves = []
    textX = 200
    textY = 10
    while run:
        draw_grid()
        pygame.display.flip()
        font = pygame.font.Font('freesansbold.ttf', 32)
        for element in one_moves:
            if element in one_moves and element + 1 in one_moves and element + 2 in one_moves and element + 3 in one_moves:
                message = font.render("Player one wins!", True, (255, 255, 255))
                Display.blit(message, (textX, textY))
                player_turn = 100
            elif element in one_moves and element + 7 in one_moves and element + 14 in one_moves and element + 21 in one_moves:
                message = font.render("Player one wins!", True, (255, 255, 255))
                Display.blit(message, (textX, textY))
                player_turn = 100
            elif element in one_moves and element + 8 in one_moves and element + 16 in one_moves and element + 24 in one_moves:
                message = font.render("Player one wins!", True, (255, 255, 255))
                Display.blit(message, (textX, textY))
                player_turn = 100
        for element in two_moves:
            if element in two_moves and element + 1 in two_moves and element + 2 in two_moves and element + 3 in two_moves:
                message = font.render("Player two wins!", True, (255, 255, 255))
                Display.blit(message, (textX, textY))
                player_turn = 100
            elif element in two_moves and element + 7 in two_moves and element + 14 in two_moves and element + 21 in two_moves:
                message = font.render("Player two wins!", True, (255, 255, 255))
                Display.blit(message, (textX, textY))
                player_turn = 100
            elif element in two_moves and element + 8 in two_moves and element + 16 in two_moves and element + 24 in two_moves:
                message = font.render("Player two wins!", True, (255, 255, 255))
                Display.blit(message, (textX, textY))
                player_turn = 100
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if player_turn in player_one and y_a > 50:
                        pygame.draw.circle(Display, (255, 0, 0), (x_a, y_a), 50)
                        y_a = y_a - 100
                        player_turn = player_turn + 1
                        one_moves.append(move_a)
                        move_a = move_a + 7
                    elif player_turn in player_two and y_a > 50:
                        pygame.draw.circle(Display, (255, 255, 0), (x_a, y_a), 50)
                        y_a = y_a - 100
                        player_turn = player_turn + 1
                        two_moves.append(move_a)
                        move_a = move_a + 7
                elif event.key == pygame.K_b:
                    if player_turn in player_one and y_b > 50:
                        pygame.draw.circle(Display, (255, 0, 0), (x_b, y_b), 50)
                        y_b = y_b - 100
                        player_turn = player_turn + 1
                        one_moves.append(move_b)
                        move_b = move_b + 7
                    elif player_turn in player_two and y_b > 50:
                        pygame.draw.circle(Display, (255, 255, 0), (x_b, y_b), 50)
                        y_b = y_b - 100
                        player_turn = player_turn + 1
                        two_moves.append(move_b)
                        move_b = move_b + 7
                elif event.key == pygame.K_c:
                    if player_turn in player_one and y_c > 50:
                        pygame.draw.circle(Display, (255, 0, 0), (x_c, y_c), 50)
                        y_c = y_c - 100
                        player_turn = player_turn + 1
                        one_moves.append(move_c)
                        move_c = move_c + 7
                    elif player_turn in player_two and y_c > 50:
                        pygame.draw.circle(Display, (255, 255, 0), (x_c, y_c), 50)
                        y_c = y_c - 100
                        player_turn = player_turn + 1
                        two_moves.append(move_c)
                        move_c = move_c + 7
                elif event.key == pygame.K_d:
                    if player_turn in player_one and y_d > 50:
                        pygame.draw.circle(Display, (255, 0, 0), (x_d, y_d), 50)
                        y_d = y_d - 100
                        player_turn = player_turn + 1
                        one_moves.append(move_d)
                        move_d = move_d + 7
                    elif player_turn in player_two and y_d > 50:
                        pygame.draw.circle(Display, (255, 255, 0), (x_d, y_d), 50)
                        y_d = y_d - 100
                        player_turn = player_turn + 1
                        two_moves.append(move_d)
                        move_d = move_d + 7
                elif event.key == pygame.K_e:
                    if player_turn in player_one and y_e > 50:
                        pygame.draw.circle(Display, (255, 0, 0), (x_e, y_e), 50)
                        y_e = y_e - 100
                        player_turn = player_turn + 1
                        one_moves.append(move_e)
                        move_e = move_e + 7
                    elif player_turn in player_two and y_e > 50:
                        pygame.draw.circle(Display, (255, 255, 0), (x_e, y_e), 50)
                        y_e = y_e - 100
                        player_turn = player_turn + 1
                        two_moves.append(move_e)
                        move_e = move_e + 7
                elif event.key == pygame.K_f:
                    if player_turn in player_one and y_f > 50:
                        pygame.draw.circle(Display, (255, 0, 0), (x_f, y_f), 50)
                        y_f = y_f - 100
                        player_turn = player_turn + 1
                        one_moves.append(move_f)
                        move_f = move_f + 7
                    elif player_turn in player_two and y_f > 50:
                        pygame.draw.circle(Display, (255, 255, 0), (x_f, y_f), 50)
                        y_f = y_f - 100
                        player_turn = player_turn + 1
                        two_moves.append(move_f)
                        move_f = move_f + 7
                elif event.key == pygame.K_g:
                    if player_turn in player_one and y_g > 50:
                        pygame.draw.circle(Display, (255, 0, 0), (x_g, y_g), 50)
                        y_g = y_g - 100
                        player_turn = player_turn + 1
                        one_moves.append(move_g)
                        move_g = move_g + 7
                    elif player_turn in player_two and y_g > 50:
                        pygame.draw.circle(Display, (255, 255, 0), (x_g, y_g), 50)
                        y_g = y_g - 100
                        player_turn = player_turn + 1
                        two_moves.append(move_g)
                        move_g = move_g + 7


def draw_grid():
    for x in range(0, WIDTH, 100):
        for y in range(100, HEIGHT, 100):
            rect = pygame.Rect(x, y, 100, 100)
            pygame.draw.rect(Display, (255, 255, 255), rect, 1)




main()





