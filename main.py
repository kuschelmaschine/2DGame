from ctypes.wintypes import RGB
import pygame
import time 




'''
    TODO:

    change color of font while rendering

    make nice particles
'''



running = True
NAME = "2D Game"
VERSION = "0.0.2"
WIDTH = 800
HEIGHT = 600

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption(NAME + " " + VERSION)

def clip(surf,x,y,x_size,y_size):
    handle_surf = surf.copy()
    clipR = pygame.Rect(x,y,x_size,y_size)
    handle_surf.set_clip(clipR)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()

class Font():
    def __init__(self, path):
        self.spacing = 1
        self.character_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']
        font_img = pygame.image.load(path).convert_alpha()
        font_img.set_colorkey((0, 0, 0))
        current_char_width = 0
        self.characters = {}
        character_count = 0
        for x in range(font_img.get_width()):
            c = font_img.get_at((x, 0))
            if c[0] == 127:
                char_img = clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
                sur_copy = char_img.copy()
                # this fucker changes the red to white 
                # i am sure there is a simpler method of doings this
                for y in range(sur_copy.get_height()):
                    for x in range(sur_copy.get_width()):
                        c: pygame.Color = sur_copy.get_at((x, y))
                        if c == pygame.Color(255, 0, 0):
                            sur_copy.set_at((x, y), (255, 255, 255))
                self.characters[self.character_order[character_count]] = sur_copy
                character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        self.space_width = self.characters['A'].get_width()

    def render(self, surf, text, loc, size):
        x_offset = 0
        for char in text:
            if char != ' ':
                current = self.characters[char]
                current = pygame.transform.scale(current, (current.get_width() * size, current.get_height() * size))
                surf.blit(current, (loc[0] + x_offset, loc[1]))
                x_offset += current.get_width() + self.spacing * size
            else:
                x_offset += self.space_width * size + self.spacing * size






my_big_font = Font('fonts\large_font.png')

tex_0 = pygame.image.load('textures\entities\entity_u_0.png').convert_alpha()
tex_1 = pygame.image.load('textures\entities\entity_u_1.png').convert_alpha()
tex_state: bool = False


def render_entity_u(tex_state: bool, x: int, y: int, scale: int):
    
    if tex_state:
        screen.blit(pygame.transform.scale(tex_0, (tex_0.get_width() * scale, tex_0.get_height() * scale)), (x, y))
    else :
        screen.blit(pygame.transform.scale(tex_1, (tex_1.get_width() * scale, tex_1.get_height() * scale)), (x, y))
    



start_time = time.time()

current_fps = 0
fps = 0

while running:


    # handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pass
            if event.key == pygame.K_s:
                pass
            if event.key == pygame.K_a:
                pass
            if event.key == pygame.K_d:
                pass

    current_fps += 1
    if time.time() - start_time >= 1 :
        start_time = time.time()
        tex_state = not tex_state
        fps = current_fps
        current_fps = 0

        
            
    
    # reset screen
    screen.fill((35, 39, 42))

    render_entity_u(tex_state, 200, 200, 4)

    my_big_font.render(screen, f"Fps: {fps}", (5, 5), 1)
    
    
    # update display
    pygame.display.update()
        


    


