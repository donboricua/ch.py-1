import requests
import json, re

class updater:

  def findid(self):
    url = requests.get("http://st.chatango.com/cfg/nc/r.json")
    id = url.json()["r"]
    return id

  def findweights(self):
    url = requests.get("http://st.chatango.com/h5/gz/r%s/id.html"%self.ID).text.splitlines()
    print("Found server weights.")
    print("Processing server weights...")
    tags = json.loads(url[7].split(" = ")[-1])
    weights = []
    for a,b in tags["sm"]:
      c = tags["sw"][b]
      weights.append([a,c])
    return weights

  def updatech(self):
    print("Writing server weights to ch.py...")
    with open("ch.py","r+") as ch:
      rdata=ch.read()
      wdata=re.sub("tsweights = .*","tsweights = %s"%str(self.weights),rdata)
      ch.seek(0)
      ch.write(wdata)
      ch.truncate()

  def run(self):
    print("Searching for latest server weights list...")
    self.ID = self.findid()
    print("Server weight list found!")
    print("ID: r"+self.ID)
    print("Retrieving server weights...")
    self.weights = self.findweights()
    #print(self.weights)
    self.updatech()
    print("The server weights are now updated for ch.py, enjoy!")

main = updater()
main.run()

