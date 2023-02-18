"""
    Implement an string shortening function using the following prototype:

    String shorten(String input_string, int prefix_size)

    The I18N shortening process has 3 parts.

    Part 1 : The first prefix_size characters of the input string
    Part 2 : An integer representation of the count of internal characters
    Part 3 : The last character of the input string

    Examples:
        shorten("internationalization", 1) -> "i18n"
        shorten("internationalization", 2) -> "in17n"
        shorten("hello", 3) -> "hel1o"
"""


def shorten(input_string, prefix_size):
    remaining_ch = len(input_string) - prefix_size
    if remaining_ch <= 1:
        return input_string
    prefix = input_string[:prefix_size]
    short_count = len(input_string) - 1 - prefix_size
    return f"{prefix}{short_count}{input_string[-1]}"


"""
Using the Shorten function from Part 1 of the problem,
implement a string array shortening function using the following prototype.

Array<String> shortenAll(Array<String> inputArray)

The value returned by ShortenAll must adhere to two constraints:
Uniqueness: Every value in the output should uniquely reference only 1 input
Shortness: Every value in the output should be the shortest representation
possible of the input

Example:
shortenAll(["abbbc", "adbbc", "abcccd"]) -> ["ab2c", "ad2c", "a4d"]

Note that the shortest representation for the first two elements is "a3c"
but we cannot return that value as it violates the 1:1 uniqueness constraint
because "a3c" can map to both "abbbc" and "adbbc"
"""


def shortenAll(inputArray: list[str]):
    shortened_dic = {}
    requires_backtrack = {}
    invalid_words = {}
    invalid_shortens = {}

    first_iteration = True
    while requires_backtrack or first_iteration:
        for i, word in enumerate(inputArray):
            if word in invalid_words:
                continue

            prefix_size = 1
            if i in requires_backtrack:
                prefix_size = requires_backtrack[i]
                prefix_size += 1
                del requires_backtrack[i]

            if len(word) <= 2 or prefix_size > len(word) - 1:
                # word cannot be shortened uniquely or is invalid length.
                invalid_words[word] = True
                continue

            short_count = len(word) - 1 - prefix_size
            short_count = "" if short_count <= 0 else short_count
            key = f"{word[:prefix_size]}{short_count}{word[-1]}"
            while key in invalid_shortens and prefix_size < len(word) - 1:
                prefix_size += 1
                short_count = len(word) - 1 - prefix_size
                short_count = "" if short_count <= 0 else short_count
                key = f"{word[:prefix_size]}{short_count}{word[-1]}"

            if key not in shortened_dic:
                shortened_dic[key] = True
            elif key in shortened_dic:
                # set prefix size
                invalid_shortens[key] = True
                requires_backtrack[i] = prefix_size
                requires_backtrack[shortened_dic[key]] = prefix_size
        if requires_backtrack:
            shortened_dic = {}
        first_iteration = False

    return list(shortened_dic)


print(
    f"""
Expect: shorten("internationalization", 1) -> "i18n"
Actual: {shorten("internationalization", 1)}
"""
)

print(
    f"""
Expect: shorten("internationalization", 2) -> "in17n"
Actual: {shorten("internationalization", 2)}
"""
)

print(
    f"""
Expect: shorten("hello", 3) -> "hel1o"
Actual: {shorten("hello", 3)}
"""
)

print(
    f"""
Expect: shortenAll(["abbbc", "adbbc", "abcccd"]) -> ["ab2c", "ad2c", "a4d"]
Actual: {shortenAll(["abbbc", "adbbc", "abcccd"])}
"""
)

print(
    f"""
Expect: shortenAll(["abcd", "abcd", "abcccd"]) -> ["ab2c", "ad2c", "a4d"]
Actual: {shortenAll(["abccd", "abced", "abcccd"])}
"""
)
