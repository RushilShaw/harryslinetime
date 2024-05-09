def get_screenshot():
    pass


def count_number_of_people():
    pass


def number_of_people_to_time_prediction():
    pass


def update_database():
    pass


def main():
    screen_shot_img = get_screenshot()
    number_of_people = count_number_of_people(screen_shot_img)
    time_estimate = number_of_people_to_time_prediction(number_of_people)
    update_database(time_estimate)


if __name__ == '__main__':
    main()