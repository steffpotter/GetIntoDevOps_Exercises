class WorkedTooMuchException(Exception):

    def __init__(self, hours_worked):
        self._hours_worked = hours_worked

    def __str__(self):
        return f"You worked {self._hours_worked} hours this week - naughty naughty"
