import pygame
import sys

pygame.init()
pygame.font.init()

display = pygame.display.set_mode((640, 640))

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

board_boxs = [["a_a","a_b","a_c"],
              ["b_a","b_b","b_c"],
              ["c_a","c_b","c_c"]]

font = pygame.font.SysFont('arialblack', 40)

def update(f):

    pygame.display.flip()

    display.blit(f, (170,17.5))
    
def get_square_collision(mousePos, a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c):

    if a_a.collidepoint(mousePos):
        return "a_a"

    elif a_b.collidepoint(mousePos):
        return "a_b"

    elif a_c.collidepoint(mousePos):
        return "a_c"

    if b_a.collidepoint(mousePos):
        return "b_a"

    elif b_b.collidepoint(mousePos):
        return "b_b"

    elif b_c.collidepoint(mousePos):
        return "b_c"

    if c_a.collidepoint(mousePos):
        return "c_a"

    elif c_b.collidepoint(mousePos):
        return "c_b"

    elif c_c.collidepoint(mousePos):
        return "c_c"

def add_box(box, color, a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c):

    if (box == "a_a") and board[0][0] == 0:

        circX = a_a.x + 77.5
        circY = a_a.y + 77.5
        lineStartX = a_a.x + 20
        lineStartY = a_a.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[0][0] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[0][0] = 2
        
        return 0

    elif (box == "a_b") and board[0][1] == 0:

        circX = a_b.x + 77.5
        circY = a_b.y + 77.5
        lineStartX = a_b.x + 20
        lineStartY = a_b.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[0][1] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[0][1] = 2
        
        return 0
        
    elif (box == "a_c") and board[0][2] == 0:

        circX = a_c.x + 77.5
        circY = a_c.y + 77.5
        lineStartX = a_c.x + 20
        lineStartY = a_c.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[0][2] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[0][2] = 2
        
        return 0
        
    elif (box == "b_a") and board[1][0] == 0:

        circX = b_a.x + 77.5
        circY = b_a.y + 77.5
        lineStartX = b_a.x + 20
        lineStartY = b_a.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[1][0] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[1][0] = 2
        
        return 0
        
    elif (box == "b_b") and board[1][1] == 0:

        circX = b_b.x + 77.5
        circY = b_b.y + 77.5
        lineStartX = b_b.x + 20
        lineStartY = b_b.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[1][1] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[1][1] = 2
        
        return 0
        
    elif (box == "b_c") and board[1][2] == 0:

        circX = b_c.x + 77.5
        circY = b_c.y + 77.5
        lineStartX = b_c.x + 20
        lineStartY = b_c.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[1][2] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[1][2] = 2
        
        return 0
        
    elif (box == "c_a") and board[2][0] == 0:

        circX = c_a.x + 77.5
        circY = c_a.y + 77.5
        lineStartX = c_a.x + 20
        lineStartY = c_a.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[2][0] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[2][0] = 2
        
        return 0
        
    elif (box == "c_b") and board[2][1] == 0:

        circX = c_b.x + 77.5
        circY = c_b.y + 77.5
        lineStartX = c_b.x + 20
        lineStartY = c_b.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[2][1] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[2][1] = 2
        
        return 0
        
    elif (box == "c_c") and board[2][2] == 0:

        circX = c_c.x + 77.5
        circY = c_c.y + 77.5
        lineStartX = c_c.x + 20
        lineStartY = c_c.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[2][2] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[2][2] = 2
    
        return 0
    
    else:

        return -1
    
def redraw_box(box, color, a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c):

    if (box == "a_a"):

        circX = a_a.x + 77.5
        circY = a_a.y + 77.5
        lineStartX = a_a.x + 20
        lineStartY = a_a.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[0][0] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[0][0] = 2
        
        return 0

    elif (box == "a_b"):

        circX = a_b.x + 77.5
        circY = a_b.y + 77.5
        lineStartX = a_b.x + 20
        lineStartY = a_b.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[0][1] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[0][1] = 2
        
        return 0
        
    elif (box == "a_c"):

        circX = a_c.x + 77.5
        circY = a_c.y + 77.5
        lineStartX = a_c.x + 20
        lineStartY = a_c.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[0][2] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[0][2] = 2
        
        return 0
        
    elif (box == "b_a"):

        circX = b_a.x + 77.5
        circY = b_a.y + 77.5
        lineStartX = b_a.x + 20
        lineStartY = b_a.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[1][0] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[1][0] = 2
        
        return 0
        
    elif (box == "b_b"):

        circX = b_b.x + 77.5
        circY = b_b.y + 77.5
        lineStartX = b_b.x + 20
        lineStartY = b_b.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[1][1] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[1][1] = 2
        
        return 0
        
    elif (box == "b_c"):

        circX = b_c.x + 77.5
        circY = b_c.y + 77.5
        lineStartX = b_c.x + 20
        lineStartY = b_c.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[1][2] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[1][2] = 2
        
        return 0
        
    elif (box == "c_a"):

        circX = c_a.x + 77.5
        circY = c_a.y + 77.5
        lineStartX = c_a.x + 20
        lineStartY = c_a.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[2][0] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[2][0] = 2
        
        return 0
        
    elif (box == "c_b"):

        circX = c_b.x + 77.5
        circY = c_b.y + 77.5
        lineStartX = c_b.x + 20
        lineStartY = c_b.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[2][1] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[2][1] = 2
        
        return 0
        
    elif (box == "c_c"):

        circX = c_c.x + 77.5
        circY = c_c.y + 77.5
        lineStartX = c_c.x + 20
        lineStartY = c_c.y + 20
        lineEndX = lineStartX + 110
        lineEndY = lineStartY + 110

        if (color == "red"):
            
            pygame.draw.circle(display, (255,0,0), (circX, circY), 60, 10)
            board[2][2] = 1

        elif (color == "blue"):
            
            pygame.draw.line(display, (0,0,255), (lineStartX, lineStartY), (lineEndX, lineEndY), 15)
            pygame.draw.line(display, (0,0,255), (lineEndX, lineStartY), (lineStartX, lineEndY), 15)
            board[2][2] = 2
    
        return 0
    
    else:

        return -1

