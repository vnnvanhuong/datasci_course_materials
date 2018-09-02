import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    person1 = record[0]
    person2 = record[1]
    mr.emit_intermediate(person1+'_'+person2, 1)
    mr.emit_intermediate(person2+'_'+person1, 1)

def reducer(key, list_of_values):
    persons = key.split('_');
    person1, person2 = persons[0], persons[1]
    if(len(list_of_values) == 1):
      mr.emit((person1, person2))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
