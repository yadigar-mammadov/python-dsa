import pytest
from algorithms.array_string.group_anagrams import GroupAnagrams

@pytest.mark.parametrize(
    "strings, expected",
    [
        (["car", "arc", "eat", "bold", "tea"],  [["car", "arc"], ["eat", "tea"], ["bold"]]),
        (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
        ([""], [[""]]),
        (["anagram"], [["anagram"]]),
        (["a", "b"], [["a"], ["b"]]),
        (["aaa", "aaa", "ab", "ba", "aa"], [["aaa", "aaa"], ["ab", "ba"], ["aa"]]),
    ]
)
def test_group_anagrams(strings, expected):
    group_anagrams = GroupAnagrams(strings)

    """Since the order of the value does not matter, we normalize the expected value and results first by sorting them."""
    normalized_expected = sorted([sorted(group) for group in expected])

    anagrams_by_sorting = group_anagrams.group_anagrams_by_sorting()
    normalized_anagrams_by_sorting = sorted([sorted(group) for group in anagrams_by_sorting])

    anagrams_by_count_using_array = group_anagrams.group_anagrams_by_count_using_array()
    normalized_anagrams_by_count_using_array = sorted([sorted(group) for group in anagrams_by_count_using_array])

    anagrams_by_count_using_dictionary = group_anagrams.group_anagrams_by_count_using_dictionary()
    normalized_anagrams_by_count_using_dictionary = sorted([sorted(group) for group in anagrams_by_count_using_dictionary])

    assert normalized_anagrams_by_sorting == normalized_expected
    assert normalized_anagrams_by_count_using_array == normalized_expected
    assert normalized_anagrams_by_count_using_dictionary == normalized_expected
