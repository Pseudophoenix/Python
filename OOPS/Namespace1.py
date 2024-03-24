class Sample:
    n=10
print(Sample.n)
Sample.n+=1
print(Sample.n)
s=Sample()
print(s.n)
s.n+=1
# observe the class variable in both namespaces i.e of instance and class
print(Sample.n)
print(s.n)
Sample.n=1
print(Sample.n)
print(s.n)
