s = "MISSISSIPPI"
cnt=0
for ch in s: # s="MISSISSIPPI"
    if(ch=="I"):
        cnt=cnt+1
    if(cnt==2):
        break
    print("{}".format(ch),end="")