def redraw():
    display.fill((255,255,255)) 

    a_a = pygame.draw.rect(display, (0,0,0), pygame.Rect(95, 95, 150, 150), 5)
    a_b = pygame.draw.rect(display, (0,0,0), pygame.Rect(245, 95, 150, 150), 5)
    a_c = pygame.draw.rect(display, (0,0,0), pygame.Rect(395, 95, 150, 150), 5)

    b_a = pygame.draw.rect(display, (0,0,0), pygame.Rect(95, 245, 150, 150), 5)
    b_b = pygame.draw.rect(display, (0,0,0), pygame.Rect(245, 245, 150, 150), 5)
    b_c = pygame.draw.rect(display, (0,0,0), pygame.Rect(395, 245, 150, 150), 5)

    c_a = pygame.draw.rect(display, (0,0,0), pygame.Rect(95, 395, 150, 150), 5)
    c_b = pygame.draw.rect(display, (0,0,0), pygame.Rect(245, 395, 150, 150), 5)
    c_c = pygame.draw.rect(display, (0,0,0), pygame.Rect(395, 395, 150, 150), 5)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                redraw_box(board_boxs[i][j], "red", a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c)
            elif board[i][j] == 2:
                redraw_box(board_boxs[i][j], "blue", a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c)


    return a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c

def check_win():
    for i in range(len(board)):
            if (board[i][0] == board[i][1] == board[i][2] == 1):
                return "red"
            elif (board[i][0] == board[i][1] == board[i][2] == 2):
                return "blue"
    
    for i in range(len(board)):
            if (board[0][i] == board[1][i] == board[2][i] == 1):
                return "red"
            elif (board[0][i] == board[1][i] == board[2][i] == 2):
                return "blue"
    
    if (board[0][0] == board[1][1] == board[2][2] == 1):
        return "red"   
    elif (board[0][0] == board[1][1] == board[2][2] == 2):
        return "blue"
    elif (board[0][2] == board[1][1] == board[2][0] == 1):
        return "red"
    elif (board[0][2] == board[1][1] == board[2][0] == 2):
        return "blue"
    
    return "none"

def retry():
    retryRect = pygame.draw.rect(display, (255,255,255), pygame.Rect(200, 560, 255, 50))
    retryFont = pygame.font.SysFont('arialblack', 40)
    retryText = pygame.font.Font.render(font, "Play Again?", True, (0,0,0))
    display.blit(retryText, (200,555))
    return retryRect


def main():

    clicked = False
    playerTurn = 0
    a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c = redraw()
    playerTurnFont = pygame.font.Font.render(font, "Player 1 Turn", True, (0,0,0))
    won = False


    while True:

        if pygame.mouse.get_pressed()[0] and not clicked and not won:

            if (playerTurn == 0):
                square = get_square_collision(pygame.mouse.get_pos(), a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c)
                out = add_box(square, "red", a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c)
                clicked = True
            
            elif (playerTurn == 1):
                square = get_square_collision(pygame.mouse.get_pos(), a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c)
                out = add_box(square, "blue", a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c)
                clicked = True
            
            a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c = redraw()

            if (check_win() == "red"):
                playerTurnFont = pygame.font.Font.render(font, "   Red Wins!", True, (0,0,0))
                won = True
            elif (check_win() == "blue"):
                playerTurnFont = pygame.font.Font.render(font, "   Blue Wins!", True, (0,0,0))
                won = True
            else:
                if (out == 0):
                    if (playerTurn == 1):
                        playerTurn = 0
                        playerTurnFont = pygame.font.Font.render(font, "Player 1 Turn", True, (0,0,0))
                        
                    elif (playerTurn == 0):
                        playerTurn = 1 
                        playerTurnFont = pygame.font.Font.render(font, "Player 2 Turn", True, (0,0,0))
    

        if pygame.mouse.get_pressed()[0] and not clicked:
            clicked = True
            if retry().collidepoint(pygame.mouse.get_pos()):

                for i in range(3):
                    for j in range(3):
                        board[i][j] = 0
                
                playerTurnFont = pygame.font.Font.render(font, "Player 1 Turn", True, (0,0,0))
                redraw()
                playerTurn = 0
                won = False

        if (won):
            retry()


        
        if pygame.mouse.get_pressed()[0] == False:
            clicked = False

        update(playerTurnFont)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


main()
