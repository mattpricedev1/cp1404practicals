from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi class."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initial SilverServiceTaxi variables."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string representation of SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get fare with added flagfall."""
        return self.flagfall + super().get_fare()
