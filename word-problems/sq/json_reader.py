DOUBLE_QUOTE = '"'
OPEN_OBJ = "{"
CLOSE_OBJ = "}"
OPEN_ARR = "["
CLOSE_ARR = "]"
COLON = ":"
COMMA = ","

KEY = "KEY"
VALUE = "VALUE"
ARRAY = "ARRAY"
COMPLETE_ARRAY = "COMPLETE_ARRAY"
OBJECT = "OBJECT"
COMPLETE_OBJ = "COMPLETE_OBJ"
STRING = "STRING"
NUMBER = "NUMBER"
BOOL = "BOOL"
INVALID = "INVALID"
END_OF_STRING = "END_OF_STRING"


class Json_Reader:
    def __init__(self):
        self.state = OBJECT

    def read_json_string(self, json_string):
        state = OBJECT
        json_string = json_string.strip()
        if len(json_string) < 2:
            return "INVALID INPUT"
        _, res = self.decode_object(json_string, 0, state)
        return res

    def determine_type(self, json_string, i, state):
        """
        When reading OBJECT or ARRAY,

        Where j is the position of the identifier of the type examples (",1,[)
        Return:
        j, TYPE
        """
        if i >= len(json_string):
            return i, END_OF_STRING
        for j in range(i, len(json_string)):
            ch = json_string[j]
            if ch.isspace():
                continue
            if state == OBJECT:
                if ch == '"':
                    return j, KEY
                elif ch == CLOSE_OBJ:
                    return j, COMPLETE_OBJ
                else:
                    return j, INVALID
            if state == VALUE:
                if ch == "t" or ch == "f":
                    return j, BOOL
                if ch == '"':
                    return j, STRING
                if ch in "0123456789":
                    return j, NUMBER
            if state == ARRAY:
                if ch == CLOSE_ARR:
                    return j, COMPLETE_ARRAY
                return j, VALUE
            elif ch == DOUBLE_QUOTE:
                return j, KEY
            if ch == OPEN_ARR:
                return j, ARRAY
            if ch == OPEN_OBJ:
                return j, OBJECT
            else:
                return j, INVALID
        return len(json_string), INVALID

    def call_decode(self, json_string, i, state):
        if state == KEY:
            return self.decode_key(json_string, i, state)

        if state == OBJECT:
            return self.decode_object(json_string, i, state)
        if state == ARRAY:
            return self.decode_array(json_string, i, state)
        if state == NUMBER:
            return self.decode_number(json_string, i, state)
        if state == STRING:
            return self.decode_string(json_string, i, state)
        if state == BOOL:
            return self.decode_bool(json_string, i, state)
        if state == INVALID:
            return {"invalid_input_index": i}

    def decode_object(self, json_string, i, state):
        if json_string[i] != "{":
            return len(json_string), INVALID

        j = i + 1
        res = {}
        while (state == OBJECT or state == KEY) and j < len(json_string):
            key = "invalid_key"
            value = "invalid_value"
            # Decode key
            j, state = self.determine_type(json_string, j, state)
            if state != KEY:
                break
            j, key = self.call_decode(json_string, j, state)
            # Decode value
            state = VALUE
            j, value = self.decode_value(json_string, j, VALUE)

            # Determine if still viewing object
            j, state = self.determine_type(json_string, j, OBJECT)
            res[key] = value

        if state == COMPLETE_OBJ:
            return j + 1, res

        for k in range(j, len(json_string)):
            ch = json_string[k]
            if ch.isspace():
                continue
            if ch == CLOSE_OBJ:
                return k + 1, res
            else:
                return len(json_string), "Error in reading end of object"

        return len(json_string), res

    def decode_array(self, json_string, i, state):
        """
        Array elements will be decoded same as VALUE
        The array is followed by comma..
        """
        if json_string[i] != "[":
            return len(json_string), INVALID

        j = i + 1
        res = []
        while (state == ARRAY or state == VALUE) and j < len(json_string):
            value = "invalid_value"
            # Decode value
            j, state = self.determine_type(json_string, j, ARRAY)
            if state != VALUE:
                break
            j, value = self.decode_value(json_string, j, VALUE)
            res.append(value)
            # Determine if still viewing array
            j, state = self.determine_type(json_string, j, ARRAY)

        if state == COMPLETE_ARRAY:
            return j + 1, res

        for k in range(j, len(json_string)):
            ch = json_string[k]
            if ch.isspace():
                continue
            if ch == CLOSE_ARR:
                return k + 1, res
            else:
                return len(json_string), "Error in reading end of arr"

        return len(json_string), res

    def decode_key(self, json_string, i, state):
        """
        key must be a string
        key must follow by :
        """
        res = INVALID
        j, res = self.decode_string(json_string, i, state)
        if res != INVALID:
            for k in range(j, len(json_string)):
                ch = json_string[k]
                if ch.isspace():
                    continue
                elif ch == ":":
                    return k + 1, res
        return len(json_string), INVALID

    def decode_value(self, json_string, i, state):
        res = INVALID
        j, current_state = self.determine_type(json_string, i, state)
        if current_state != INVALID:
            j, res = self.call_decode(json_string, j, current_state)
        if res == INVALID:
            return len(json_string), INVALID
        for k in range(j, len(json_string)):
            # value require trail comma except last value..
            ch = json_string[k]
            if ch.isspace():
                continue
            if ch == ",":
                return k + 1, res
            else:
                return k, res
        return j, res

    def decode_string(self, json_string, i, state):
        res = ""
        is_escaped = False
        for j in range(i + 1, len(json_string)):
            ch = json_string[j]
            if ch == '"' and not is_escaped:
                return j + 1, res
            elif is_escaped:
                res += ch
                is_escaped = False
            elif ch == "\\":
                # This character is escape character, do not add it.
                is_escaped = True
            else:
                res += ch
        # If reach end with no double quote, invalid string.
        return len(json_string), INVALID

    def decode_number(self, json_string, i, state):
        res = ""
        for j in range(i, len(json_string)):
            ch = json_string[j]
            if ch not in "0123456789":
                return j, int(res)
            res += ch

        return int(res)

    def decode_bool(self, json_string, i, state):
        if i + 3 > len(json_string):
            return len(json_string), INVALID
        if json_string[i : i + 3] == "true":
            return True
        if i + 4 > len(json_string):
            return len(json_string), INVALID
        if json_string[i : i + 4] == "false":
            return False


sample_json = r"""
{
    "test": 1234,
    "abc": "ef"
}
"""

sample_json_arr = r"""
{
    "test": 1234,
    "abc": "ef",
    "arr": [1,2,3]
}
"""

sample_nested = r"""
{
    "test": {
        "nest": [50,60,70],
        "nest2": "NEsted value"
    },
    "abc": "ef",
    "arr": [1,2,3],
    "arrofObjects": [
        {
            "test": 1234,
            "key2": "its nested"
        },
        1234
    ]
}
"""

json_reader = Json_Reader()
res = json_reader.read_json_string(sample_json)
print("Test 1:", res)
res = json_reader.read_json_string(sample_json_arr)
print("Test 2:", res)
res = json_reader.read_json_string(sample_nested)
print("Test 3:", res)
