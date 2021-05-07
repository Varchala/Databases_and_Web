
    
    var url = 'http://localhost:5000/periodictable/load';
    htmlcode = "";
    $.ajax({
        url: url,
        // async: "false",
        type: 'GET',
        contentType: "application/json",
        dataType: "json",
        success: function(response) {
          console.log(response);
         
          htmlcode += "<label> Classification </label><select id ='classification' onchange='e_class()'>";
          for(i in response['class'])
          {
              htmlcode += "<option value ='"+response['class'][i]+"'>"+response['class'][i]+"</option>";
          }
          htmlcode += "</select>";

          htmlcode += "<label> Standard States </label><select id ='state'  onchange='e_state()'>";
            for(i in response['state'])
            {
      
                htmlcode += "<option value ='"+response['state'][i]+"'>"+response['state'][i]+"</option>";
            }
            htmlcode += "</select>";

            htmlcode += "<label> Blocks </label> <select id ='block'  onchange='e_block()'>";
            
            for(i in response['block'])
            {
      
                htmlcode += "<option value ='"+response['block'][i]+"'>"+response['block'][i]+"</option>";
            }
            htmlcode += "</select>";
            htmlcode += "<label> Groups </label> <select id ='group'  onchange='e_group()'>";
            arr = Array.from(new Set(response['group'])).sort();
            for(i in arr)
            {
      
                htmlcode += "<option value ='"+arr[i]+"'>"+arr[i]+"</option>";
            }
            htmlcode += "</select>";
            htmlcode += " <label>Periods </label> <select id ='period'  onchange='e_period()'>";
            arr = Array.from(new Set(response['period'])).sort();
            console.log(arr)
            for(i in arr)
            {
      
                htmlcode += "<option value ='"+arr[i]+"'>"+arr[i]+"</option>";
            }
            htmlcode += "</select>";
          // console.log(htmlcode)
          $("#container").html(htmlcode);
        }
      });
    function e_class()
    {
      htmlcode=""
      console.log(document.getElementById("classification").value)
      var url = 'http://localhost:5000/periodictable/classification/'+document.getElementById("classification").value;
      console.log(url);
      $.ajax({
          url: url,
          type: 'GET',
          // async: "false",
          contentType: "application/json",
          dataType: "json",
          success: function(response) {
            // htmlcode = ""
            console.log(response);
            console.log(response['ele'].length-1)
            htmlcode += "<table>";

            for(i=0;i<response['ele'].length;i=i+10)
            {
              htmlcode += "<tr>";
              k = i+10;
              // console.log(k)
              if(k>response['ele'].length-1)
              {
                k=response['ele'].length
              }
              console.log(k)
              for(j=i;j<k;j++)
              {
                htmlcode += "<td onclick=\"element('"+response['ele'][j]+"')\">"+response['ele'][j]+"</td>";
              }
                htmlcode += "</tr>";
            }
            htmlcode += "</table>";
            console.log(htmlcode)
            $("#databasetables").html(htmlcode);
          }
        });
 
    }
    function element(val)
    {
      console.log(val)
      htmlcode=""
      var url = 'http://localhost:5000/periodictable/element/'+val;
      console.log(url);
      $.ajax({
          url: url,
          type: 'GET',
          // async: "false",
          contentType: "application/json",
          dataType: "json",
          success: function(response) {
            // htmlcode = ""
            console.log(response);
            // console.log(response['ele'].length-1)
            htmlcode += "<table>";
            htmlcode += "<tr> <td>name: "+response["name"]+"</td></tr>";
            htmlcode += "<tr> <td>symbol: "+response["symbol"]+"</td></tr>";
            htmlcode += "<tr> <td>group: "+response["group"]+"</td></tr>";
            htmlcode += "<tr> <td>period: "+response["period"]+"</td></tr>";
            htmlcode += "<tr> <td>standardstate: "+response["standardstate"]+"</td></tr>";
            htmlcode += "<tr> <td>block: "+response["block"]+"</td></tr>";
            htmlcode += "<tr> <td>classification: "+response["classification"]+"</td></tr>";
            htmlcode += "<tr> <td>casRegistryID: "+response["casRegistryID"]+"</td></tr>";
            htmlcode += "<tr> <td>atmoicweight: "+response["atmoicweight"]+"</td></tr>";
            htmlcode += "<tr> <td>atomicnumber: "+response["atomicnumber"]+"</td></tr>";
            htmlcode += "<tr> <td>color: "+response["color"]+"</td></tr>";
         
        
            htmlcode += "</table>";
            console.log(htmlcode)
            $("#ele").html(htmlcode);
          }
        });
    }
    function e_block()
    {
      htmlcode=""
      console.log(document.getElementById("block").value)
      var url = 'http://localhost:5000/periodictable/block/'+document.getElementById("block").value;
      console.log(url);
      $.ajax({
          url: url,
          type: 'GET',
          // async: "false",
          contentType: "application/json",
          dataType: "json",
          success: function(response) {
            // htmlcode = ""
            console.log(response);
            console.log(response['ele'].length-1)
            htmlcode += "<table>";

            for(i=0;i<response['ele'].length;i=i+10)
            {
              htmlcode += "<tr>";
              k = i+10;
              // console.log(k)
              if(k>response['ele'].length-1)
              {
                k=response['ele'].length
              }
              console.log(k)
              for(j=i;j<k;j++)
              {
                htmlcode += "<td onclick=\"element('"+response['ele'][j]+"')\">"+response['ele'][j]+"</td>";
              }
                htmlcode += "</tr>";
            }
            htmlcode += "</table>";
            console.log(htmlcode)
            $("#databasetables").html(htmlcode);
          }
        });
 
    }
    function e_group()
    {
      
      htmlcode=""
      console.log(document.getElementById("group").value)
      var url = 'http://localhost:5000/periodictable/group/'+document.getElementById("group").value;
      console.log(url);
      $.ajax({
          url: url,
          type: 'GET',
          // async: "false",
          contentType: "application/json",
          dataType: "json",
          success: function(response) {
            // htmlcode = ""
            console.log(response);
            console.log(response['ele'].length-1)
            htmlcode += "<table>";

            for(i=0;i<response['ele'].length;i=i+10)
            {
              htmlcode += "<tr>";
              k = i+10;
              // console.log(k)
              if(k>response['ele'].length-1)
              {
                k=response['ele'].length
              }
              console.log(k)
              for(j=i;j<k;j++)
              {
                htmlcode += "<td onclick=\"element('"+response['ele'][j]+"')\">"+response['ele'][j]+"</td>";
              }
                htmlcode += "</tr>";
            }
            htmlcode += "</table>";
            console.log(htmlcode)
            $("#databasetables").html(htmlcode);
          }
        });
    }
    function e_period()
    {

      
      htmlcode=""
      console.log(document.getElementById("period").value)
      var url = 'http://localhost:5000/periodictable/period/'+document.getElementById("period").value;
      console.log(url);
      $.ajax({
          url: url,
          type: 'GET',
          // async: "false",
          contentType: "application/json",
          dataType: "json",
          success: function(response) {
            // htmlcode = ""
            console.log(response);
            console.log(response['ele'].length-1)
            htmlcode += "<table>";

            for(i=0;i<response['ele'].length;i=i+10)
            {
              htmlcode += "<tr>";
              k = i+10;
              // console.log(k)
              if(k>response['ele'].length-1)
              {
                k=response['ele'].length
              }
              console.log(k)
              for(j=i;j<k;j++)
              {
                htmlcode += "<td onclick=\"element('"+response['ele'][j]+"')\">"+response['ele'][j]+"</td>";
              }
                htmlcode += "</tr>";
            }
            htmlcode += "</table>";
            console.log(htmlcode)
            $("#databasetables").html(htmlcode);
          }
        });
      
    }
    function e_state()
    {
      
      htmlcode=""
      console.log(document.getElementById("state").value)
      var url = 'http://localhost:5000/periodictable/state/'+document.getElementById("state").value;
      console.log(url);
      $.ajax({
          url: url,
          type: 'GET',
          // async: "false",
          contentType: "application/json",
          dataType: "json",
          success: function(response) {
            // htmlcode = ""
            console.log(response);
            console.log(response['ele'].length-1)
            htmlcode += "<table>";

            for(i=0;i<response['ele'].length;i=i+10)
            {
              htmlcode += "<tr>";
              k = i+10;
              // console.log(k)
              if(k>response['ele'].length-1)
              {
                k=response['ele'].length
              }
              console.log(k)
              for(j=i;j<k;j++)
              {
                htmlcode += "<td onclick=\"element('"+response['ele'][j]+"')\">"+response['ele'][j]+"</td>";
              }
                htmlcode += "</tr>";
            }
            htmlcode += "</table>";
            console.log(htmlcode)
            $("#databasetables").html(htmlcode);
          }
        });
    }
    
      // var url = 'http://localhost:5000/periodictable/blocks';
      // $.ajax({
      //     url: url,
      //     type: 'GET',
      //     // async: "false",
      //     contentType: "application/json",
      //     dataType: "json",
      //     success: function(response) {
      //       // htmlcode = ""
      //       console.log(response);
      //       htmlcode += "<select name ='blocks'>";
      //       for(i in response['name'])
      //       {
      
      //           htmlcode += "<option value ='"+response['name'][i]+"'>"+response['name'][i]+"</option>";
      //       }
      //       htmlcode += "</select>";
      //       // console.log(htmlcode)
      //       $("#container").html(htmlcode);
      //     }
      //   });
      
    
 
      
    