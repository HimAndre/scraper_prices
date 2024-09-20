import pandas

value = 5.05
data = "25/06" 

data = {
    "value": [value],
    "data": [data],
}

frame = pandas.DataFrame(data)

print(frame)

