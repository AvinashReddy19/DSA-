def generateRow(row):
        templist=[]
        ans1=1
        templist.append(ans1)
        for col in range(1,row):
            ans1*=(row-col)
            ans1=ans1//col
            templist.append(ans1)
        return templist
def generate(n):
        ans=[]
        for row in range(1,n+1):
            ans.append(generateRow(row))
        return ans

n=5
print(generate(n))
