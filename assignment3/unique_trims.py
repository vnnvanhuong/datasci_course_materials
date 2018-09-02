import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    value = record[1]
    mr.emit_intermediate(value[:-10], 1)

def reducer(key, list_of_values):
    mr.emit(key)


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
