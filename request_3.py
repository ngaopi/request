import requests
import json 
def request():
    a=requests.get("http://saral.navgurukul.org/api/courses")
    b=a.json()
    with open("courses-1.json","w") as f:
        json.dump(b,f,indent=4)
    list=[]
    i=0
    while i<len(b["availableCourses"]):
        print(i+1,":",b["availableCourses"][i]["name"],"_ _ _",b["availableCourses"][i]["id"])
        list.append(b["availableCourses"][i]["id"])
        i+=1 
    user=int(input("select the serial number:--"))-1
    d=requests.get("http://saral.navgurukul.org/api/courses/"+str(list[user])+"/exercises")
    e=d.json()
    with open("course-2.json","w") as g:
        json.dump(e,g,indent=4)
        # print(e)
    j=0
    l=0
    slug=[]
    while j<len(e[b]):
        print(l+1,e[b][j]["name"])
        slug.append(e[b][j]["slug"])
        l+=1
        j+=1
    user2=int(input("enter the slug name:--"))
    sluglist=requests.get("http://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug=requests__using-json ")
    m=sluglist.json()
    with open("sluglist-1.json","w") as k:
        json.dump(m,k,indent=4)
    s=d["name"]
    u=d["content"]
    print(s)
    print(u)
request()


  