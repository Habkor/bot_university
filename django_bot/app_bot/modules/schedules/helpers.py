

def week_of_month(date_value):
    """Получает номер недели из месяца."""
    week = date_value.isocalendar()[1] - date_value.replace(day=1).isocalendar()[1] + 1
    return date_value.isocalendar()[1] if week < 0 else week


def is_numerator_week(date_value):
    number_week = week_of_month(date_value)

    if number_week % 2 == 0:
        return 'numerator'
    else:
        return 'denominator'
