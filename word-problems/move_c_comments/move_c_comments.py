class Solution:
    def move_c_comments(self, input_str: str):

        res = ""

        decoding_str = False
        comment_start = False
        comment_start_i = -1
        comment_end_i = 0
        for i, ch in enumerate(input_str):
            if decoding_str:
                if self._is_string_ch(input_str, i):
                    decoding_str = False
            elif self._is_string_ch(input_str, i):
                decoding_str = True
            elif comment_start and self._is_comment_end(input_str, i):
                res += input_str[comment_end_i:comment_start_i]
                comment_end_i = i + 1
                comment_start = False
            elif self._is_comment_start(input_str, i):
                comment_start = True
                comment_start_i = i - 1

        res += input_str[comment_end_i : len(input_str)]
        return res

    def _is_string_ch(self, input_str, i):
        # for c string is "" and ch literal ''. Return true either
        if input_str[i] == "'" or input_str[i] == '"':
            return True
        return False

    def _is_comment_start(self, input_str, i):
        if i + 1 >= len(input_str):
            return False
        if input_str[i - 1] == "/" and input_str[i] == "*":
            return True
        return False

    def _is_comment_end(self, input_str, i):
        if i + 1 >= len(input_str):
            return False
        if input_str[i - 1] == "*" and input_str[i] == "/":
            return True
        return False
