class Inventory(object):
    def __init__(self, items):
        self.items = items
        self.date = 123

    def add():
        pass

    def update_inventory():
        pass


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    @property
    def name(self):
        return self.__name
    
    @property
    def sell_in(self):
        return self.__sell_in

    @property
    def quality(self):
        return self.__quality 

    @name.setter
    def name(self, value):
        self.__name = value

    @sell_in.setter
    def sell_in(self, value):
        self.__sell_in = value
    
    @quality.setter
    def quality(self, value):
        self.__quality = value

    def __eq__(self, other):
        return self.name == other.name \
               and self.sell_in == other.sell_in \
               and self.quality == other.quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Updateable:
    def update_quality():
        pass


class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def set_sell_in(self):
        self.sell_in -= 1

    def setQuality(self, valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.set_sell_in()


class AgedBrie(NormalItem):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.set_sell_in()


# menos días más calidad


class Sulfuras(NormalItem):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_quality(self):
        self.quality = 80


class BackstagePasses(NormalItem):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality(1)
        elif self.sell_in > 5:
            self.setQuality(2)
        elif self.sell_in > 0:
            self.setQuality(3)
        else:
            self.quality = 0
        self.set_sell_in()