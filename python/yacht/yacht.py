from collections import Counter


class Category:
    def __init__(self, dice):
        self.dice = dice

    def _is_valid(self):
        return True

    def _calculate_score(self):
        return 0

    @property
    def score(self):
        if self._is_valid():
            return self._calculate_score()
        return 0


class MultiplierCategory(Category):
    """
    A Multiplier Category multiplies the number of items it finds by the
    configured multiplier.
    """
    multiplier = 0

    def _is_valid(self):
        return True

    def _calculate_score(self):
        return self.multiplier * self.dice.count(self.multiplier)


class OnesCategory(MultiplierCategory):
    multiplier = 1


class TwosCategory(MultiplierCategory):
    multiplier = 2


class ThreesCategory(MultiplierCategory):
    multiplier = 3


class FoursCategory(MultiplierCategory):
    multiplier = 4


class FivesCategory(MultiplierCategory):
    multiplier = 5


class SixesCategory(MultiplierCategory):
    multiplier = 6


class ConstantCategory(Category):
    """
    A Constant Category always returns a constant value if the dice are
    valid for the category.
    """
    constant = 0

    def _calculate_score(self):
        return self.constant


class YachtCategory(ConstantCategory):
    constant = 50

    def _is_valid(self):
        return self.dice.count(self.dice[0]) == 5


class LittleStraightCategory(ConstantCategory):
    constant = 30

    def _is_valid(self):
        return list(sorted(self.dice)) == [1, 2, 3, 4, 5]


class BigStraightCategory(ConstantCategory):
    constant = 30

    def _is_valid(self):
        return list(sorted(self.dice)) == [2, 3, 4, 5, 6]


class SumCategory(Category):
    """
    A SumCategory sums the thrown values of the dice.
    """
    def _calculate_score(self):
        return sum(self.dice)


class FullHouseCategory(SumCategory):
    """
    A Full House sums the dice if the dice are a valid Full House.
    """
    def _is_valid(self):
        counted_values = Counter(self.dice).most_common()
        three_value, three_count = counted_values[0]
        return len(counted_values) == 2 and three_count == 3


class FourOfAKindCategory(Category):
    """
    A Four of a Kind sums the four dice with the same face value.
    """
    def __init__(self, dice):
        super().__init__(dice)
        self.four_value = 0

    def _is_valid(self):
        counted_dice = Counter(self.dice).most_common()
        self.four_value, four_count = counted_dice[0]
        return four_count >= 4

    def _calculate_score(self):
        return self.four_value * 4


YACHT = YachtCategory
ONES = OnesCategory
TWOS = TwosCategory
THREES = ThreesCategory
FOURS = FoursCategory
FIVES = FivesCategory
SIXES = SixesCategory
FULL_HOUSE = FullHouseCategory
FOUR_OF_A_KIND = FourOfAKindCategory
LITTLE_STRAIGHT = LittleStraightCategory
BIG_STRAIGHT = BigStraightCategory
CHOICE = SumCategory


def score(dice, category):
    return category(dice).score
