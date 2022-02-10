from task1 import resp


numerals = {
    "ESP": ["cero", "uno", "dos", "tres", "cuatro", "cinco",
            "seis", "siete", "ocho", "nueve"],
    "NOR": ["nul", "en", "to", "tre", "fire", "fem",
            "seks", "sju", "åtte", "ni"],
    "ENG": ["zero", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine"]
}
language = "ENG"


def response(request: str) -> str:
    global language
    # Modify these lines accordingly
    method, value = "EAT", "SALMON"
    if method == "A":
        pass
    elif method == "B":
        pass
    elif method == "C":
        pass
    else:
        return "BAD REQUEST"


if __name__ == "__main__":

    # Testing
    for key in resp:
        assert resp[key] == response(key)
