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
        self.frame.fill((0, 0, 0, 100))
        semiTransparent = (0, 0, 0, 100)

        green = (0, 255, 0)
        red = (255, 0, 0)

        pygame.draw.rect(self.frame, (171, 145, 123), (0, 0, 200, 100),
                         border_top_left_radius=10, border_top_right_radius=10)
        pygame.draw.rect(self.frame, (231, 205, 183), (0, 30, 200, 220),
                         border_bottom_left_radius=10, border_bottom_right_radius=10)

        title = font.render("Mod Menu", True, (255, 255, 255))
        self.frame.blit(title, (100 - (title.get_width()/2),
                        15 - (title.get_height()/2)))

        # Free Upgrade Code
        if self.config["freeUpgrades"]:
            fUp = font.render("Free Upgrades", True, green)
        elif not self.config["freeUpgrades"]:
            fUp = font.render("Free Upgrades", True, red)
        else:
            self.config["freeUpgrades"] = False  # just in case

        # render hotkey
        fUpHotkey = font.render("F1", True, (255, 255, 255))

        self.frame.blit(fUp, (100 - (fUp.get_width()/2),
                        50 - (fUp.get_height()/2)))
        self.frame.blit(
            fUpHotkey, (100 - (fUpHotkey.get_width()/2), 70 - (fUpHotkey.get_height()/2)))

        # No Health Code
        if self.config["noHealth"]:
            nH = font.render("No Health", True, green)
        elif not self.config["noHealth"]:
            nH = font.render("No Health", True, red)
        else:
            self.config["noHealth"] = False  # just in case

        # render hotkey
        nHHotkey = font.render("F2", True, (255, 255, 255))

        self.frame.blit(nH, (100 - (nH.get_width()/2),
                        100 - (nH.get_height()/2)))
        self.frame.blit(nHHotkey, (100 - (nHHotkey.get_width()/2),
                        120 - (nHHotkey.get_height()/2)))
