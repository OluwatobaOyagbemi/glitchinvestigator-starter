from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_comparison_is_numeric_not_string():
    # As strings "9" > "10", but as ints 9 < 10, so this must be "Too Low"
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"


def test_hard_range_is_larger_than_normal():
    from logic_utils import get_range_for_difficulty
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high


def test_parse_guess_rejects_non_numbers_and_floats():
    from logic_utils import parse_guess
    assert parse_guess("abc")[0] is False
    assert parse_guess("")[0] is False
    assert parse_guess("7.9")[0] is False


def test_parse_guess_enforces_range():
    from logic_utils import parse_guess
    assert parse_guess("0", 1, 100)[0] is False
    assert parse_guess("101", 1, 100)[0] is False
    assert parse_guess("50", 1, 100) == (True, 50, None)


def test_score_first_guess_win_and_wrong_guesses():
    from logic_utils import update_score
    assert update_score(0, "Win", 1) == 90
    assert update_score(0, "Too High", 2) == -5
    assert update_score(0, "Too High", 3) == -5
    assert update_score(0, "Too Low", 2) == -5
