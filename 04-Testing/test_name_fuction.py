from name_function import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name('john', 'wick')
    assert formatted_name == 'John Wick'
    
def test_another():
    formatted_name_2 = get_formatted_name('Sika', 'Tanju')
    assert formatted_name_2 == 'Sika Tanju'

def test_three():
    assert get_formatted_name('saad', last='ka', middle='ibn') == 'Saad Ibn Ka'
