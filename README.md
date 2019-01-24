# Unladen Swallow
Release v1.0 by [Karl Saint Lucy](https://karlsaintlucy.com).

## Installation

```bash
$ pip install UnladenSwallow
```

## Features
Returns the airspeed velocity of an unladen swallow. You have to know these sorts of things when you’re a king, you know.

## Usage
It’s very easy to find the airspeed velocity of an unladen swallow:

```python
>>> from unladen_swallow import AirSpeedVelocityOfAnUnladenSwallow
>>> a = AirSpeedVelocityOfAnUnladenSwallow()
<unladen_swallow.AirSpeedVelocityOfAnUnladenSwallow object at 0x123456789>
>>> a.what_is_the_air_speed_velocity_of_an_unladen_swallow()
'The airspeed velocity of a European swallow is 11 meters per second or 24
miles per hour. See http://style.org/unladenswallow/ for more information.'
```

Codebase

```python
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
```

## License
This project is licensed under the [BSD License](https://opensource.org/licenses/BSD-2-Clause).