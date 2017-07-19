def url(value):
    print('https://q4q61iwvq7.execute-api.us-east-1.amazonaws.com/v1/verchk/CADO/p1/m1?v=' + value + 'u=')

value = ['0.0.1', '0.0.2', '0.0.3', '0.0.4', '0.0.5', '0.0.6', '1.0.5', '0.1.5']
u = ['s1', 's2', 's3', 's4', 's5','s6', 's7', 's8', 's9', 's10',]

for i in range(1, 10):
    v = value[i]
    url(v)
    print('Next ' + v)

