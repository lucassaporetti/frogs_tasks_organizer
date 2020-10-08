import uuid
from src.model.entity_model import Entity


class Task(Entity):
    @staticmethod
    def of(values: list):
        return Task(
            str(values[0]), str(values[1]), str(values[2]),
            str(values[3]), str(values[4]), str(values[5]),
            int(values[6]), int(values[7]), int(values[8]), int(values[9]),
            int(values[10]), int(values[11]), int(values[12]), int(values[13]),
            int(values[14]), int(values[15]), int(values[16]), int(values[17]),
            int(values[18]), int(values[19]), float(values[20]), str(values[21]),
            str(values[22]), str(values[23]), str(values[24]), str(values[25]), str(values[26])
        )

    def __init__(self, id: str = None, name: str = None, category: str = None, item_type: str = None,
                 description: str = None, attributes: str = None, consume_mp: int = None,
                 consume_heart: int = None, statistics_hp: int = None, statistics_mp: int = None,
                 statistics_heart: int = None, statistics_str: int = None, statistics_att: int = None,
                 statistics_gold: int = None, statistics_con: int = None, statistics_def: int = None,
                 statistics_max_ht: int = None, statistics_int: int = None, statistics_lck: int = None,
                 statistics_max_hp: int = None, sell: float = None, found_at: str = None,
                 dropped_by: str = None, effect: str = None, image: str = None, animation: str = None,
                 special_animation: str = None):
        super().__init__(id)
        self.name = name
        self.category = category
        self.item_type = item_type
        self.description = description
        self.attributes = attributes
        self.consume_mp = consume_mp
        self.consume_heart = consume_heart
        self.statistics_hp = statistics_hp
        self.statistics_mp = statistics_mp
        self.statistics_heart = statistics_heart
        self.statistics_str = statistics_str
        self.statistics_att = statistics_att
        self.statistics_gold = statistics_gold
        self.statistics_con = statistics_con
        self.statistics_def = statistics_def
        self.statistics_max_ht = statistics_max_ht
        self.statistics_int = statistics_int
        self.statistics_lck = statistics_lck
        self.statistics_max_hp = statistics_max_hp
        self.sell = sell
        self.found_at = found_at
        self.dropped_by = dropped_by
        self.effect = effect
        self.image = image
        self.animation = animation
        self.special_animation = special_animation

    def __str__(self):
        return "{} | {} | {} | {} | {} | {} | {} | {} | {} | {}" \
               "{} | {} | {} | {} | {} | {} | {} | {} | {} | {}" \
               "{} | {} | {} | {} | {}".format(
                super().__str__(), self.name, self.category, self.item_type, self.description,
                self.attributes, self.consume_mp, self.consume_heart, self.statistics_hp, self.statistics_mp,
                self.statistics_heart, self.statistics_str, self.statistics_att, self.statistics_gold,
                self.statistics_con, self.statistics_def, self.statistics_max_ht, self.statistics_int,
                self.statistics_lck, self.statistics_max_hp, self.sell, self.found_at, self.dropped_by,
                self.effect, self.image, self.animation, self.special_animation)

    class Builder:
        def __init__(self):
            self.id = str(uuid.uuid4())
            self.name = None
            self.category = None
            self.item_type = None
            self.description = None
            self.attributes = None
            self.consume_mp = None
            self.consume_heart = None
            self.statistics_hp = None
            self.statistics_mp = None
            self.statistics_heart = None
            self.statistics_str = None
            self.statistics_att = None
            self.statistics_gold = None
            self.statistics_con = None
            self.statistics_def = None
            self.statistics_max_ht = None
            self.statistics_int = None
            self.statistics_lck = None
            self.statistics_max_hp = None
            self.sell = None
            self.found_at = None
            self.dropped_by = None
            self.effect = None
            self.image = None
            self.animation = None
            self.special_animation = None

        def with_name(self, name: str):
            self.name = name
            return self

        def with_category(self, category: str):
            self.category = category
            return self

        def with_item_type(self, item_type: str):
            self.item_type = item_type
            return self

        def with_description(self, description: str):
            self.description = description
            return self

        def with_attributes(self, attributes: str):
            self.attributes = attributes
            return self

        def with_consume_mp(self, consume_mp: int):
            self.consume_mp = consume_mp
            return self

        def with_consume_heart(self, consume_heart: int):
            self.consume_heart = consume_heart
            return self

        def with_statistics_hp(self, statistics_hp: int):
            self.statistics_hp = statistics_hp
            return self

        def with_statistics_mp(self, statistics_mp: int):
            self.statistics_mp = statistics_mp
            return self

        def with_statistics_heart(self, statistics_heart: int):
            self.statistics_heart = statistics_heart
            return self

        def with_statistics_str(self, statistics_str: int):
            self.statistics_str = statistics_str
            return self

        def with_statistics_att(self, statistics_att: int):
            self.statistics_att = statistics_att
            return self

        def with_statistics_gold(self, statistics_gold: int):
            self.statistics_gold = statistics_gold
            return self

        def with_statistics_con(self, statistics_con: int):
            self.statistics_con = statistics_con
            return self

        def with_statistics_def(self, statistics_def: int):
            self.statistics_def = statistics_def
            return self

        def with_statistics_max_ht(self, statistics_max_ht: int):
            self.statistics_max_ht = statistics_max_ht
            return self

        def with_statistics_int(self, statistics_int: int):
            self.statistics_int = statistics_int
            return self

        def with_statistics_lck(self, statistics_lck: int):
            self.statistics_lck = statistics_lck
            return self

        def with_statistics_max_hp(self, statistics_max_hp: int):
            self.statistics_max_hp = statistics_max_hp
            return self

        def with_sell(self, sell: float):
            self.sell = sell
            return self

        def with_found_at(self, found_at: str):
            self.found_at = found_at
            return self

        def with_dropped_by(self, dropped_by: str):
            self.dropped_by = dropped_by
            return self

        def with_effect(self, effect: str):
            self.effect = effect
            return self

        def with_image(self, image: str):
            self.image = image
            return self

        def with_animation(self, animation: str):
            self.animation = animation
            return self

        def with_special_animation(self, special_animation: str):
            self.special_animation = special_animation
            return self

        def build(self):
            return Task(self.id, self.name, self.category, self.item_type, self.description, self.attributes,
                        self.consume_mp, self.consume_heart, self.statistics_hp, self.statistics_mp,
                        self.statistics_heart, self.statistics_str, self.statistics_att, self.statistics_gold,
                        self.statistics_con, self.statistics_def, self.statistics_max_ht, self.statistics_int,
                        self.statistics_lck, self.statistics_max_hp, self.sell, self.found_at, self.dropped_by,
                        self.effect, self.image, self.animation, self.special_animation)
