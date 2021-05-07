    
    function buttonClick() {

        const uname = $("#uname").val();
        const password = $("#psw").val();
        const dbname = $("#dbname").val();
        // console.log('http://127.0.0.1:5000/?query={login(username:"'+uname+'",password:"'+password+'",dbname:"'+dbname+'"){conn}}');

        $.ajax({url: 'http://127.0.0.1:5000/?query={login(username:"'+uname+'",password:"'+password+'",dbname:"'+dbname+'"){table}}',
            // contentType: "application/json",
            // mimeType: "application/json",
            type:'GET',
            // async:false,
            success: function(response) {
                // console.log(response.data.login.conn);
                // htmlCode = response.data.login.conn;
                // $("#abc").html(htmlCode);
                var table = response.data.login;
                // console.log(table.length);
                htmlcode="<form action='javascript:getSk("+table.length+")'>";
                // console.log(table);
                for(i=0;i<table.length;i++)
                {
                    htmlcode += "<label>"+table[i].table+"</label><select id="+table[i].table+">";
                    window['table'+i] = table[i].table; 

                    for(j=0;j<3;j++)
                    {
                        htmlcode += "<option value='"+j+"'>"+j+"</option>";
                    }
                    htmlcode += "</select><br>";
                    // console.log(htmlcode);
                    
                }
                htmlcode += "<button id='getsk'>Get Skeleton</button><input type='reset' value='Reset' onclick=resetit()></form>"
                $("#databasetables").html(htmlcode);
            },
            error: function(error) {
                alert("ERROR");
                console.log(error);
              }
        });
    }
    function resetit()
    {
        $("#qbe").html("");
        $("#runqe").html("");
        $("#res").html("");
    }

    function getSk(tl)
    {
        console.log("1: "+tl) //
        const uname = $("#uname").val();
        const password = $("#psw").val();
        const dbname = $("#dbname").val();
        window["num"] = 0
        // if
        htmlcode="";
        htmlcode2="";
        var flag=0;
        $("#qbe").html(htmlcode);
        $("#runqe").html(htmlcode2);
        
        htmlcode += "<form id='runq' action='javascript:runQ("+tl+")'>";
        for(i=0;i<tl;i++)
        {
            var n = eval('table'+i);
            console.log("2: "+eval('table'+i));   ///
            console.log("3: "+$('#'+eval('table'+i)).find(":selected").text());///
            if($('#'+eval('table'+i)).find(":selected").text()>0)
            {
                flag = 1;
                console.log("4: "+"click");         ///
                console.log("5: "+eval('table'+i));  ///
                for(j=0;j<$('#'+eval('table'+i)).find(":selected").text();j++)
                {
                    num += 1
                    window["tb"+num] = n
                    $.ajax({url: 'http://127.0.0.1:5000/?query={params(username:"'+uname+'",password:"'+password+'",dbname:"'+dbname+'",tbname:"'+eval('table'+i)+'"){columns}}',
                    
                                type:'GET',
                                async:false, 
                                success: function(response) {
                                    
                                    console.log("6: "+"In success "+n);
                                    var cols = response.data.params;
                                    htmlcode += "<table id='t"+n+"'>"+
                                                "<tr>"+
                                                "<th>"+n+"</th>";
                                    window[n+"col"]=cols.length;
                                    for(k=0;k<cols.length;k++)
                                    {
                                        console.log("7: "+cols[k].columns);
                                        // window[n+k] = cols[k].columns;
                                        htmlcode +=  "<th>"+cols[k].columns+"</th>";
                                    }
                                    htmlcode += "</tr>"+
                                                "<tr>";
                                    for(k=0;k<cols.length+1;k++)
                                    {            
                                        // window[n+k] = n+k; 
                                        htmlcode += "<td><input type='text' placeholder='-' id="+n+k+"></input></td>";
                                                
                                    }
                                    htmlcode += "</tr>"+
                                                "</table>";
                                    console.log("8: "+htmlcode);

                                    $("#qbe").html(htmlcode); 
                                },
                                error: function(error) {
                                    alert("ERROR");
                                    console.log(error);
                                  }
                            });
                }

                
                
            }
            
        }
        
        if(flag==0 && i==tl)
        {
            $("#qbe").html("No Tables selected");
            // htmlcode2=""
            // console.log(htmlcode2);
            // $("#runq").append(htmlcode2); 
        }
        else if(i==tl && flag!=0)
        {
            // console.log(i,flag)
            htmlcode2 += "<label>Condition </label><input type='text' placeholder='condition' id='condition'>"+
                        "<button form='runq' onclick=runQ("+tl+")>Run Query</button></form>";
                        
        console.log("9: "+htmlcode2);
        $("#runqe").append(htmlcode2); 
        }

        
    }
    

    function runQ(tl)
    {
        console.log(tl);
        const uname = $("#uname").val();
        const password = $("#psw").val();
        const dbname = $("#dbname").val();
        htmlcode="";
        queryJoin="";
        check=["P.","_"]
        if(num==1)
        {
            tbname = window["tb"+num];
            console.log(tbname);
            var tb =  $("#t"+tbname);
            queryColParams = new Array();
            queryColNames = new Array();
            queryTabParams = "";
            queryCondParams = "";
            console.log($('#t'+tbname))
            $('#t'+tbname+' tr td').each(function() {
                console.log("Regex :"+$(this).find("input").val())
                // console.log(($(this).find("input").val()).match(/\bP./i))
                if(($(this).find("input").val()).match(/\bP./i) || ($(this).find("input").val()).match(/\b_[a-b]$/i) || $(this).find("input").val()==="" || $(this).find("input").val().match(/\b'.*'$/))
                {
                    queryColParams.push('"'+$(this).find("input").val().toUpperCase()+'"'); 
                }
                       
                else
                {
                    alert("Incorrect input");
                }
                
               
             });
             $('#t'+tbname+' tr th').each(function() {
                
                queryColNames.push('"'+$(this).text()+'"');    
            
            });
            
              
            console.log(queryColParams);
            console.log(queryColNames);
            if($('#t'+tbname+' tr td').find("input").val().match(/\bP./i) || $('#t'+tbname+' tr td').find("input").val()==="")
            {
                queryTabParams = $('#t'+tbname+' tr td').find("input").val().toUpperCase();
            }
            else
            {
                alert("Incorrect input");
                    
            }
            

            console.log(queryTabParams)
      
            console.log($("#condition"))
            queryCondParams = $("#condition").val();
            console.log("queryCondParams : "+queryCondParams);

          
            
            console.log('http://127.0.0.1:5000/?query={qbe(username:"'+uname+'",password:"'+password+'",dbname:"'+dbname+'",tbname:["'+tbname+'"],queryColNames:[['+queryColNames+']], queryCondParams:"'+queryCondParams+'", queryColParams:[['+queryColParams+']], queryTabParams:["'+queryTabParams+'"]){sql out}}')
            //ajax call for qbe
            $.ajax({url: 'http://127.0.0.1:5000/?query={qbe(username:"'+uname+'",password:"'+password+'",dbname:"'+dbname+'",tbname:["'+tbname+'"],queryColNames:[['+queryColNames+']], queryCondParams:"'+queryCondParams+'", queryColParams:[['+queryColParams+']], queryTabParams:["'+queryTabParams+'"]){sql out}}',
                    
            type:'GET',
            async:false, 
            success: function(response) {
                
                // console.log("6: "+"In success "+n);
                var sql = response.data.qbe.sql;
                var out = response.data.qbe.out;
                // htmlcode += "<table id='t"+n+"'>"+
                //             "<tr>"+
                //             "<th>"+n+"</th>";
                // window[n+"col"]=cols.length;
                // for(k=0;k<cols.length;k++)
                // {
                //     console.log("7: "+cols[k].columns);
                //     // window[n+k] = cols[k].columns;
                //     htmlcode +=  "<th>"+cols[k].columns+"</th>";
                // }
                // htmlcode += "</tr>"+
                //             "<tr>";
                // for(k=0;k<cols.length+1;k++)
                // {            
                //     // window[n+k] = n+k; 
                //     htmlcode += "<td><input type='text' placeholder='-' id="+n+k+"></input></td>";
                            
                // }
                // htmlcode += "</tr>"+
                //             "</table>";
                // console.log("8: "+htmlcode);

                $("#res").html("<br><p><b>"+sql+"</b><br></p><p>"+out+"</p>"); 
            },
            error: function(error) {
                alert("ERROR");
                console.log(error);
              }
        });
        }
        if(num>1)
        {
            tbname = new Array();
            // tb =new Array();
            for(i=1;i<=num;i++)
            {
                tbname.push('"'+eval("tb"+i)+'"');
                
                // tb.push($("#t"+eval("tb"+i)));

            }

            console.log(tbname);
            console.log(tb);
            queryColParams = new Array();
            queryColNames = new Array();
            queryTabParams = new Array();
            queryCondParams = "";
            check=new Array();
            for(i=0;i<num;i++)
            {
                value1 = new Array();
                value2 = new Array();
                console.log(tbname[i])
                $("#t"+eval("tb"+(i+1))+' tr td').each(function() {
                // console.log("I m in")
                // console.log($(this).find("input").val())
                // if(($(this).find("input").val()).match(/\bP./i) || ($(this).find("input").val()).match(/\b_[a-b]$/i) || $(this).find("input").val()==="" || $(this).find("input").val().match(/\b'.*'$/))
                //   {
                value1.push('"'+$(this).find("input").val().toUpperCase()+'"');   
                //   }
                //   else
                //   {
                //     alert("Incorrect input");
                //   }
               
             });
             $("#t"+eval("tb"+(i+1))+' tr th').each(function() {
                
                value2.push('"'+$(this).text()+'"');    
                // console.log($(this).text())
            });
            // if(i!=num-1)
            // {
            // queryColParams.push("["+value1+"],");
            // queryColNames.push("["+value2+"],");
            // }
            // else
            // {
            queryColParams.push("["+value1+"]");
            queryColNames.push("["+value2+"]");
            // }
            
          
            }

            
            // console.log("queryColParams")
            // console.log(queryColParams);
            // console.log(queryColNames);
            for(i=0;i<num;i++)
            {
            //     if($('#t'+eval("tb"+(i+1))+' tr td').find("input").val().match(/\bP./i) || $('#t'+eval("tb"+(i+1))+' tr td').find("input").val()==="")
            // {
                queryTabParams[i] = '"'+$('#t'+eval("tb"+(i+1))+' tr td').find("input").val().toUpperCase()+'"';
            // }
            // else
            // {
            //     alert("Incorrect input");
            // }
            }
            

            console.log(queryTabParams)
      
            console.log($("#condition"))
            queryCondParams = $("#condition").val();
            console.log("queryCondParams : "+queryCondParams);
            //ajax call for qbe
            console.log('http://127.0.0.1:5000/?query={qbe(username:"'+uname+'",password:"'+password+'",dbname:"'+dbname+'",tbname:['+tbname+'],queryColNames:['+queryColNames+'], queryCondParams:"'+queryCondParams+'", queryColParams:['+queryColParams+'], queryTabParams:['+queryTabParams+']){sql out}}')
            $.ajax({url: 'http://127.0.0.1:5000/?query={qbe(username:"'+uname+'",password:"'+password+'",dbname:"'+dbname+'",tbname:['+tbname+'],queryColNames:['+queryColNames+'], queryCondParams:"'+queryCondParams+'", queryColParams:['+queryColParams+'], queryTabParams:['+queryTabParams+']){sql out}}',
                    
            type:'GET',
            async:false, 
            success: function(response) {
                
                // console.log("6: "+"In success "+n);
                var sql = response.data.qbe.sql;
                var out = response.data.qbe.out;
                // htmlcode += "<table id='t"+n+"'>"+
                //             "<tr>"+
                //             "<th>"+n+"</th>";
                // window[n+"col"]=cols.length;
                // for(k=0;k<cols.length;k++)
                // {
                //     console.log("7: "+cols[k].columns);
                //     // window[n+k] = cols[k].columns;
                //     htmlcode +=  "<th>"+cols[k].columns+"</th>";
                // }
                // htmlcode += "</tr>"+
                //             "<tr>";
                // for(k=0;k<cols.length+1;k++)
                // {            
                //     // window[n+k] = n+k; 
                //     htmlcode += "<td><input type='text' placeholder='-' id="+n+k+"></input></td>";
                            
                // }
                // htmlcode += "</tr>"+
                //             "</table>";
                // console.log("8: "+htmlcode);

                $("#res").html("<br><p><b>"+sql+"</b><br></p><p>"+out+"</p>"); 
            },
            error: function(error) {
                alert("ERROR");
                console.log(error);
              }
        });
            console.log(tbname);

        }
    }