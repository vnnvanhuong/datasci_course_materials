import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    matrix = record[0]
    row = record[1]
    col = record[2]
    if matrix == 'a':
      if row == 0:
        mr.emit_intermediate('0_0', record)
        mr.emit_intermediate('0_1', record)
        mr.emit_intermediate('0_2', record)
        mr.emit_intermediate('0_3', record)
        mr.emit_intermediate('0_4', record)
      elif row == 1:
        mr.emit_intermediate('1_0', record)
        mr.emit_intermediate('1_1', record)
        mr.emit_intermediate('1_2', record)
        mr.emit_intermediate('1_3', record)
        mr.emit_intermediate('1_4', record)
      elif row == 2:
        mr.emit_intermediate('2_0', record)
        mr.emit_intermediate('2_1', record)
        mr.emit_intermediate('2_2', record)
        mr.emit_intermediate('2_3', record)
        mr.emit_intermediate('2_4', record)
      elif row == 3:
        mr.emit_intermediate('3_0', record)
        mr.emit_intermediate('3_1', record)
        mr.emit_intermediate('3_2', record)
        mr.emit_intermediate('3_3', record)
        mr.emit_intermediate('3_4', record)
      else:
        mr.emit_intermediate('4_0', record)
        mr.emit_intermediate('4_1', record)
        mr.emit_intermediate('4_2', record)
        mr.emit_intermediate('4_3', record)
        mr.emit_intermediate('4_4', record)
    elif matrix == 'b':
      if col == 0:
        mr.emit_intermediate('0_0', record)
        mr.emit_intermediate('1_0', record)
        mr.emit_intermediate('2_0', record)
        mr.emit_intermediate('3_0', record)
        mr.emit_intermediate('4_0', record)
      elif col == 1:
        mr.emit_intermediate('0_1', record)
        mr.emit_intermediate('1_1', record)
        mr.emit_intermediate('2_1', record)
        mr.emit_intermediate('3_1', record)
        mr.emit_intermediate('4_1', record)
      elif col == 2:
        mr.emit_intermediate('0_2', record)
        mr.emit_intermediate('1_2', record)
        mr.emit_intermediate('2_2', record)
        mr.emit_intermediate('3_2', record)
        mr.emit_intermediate('4_2', record)
      elif col == 3:
        mr.emit_intermediate('0_3', record)
        mr.emit_intermediate('1_3', record)
        mr.emit_intermediate('2_3', record)
        mr.emit_intermediate('3_3', record)
        mr.emit_intermediate('4_3', record)
      else:
        mr.emit_intermediate('0_4', record)
        mr.emit_intermediate('1_4', record)
        mr.emit_intermediate('2_4', record)
        mr.emit_intermediate('3_4', record)
        mr.emit_intermediate('4_4', record)


def reducer(key, list_of_values):
    parts = key.split('_')
    row, col = int(parts[0]), int(parts[1])

    matrixMap = {}
    matrixMap.setdefault("a", [])
    matrixMap.setdefault("b", [])

    for x in list_of_values:
      matrixMap[x[0]].append(x)

    total = 0;
    for a in matrixMap["a"]:
      for b in matrixMap["b"]:
        if a[2] == b[1]:
          total += a[3] * b[3]

    mr.emit((row, col, total))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
