tuple1=(11,[22,33],44,55)
tuple2=list(tuple1)
tuple2[1][0]=200
tuple1=tuple(tuple2)
print(f"tuple1:{tuple1}")
