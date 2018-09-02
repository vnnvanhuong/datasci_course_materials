import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    sourceMap = {}
    sourceMap.setdefault("order", [])
    sourceMap.setdefault("line_item", [])

    for values in list_of_values:
      sourceMap[values[0]].append(values)

    for x in sourceMap["order"]:
      for y in sourceMap["line_item"]:
        mr.emit(x + y)


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
