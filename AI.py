import pygame
pygame.font.init()
screen = pygame.display.set_mode((500, 500))
x = 0
y = 0
dif = 500 / 9
val = 0

grid =[
          [2,3 , 5, 0, 8, 6, 0, 4, 1],
          [6, 0, 0, 4, 2, 1, 0, 0, 3],
          [9, 0, 4, 3, 0, 7, 2, 8, 0],
          [0, 7, 2, 0, 3, 5, 0, 1, 9],
          [0, 6, 8, 0, 1, 0, 5, 7, 4],
          [5, 9, 1, 7 , 6, 4, 8, 3,2],
          [1, 4, 0, 5, 7, 2, 0, 9, 8],
          [8, 5, 9, 6, 0, 3, 1, 2, 7],
          [7, 0, 3, 0, 0, 8, 4, 6, 0]
    ]
 

font1 = pygame.font.SysFont("comicsans", 30)
font2 = pygame.font.SysFont("comicsans", 20)
def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif
 

def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)  
        
def draw():
    
        
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:
 

                pygame.draw.rect(screen, (200, 100, 50), (i * dif, j * dif, dif + 1, dif + 1))
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
       
    for i in range(10):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)     
 
# Fill value entered 
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))   
 

def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 
def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 
 

def valid(m, i, j, val):
    
                
    return True
 

 

def result():
    text1 = font1.render("FINISHED ", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))   
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

while run:
     
    
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1   
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2   
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9 
            if event.key == pygame.K_RETURN:
                flag2 = 1  
            
          
   
    if val != 0:           
        draw_val(val)
        
        if valid(grid, int(x), int(y), val)== True:
            grid[int(x)][int(y)]= val
            flag1 = 0
        else:
            grid[int(x)][int(y)]= 0
            raise_error2()  
        val = 0   
       
    if error == 1:
        raise_error1() 
    if rs == 1:
        result()       
    draw() 
    if flag1 == 1:
        draw_box()      
    
 
    
    pygame.display.update() 
 
  
pygame.quit()    
   