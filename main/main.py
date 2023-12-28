import logging

from main.char import Character
from main.stats import (
    BodyAttributes as BA,
    SoulAttributes as SA,
    Beliefs,
    Goals,
    Facets,
    AttributeType,
)

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


def generate_characters():
    char1 = Character(name="Aban", beliefs={}, goals=[], facets={}, attributes={})
    char2 = Character(name="Aban", beliefs={}, goals=[], facets={}, attributes={})
    char3 = Character(name="Aban", beliefs={}, goals=[], facets={}, attributes={})
    char4 = Character(name="Aban", beliefs={}, goals=[], facets={}, attributes={})
    char5 = Character(name="Aban", beliefs={}, goals=[], facets={}, attributes={})
    char6 = Character(name="Aban", beliefs={}, goals=[], facets={}, attributes={})
    char7 = Character(name="Aban", beliefs={}, goals=[], facets={}, attributes={})
