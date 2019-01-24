"""A class for the airspeed velocity of an unladen swallow."""


class AirSpeedVelocityOfAnUnladenSwallow:
    """Class for the airspeed velocity of an unladen swallow."""

    species = 'European'
    meters_per_second = 11
    miles_per_hour = 24
    source = 'http://style.org/unladenswallow/'

    def what_is_the_airspeed_velocity_of_an_unladen_swallow(self):
        """Return the airspeed velocity of an unladen swallow."""
        answer = (
            'The airspeed velocity of a {0} swallow is {1} meters per '
            'second or {2} miles per hour. See {3} for more information.'
        ).format(
            self.species,
            self.meters_per_second,
            self.miles_per_hour,
            self.source)

        return answer
