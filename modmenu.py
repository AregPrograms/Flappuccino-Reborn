import pygame


class ModMenu:
    def __init__(self):
        self.frame = pygame.Surface((200, 250), pygame.SRCALPHA)
        self.config = {
            "speed":  60,
            "freeUpgrades": False,
            "noHealth": False
        }

    def update(self, font: pygame.font.Font):
        # semi-transparent background
        #self.frame.fill((0, 0, 0, 100))
        #semiTransparent = (0, 0, 0, 100)

        pygame.draw.rect(self.frame, (171, 145, 123), (0, 0, 200, 100),
                         border_top_left_radius=10, border_top_right_radius=10)
        pygame.draw.rect(self.frame, (231, 205, 183), (0, 30, 200, 220),
                         border_bottom_left_radius=10, border_bottom_right_radius=10)

        title = font.render("Mod Menu", True, (255, 255, 255))
        self.frame.blit(title, (100 - (title.get_width()/2),
                        15 - (title.get_height()/2)))
        
        free_upgrades_btn = pygame.image.load("./data/gfx/buttons/free_upgrades.png").convert_alpha()
        no_health_btn = pygame.transform.scale(pygame.image.load("./data/gfx/buttons/nohealth.png").convert_alpha(), free_upgrades_btn.get_size())
        q = pygame.image.load("./data/gfx/buttons/q.png").convert_alpha()
        e = pygame.image.load("./data/gfx/buttons/e.png").convert_alpha()
        enabled = pygame.transform.scale(pygame.image.load("./data/gfx/buttons/enabled.png").convert_alpha(), (64, 32))
        disabled = pygame.transform.scale(pygame.image.load("./data/gfx/buttons/disabled.png").convert_alpha(), (64, 32))
        
        self.frame.blit(free_upgrades_btn, (100 - (free_upgrades_btn.get_width()/2),
                        50 - (free_upgrades_btn.get_height()/2)))
        
        self.frame.blit(q, (100 - (free_upgrades_btn.get_width()/2),
                        73 - (q.get_height()/2)))
     

        # Free Upgrade Code
        if self.config["freeUpgrades"]:
            self.frame.blit(enabled, (100 - (free_upgrades_btn.get_width()/2) + free_upgrades_btn.get_width() - enabled.get_width(),
                        73 - (enabled.get_height()/2)))   
        elif not self.config["freeUpgrades"]:
            self.frame.blit(disabled, (100 - (free_upgrades_btn.get_width()/2) + free_upgrades_btn.get_width() - enabled.get_width(),
                        73 - (enabled.get_height()/2)))   
        else:
            self.config["freeUpgrades"] = False  # just in case

        self.frame.blit(no_health_btn, (100 - (no_health_btn.get_width()/2),
                        110 - (no_health_btn.get_height()/2)))
        
        self.frame.blit(e, (100 - (no_health_btn.get_width()/2),
                        133 - (e.get_height()/2)))

        # No Health Code
        if self.config["noHealth"]:
            self.frame.blit(enabled, (100 - (free_upgrades_btn.get_width()/2) + free_upgrades_btn.get_width() - enabled.get_width(),
                        133 - (enabled.get_height()/2)))   
        elif not self.config["noHealth"]:
            self.frame.blit(disabled, (100 - (free_upgrades_btn.get_width()/2) + free_upgrades_btn.get_width() - enabled.get_width(),
                        133 - (enabled.get_height()/2)))   
        else:
            self.config["noHealth"] = False  # just in case
