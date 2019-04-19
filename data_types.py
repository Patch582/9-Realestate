class Purchase:
    def __init__(
            self, ref, Address1, Address2, Suburb, Postcode,
            State, Type, Squares, Beds, Bathrooms, Toilets, Cars, Garage,
            Sale_price, Sale_date, Latitude, Longitude):
        self.ref = ref,
        self.Address1 = Address1,
        self.Address2 = Address2,
        self.Suburb = Suburb,
        self.Postcode = Postcode,
        self.State = State,
        self.Type = Type,
        self.Squares = Squares,
        self.Beds = Beds,
        self.Bathrooms = Bathrooms,
        self.Toilets = Toilets,
        self.Cars = Cars,
        self.Garage = Garage,
        self.Sale_price = Sale_price,
        self.Sale_date = Sale_date,
        self.Latitude = Latitude,
        self.Longitude = Longitude

    @staticmethod
    def create_from_dict(lookup):
        return Purchase(
            int(lookup['ref']),
            lookup['Address1'],
            lookup['Address2'],
            lookup['Suburb'],
            lookup['Postcode'],
            lookup['State'],
            lookup['Type'],
            int(lookup['Squares']),
            int(lookup['Beds']),
            int(lookup['Bathrooms']),
            int(lookup['Toilets']),
            int(lookup['Cars']),
            int(lookup['Garage']),
            float(lookup['Sale_price']),
            lookup['Sale_date'],
            lookup['Latitude'],
            lookup['Longitude'])
