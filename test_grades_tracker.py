import grades_tracker


def test_get_top_student():
    students = grades_tracker.load_csv()
    result=grades_tracker.get_top_student(students)
    assert (result['name'] == 'Farid')
    assert (result['score'] == 91)
    assert (grades_tracker.get_top_student([]) == None)


def test_calc_average_score():
    students = grades_tracker.load_csv()
    result = grades_tracker.calc_average_score(students)
    assert (abs(result - 62.17) < 0.01)
    assert (grades_tracker.calc_average_score([]) == 0)


def test_count_passed():
    students = grades_tracker.load_csv()
    result = grades_tracker.count_passed(students)
    assert (result == 4)
    assert (grades_tracker.count_passed([]) == 0)
