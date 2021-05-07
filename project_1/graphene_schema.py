import graphene
import mysql.connector as mysql

class Login(graphene.ObjectType):
    table = graphene.String()

class Params(graphene.ObjectType):
    columns = graphene.String()

class Qbe(graphene.ObjectType):
    sql = graphene.String()
    out = graphene.String()

class Queries(graphene.ObjectType):
    
    login = graphene.List(Login, username=graphene.String(),password=graphene.String(),dbname=graphene.String())
    params = graphene.List(Params, username=graphene.String(),password=graphene.String(),dbname=graphene.String(),tbname=graphene.String())  
    qbe = graphene.Field(Qbe, username=graphene.String(),password=graphene.String(),dbname=graphene.String(),queryCondParams=graphene.String(),args={'tbname':graphene.List(graphene.String),'queryTabParams': graphene.List(graphene.String),'queryColParams': graphene.List(graphene.List(graphene.String)),'queryColNames': graphene.List(graphene.List(graphene.String))})
    print("hi")
    def resolve_qbe(self,info,username,password,dbname,queryCondParams,tbname,queryTabParams,queryColParams,queryColNames):
        db = mysql.connect(
            host="localhost",
            database=dbname,
            user=username,
            passwd=password,
            auth_plugin='mysql_native_password'
        )
        coln=[]
        cond=""
        query=""
        cols=""
        tbs=""
        flag=1
        countp=0
        check=[]
        queryJoin = ""
        for i in range(len(tbname)):
            if(queryTabParams[i]=="P."):
                countp += 1
        if(countp==len(tbname)):
            flag=0
        else:
            flag=1
        print("flag")
        print(flag)
        for row in queryColParams:
            del row[0]
        for row in queryColNames:
            del row[0]
        print(len(tbname))
        print(queryColParams)
        for tn in range(len(tbname)):
        
            print(queryColParams[tn]!= "")

            if(queryTabParams[tn]=='P.'and (queryCondParams=="" or (queryCondParams[0:2] not in queryColParams[tn])) and flag==1 and len(tbname)>1):
                for k in queryColNames[tn]:
                    # if(len(coln)<=1):
                    coln.append([tbname[tn]+"."+k])
                    # else:
                            # coln[tn].append(tbname[tn]+"."+k)
                    # coln[tn].append(tbname[tn]+"."+k)
                print("1: "+queryTabParams[tn]+" COLN: ")
                print(coln)
            elif(queryTabParams[tn]=='P.'and queryCondParams=="" and flag==0):
                query = "SELECT * FROM {}".format(tbname[tn])
                print(queryTabParams[tn])
                print("queryColParams")
                print(queryColParams[tn])
            if(queryColParams[tn]!= ""):
                print(queryColParams[tn]!= "")
                for i,j in zip(queryColParams[tn],queryColNames[tn]):
                    print("2: i j " + i,j)
                    if(i=="P." or  "P._" in i):
                        print(tn)
                        print(coln)
                        # if(len(coln)<=1):
                        coln.append([tbname[tn]+"."+j])
                        
                        print(coln)
                    elif("_" not in i and i != ""):
                        print("3: i j "+ i,j)
                        if(cond!=""):
                            cond += " && "+tbname[tn]+"."+j+"="+i+" "
                        else:
                            cond += tbname[tn]+"."+j+"="+i+" "

                    if(len(tbname)>1 and ("_" in i or i!="P." ) and i!= ""):
                        i = i.replace('P.','',1)
                        print("5: "+i)
                        if(i in check):
                            queryJoin = j
                        check.append(i)
                    if(queryCondParams !="" and ("_" in i or i!="P." ) and i!= ""):  
                        print("4: "+queryCondParams !="" and ("_" in i or i!="P." ))
                        if('P.' in i):
                                i = i.replace('P.','',1)
                                print("5: "+i)
                                
                        if(cond=="" and i in queryCondParams):
                            queryCondParams = queryCondParams.replace(i,'',1)
                            cond=tbname[tn]+"."+j+queryCondParams
                            print("6: "+cond)
                        elif(cond!="" and i in queryCondParams):
                            queryCondParams = queryCondParams.replace(i,'',1)
                            cond=" && "+tbname[tn]+"."+j+queryCondParams
                            print("7: "+cond)
                    # else:
                    #     if(i ):
                    #     cond=""
                    print("8: "+cond)
                      
        # for s in range(len(coln)):
        # print(s)
        print(len(coln))
        for col in coln:
            print(col[0])
            cols += col[0]+","
        cols=cols[:-1]
                    
        for t in tbname:
            tbs +=t+","
        tbs=tbs[:-1]
        print("cols :"+cols)
        
        
                    
        if(queryJoin!="" and cond!=""):
            cond += " && TRUE and "
            for i in tbname:
                cond += i+"."+queryJoin+"="
            cond = cond[:-1]
        elif (queryJoin!="" and cond==""):
            cond += " TRUE and "
            for i in tbname:
                cond += i+"."+queryJoin+"="
            cond = cond[:-1]
      
        # for i in range(tbname.length):
        if(len(tbname)>1):
            for l in range(len(tbname)):
                if (cond!="" and flag==1):
                    print("9: "+cond)
                    print("10: "+tbname[l])
                    # print("11: "+coln)
                    
                    query = "select {} from {} where {}".format(cols,tbs,cond)
                    #query = "select +"+coln+" from +"+tbname+" where "+cond'

                elif(cond!="" and  flag!=1):
                    query = "select * from {} where {}".format(tbs,cond)
                elif(cond==""):
                    query = "select {} from {}".format(cols,tbs)
        elif(len(tbname)==1):
            if (cond!="" and queryTabParams[0]!='P.'):
                print("9: "+cond)
                print("10: "+tbname[0])
                # print("11: "+coln)
                
                query = "select {} from {} where {}".format(cols,tbname[0],cond)
                #query = "select +"+coln+" from +"+tbname+" where "+cond
            elif(cond!="" and queryTabParams[0]=='P.' ):
                query = "select * from {} where {}".format(tbname[0],cond)
            elif(cond=="" and flag==1):
                query = "select {} from {}".format(cols,tbname[0])
        
        
        print("12: "+query)
        cursor = db.cursor()
        cursor.execute(query)
        qbe = cursor.fetchall()
        cursor.close()
        db.close()
        return Qbe(out=qbe,sql=query)
    def resolve_login(self,info,username,password,dbname):
        text = "hi"
        print("Hi")
        db = mysql.connect(
            host="localhost",
            database=dbname,
            user=username,
            passwd=password,
            auth_plugin='mysql_native_password'
        )
        if db.is_connected():
            text= "Connected to mysql"
        else:
            text= "Connection error"
        
        print(text)
        query = "SELECT table_name FROM information_schema.tables WHERE table_schema = \'{}\'".format(dbname)
        # print("SELECT table_name FROM information_schema.tables WHERE table_schema = \'{}\'".format(dbname))
        cursor = db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        db.close()
        login = []
        # text=Login(conn=text)
        for i in records:
            print(i[0])
            login.append(Login(table=i[0]))
        print(login)
        return login

    def resolve_params(self, info, username,password,dbname,tbname):
        db = mysql.connect(
            host="localhost",
            database=dbname,
            user=username,
            passwd=password,
            auth_plugin='mysql_native_password'
        )
        query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = \'{}\' AND TABLE_NAME = \'{}\'".format(dbname,tbname)
        cursor = db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        db.close()
        columns = []
        for i in records:
            print(i[0])
            columns.append(Params(columns=i[0]))
        print(columns)
        return columns


    

# def main():
schema = graphene.Schema(query=Queries)

# if __name__ == '__main__':
#     main()