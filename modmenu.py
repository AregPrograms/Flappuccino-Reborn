import pygame

class ModMenu:
    
    def __init__(self):
        self.frame = pygame.Surface((200, 250), pygame.SRCALPHA)
        self.config = {
            "speed":  60
        }
        
    def update(self, font: pygame.font.Font):
        self.frame.fill((0, 0, 0, 0))
        
        pygame.draw.rect(self.frame, (171, 145, 123), (0, 0, 200, 30), border_top_left_radius=10, border_top_right_radius=10)
        pygame.draw.rect(self.frame, (231, 205, 183), (0, 30, 200, 220), border_bottom_left_radius=10, border_bottom_right_radius=10)
        
        title = font.render("Mod Menu", True, (255, 255, 255))
        self.frame.blit(title, (100 - (title.get_width()/2), 15 - (title.get_height()/2)))