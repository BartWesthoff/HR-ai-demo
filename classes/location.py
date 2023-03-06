class Location:

    def __init__(self, house_number, street, city, country):
        self.house_number = house_number
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.house_number} {self.street}, {self.city}, {self.country}"

    def __eq__(self, other):
        return self.house_number == other.house_number and self.street == other.street \
            and self.city == other.city and self.country == other.country

    def __ne__(self, other):
        return not self.__eq__(other)
