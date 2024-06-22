d={"dai":60,"DBDA":100,"DUASP":40}
print(d)
#to find capacity of a course DUASP
print("capacity of DUASP",d['DUASP'])
d={"pune":["neem","mango"],"mumbai":["coconut","supari","mango"]}
print(d)
#list of trees in pune
print("list of trees in pune city",d['pune'])
d['pune'].append("coconut")
print("list of trees in pune city after append",d['pune'])
d={123:{"eid":123,"ename":"Rajan","desg":"game designer"},
   124:{"eid":124,"ename":"Revati","desg":"UX designer"}}
print(d)
print("revatis designation:",d[124]["desg"])
print("display name of employee with id 123",d[123]["ename"])

lst=[{"name":"apple","num":20},{"name":"samsung","num":200},{"name":"mi","num":300}]
#display how many phones are sold for the given company name
cname="samsung"
for data in lst:
    if data['name']==cname:
        print(f"{data['name']}--->{data['num']}")
        break
else:
    print(f" {cname} not found")

d={"samsung":{"name":"samsung","num":200},"apple":{"name":"apple","num":20},
   "mi":{"name":"mi","num":300}}
#display how many phones are sold for the given company name
cname="samsung"
if cname in d:
    print(d[cname]["num"])
    





