import search

def test_readfile():
    assert isinstance(search.readfile("tp7/text1.txt"), list), "Test 1 readfile"
    try:
        assert isinstance(search.readfile("text1.txt"), list), "Test 2 readfile"
    except:
        print("AssertionError", "Test 2 readfile")

def test_get_words():
    assert  search.get_words(["ujjk","gghjn","dfcgbh"]), "Test 1 get_words"
    try:
        assert search.get_words("qwerty"), "Test 2 get_words"
    except:
        print("AssertionError", "Test 2 get_words")

def test_create_index():
    assert  search.create_index("tp7/text1.txt"), "Test 1 create_index"
    try:
        assert search.create_index("text1.txt"), "Test 2 create_index"
    except:
        print("AssertionError", "Test 2 create_index")

def test_get_lines():
    assert isinstance(search.get_lines(["text1","correct"], {"test": 1} ),list), "Test 1 get_lines"

    try:
        assert search.get_lines("text1.txt", {"test": 1} ), "Test 2 get_lines"
    except:
        print("AssertionError", "Test 2 get_lines")

    try:
        assert search.get_lines(["text1.txt", 55, [], {}, True], {"test": 1} ), "Test 3 get_lines"
    except:
        print("AssertionError", "Test 3 get_lines")

    try:
        assert search.get_lines(["text1.txt","3456"], ["test"] ), "Test 4 get_lines"
    except:
        print("AssertionError", "Test 4 get_lines")

test_readfile()
test_get_words()
test_create_index()
test_get_lines()