from typing import Tuple


delta_x = {
  b"w": 0,
  b"s": 0,
  b"a": -1,
  b"d": 1
}

delta_y = {
  b"w": 1,
  b"s": -1,
  b"a": 0,
  b"d": 0
}


def positioning(key_pressed: bytes, x: int, y: int) -> Tuple[int, int]:
  if key_pressed not in delta_x.keys():
    return x, y
  return (
    min(max(x+delta_x[key_pressed], 0), 255),
    min(max(y+delta_y[key_pressed], 0), 255)
  )
