# Graphique
RESOLUTION: tuple[int, int] = (1280, 720) # Inutile
PERSO_H_SCALE: float = 0.6
PERSO_V_SCALE: float = 0.8
COLOR_WALL: tuple[int, int, int] = (255, 0, 0)

# Map (taille mini = 5x5)
MAP_WIDTH: int = 10
MAP_HEIGHT: int = 10
PLAYER_SPAWN: tuple[int, int] = (MAP_WIDTH-1, MAP_HEIGHT-1)

# Controles
UP: tuple[int, int] = (0,-1)
DOWN: tuple[int, int] = (0,1)
LEFT: tuple[int, int] = (-1,0)
RIGHT: tuple[int, int] = (1,0)

# Chemins graphismes
PATH_PERSO: str = "ressources/images/perso/"
PATH_BACKGROUND: str = "ressources/images/fond.jpg"
PATH_CLE: str = "ressources/images/cle/"
PATH_CADRE: str = "ressources/images/border.png"

# Chemin audio
PATH_SOUNDS: str = "ressources/sons/"
BASE_OPEN_SOUND: str = "DoorOpening/"
BASE_CLOSED_SOUND: str = "DoorClosed/"
NAME_KEY_SOUND: str = "SwordStrike/SwordStrike.wav"
BASE_SWORD_SOUND: str = "SwordStrike/"
BASE_WALL_SOUND: str = "WallHiting/"