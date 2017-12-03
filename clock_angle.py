def clock_angle(time):
    alphabet = "0123456789"
    numbers = 0
    i = 3
    for a in time:
        for b in alphabet:
            if a == b:
                numbers += alphabet.index(b) * (10 ** i)
                i -= 1
                break
    min = numbers % 100
    hour = (numbers - min) / 100
    if hour > 11:
        hour -= 12
    angle_min = min * 90 / 15
    angle_hour = (hour * 60 + min) * 90 / 180
    angle = angle_min - angle_hour
    if angle < 0:
        angle = angle * -1
    if angle > 180:
        angle = 360 - angle
    return angle


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("06:15") == 97.5, "Хитрый угол"
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
