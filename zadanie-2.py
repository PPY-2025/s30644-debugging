def get_grades():
    return [5, 4, "3", 2, 1]

def calculate_average(grades):
    grades_sum = 0

    for grade in grades:
        try:
            grades_sum += int(grade)
        except ValueError:
            raise ValueError("Zly format danych! Nie mozna obliczyc sredniej") from None

    return grades_sum / len(grades)

# Znaleziony błąd w calculate_average(): Oceny zapisane w formacie string nie mogły być dodane do sumy
# Dodano zabezpieczenie przed nieprawidłowym typem danych

def to_word_grade(avg):
    if avg >= 4.5:
        return "bardzo dobry"
    elif avg >= 3.5:
        return "dobry"
    elif avg >= 2.5:
        return "dostateczny"
    else:
        return "niedostateczny"

def show_result():
    grades = get_grades()
    avg = calculate_average(grades)
    word = to_word_grade(avg)
    print(f"Średnia: {avg:.2f}, Ocena: {word}")

# Testy:
def test_get_grades():
    assert get_grades() == [5, 4, "3", 2, 1]

def test_calculate_average():
    assert calculate_average(get_grades()) == 3

def test_to_word_grade():
    assert to_word_grade(calculate_average(get_grades())) == "dostateczny"
    assert to_word_grade(5) == "bardzo dobry"
    assert to_word_grade(4.5) == "bardzo dobry"
    assert to_word_grade(4) == "dobry"
    assert to_word_grade(3.5) == "dobry"
    assert to_word_grade(3) == "dostateczny"
    assert to_word_grade(2.5) == "dostateczny"
    assert to_word_grade(2) == "niedostateczny"

if __name__ == '__main__':
    show_result()