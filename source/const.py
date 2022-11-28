DEBUG = True

# Graphique
RESOLUTION: tuple[int, int] = (1280, 720) # Inutile
PERSO_H_SCALE: float = 0.6
PERSO_V_SCALE: float = 0.8
COLOR_WALL: tuple[int, int, int] = (255, 0, 0)

# Map (taille mini = 5x5)
MAP_WIDTH: int = 6
MAP_HEIGHT: int = 5
PLAYER_SPAWN: tuple[int, int] = (MAP_WIDTH-1, MAP_HEIGHT-1)
AMOUNT_ENNEMIES: int = 2

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
PATH_SORTIE: str = "ressources/images/perso/fin/BlindManWalkingInDoor"
PATH_INTRO: str = "ressources/images/perso/intro/"
PATH_DOOR_CLOSED: str = "ressources/images/door.png"
PATH_DEATH: str = "ressources/images/perso/mort/"

# Chemin audio
PATH_SOUNDS: str = "ressources/sons/"
BASE_DOOR_SOUND: str = "Door/"
NAME_KEY_SOUND: str = "KeyPickup.wav"
BASE_SWORD_SOUND: str = "Sword/"
BASE_WALL_SOUND: str = "WallHiting/"
BASE_ENNEMY_SOUND: str = "Gobelin/"
NAME_DEATH_SOUND: str = "mort.wav"
BASE_ENNEMY_SOUND: str = "Gobelin/"
