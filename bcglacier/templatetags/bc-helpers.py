from django import template

register = template.Library()

@register.filter
def subtract(value, counter):
    if value is None:
        return 1
    else:
        return counter - value

@register.filter(name='range')
def filter_range(start, end):
  return range(start, end)

@register.filter
def getStar(value, counter):

    # if no ratings, value will be None, just print empty star
    if value is None:
        return "star-empty"

    # get difference between loop counter (which star in sequence of 5) and the average rating
    difference = counter - value

    # if rating is higher than counter, filled star
    if difference <= 0:
        return "star-filled"
    # if rating is less than counter (current star), empty star
    elif difference >= 1:
        return "star-empty"
    # for fractional stars, figure out which to print
    else:
        if difference > 0.5:
            return "star-quarter"
        elif difference > 0.25:
            return "star-half"
        else:
            return "star-three-quarters"
