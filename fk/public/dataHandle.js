$(document).ready(function(){
    $("form").submit(function(event){
        //this line disable the action inside of form
        event.preventDefault();
        //.val() to get the actual value of the id
        var formName;
        var userIn = $("#userInput").val();
        // set up the form name
        theForms = document.getElementsByTagName("form");
        for(i=0;i<theForms.length;i++){
            formName = theForms[i].name;
        }


        $("#resultV").load("action_page.php", {
            //left-right is key-value, which the value just got from extract info from above
            // JSON.stringify({formName: formName, userInput: userIn});
            formName: formName,
            userInput: userIn
            
        }, function(responseTxt, statusTxt){
            var x =document.getElementById("chatDisplay").innerHTML;
            if(statusTxt == "success"){
            }else if(statusTxt == "error"){
                alert("Error: " + xhr.status + ": " + xhr.statusText);
            }else if(r.slice(r.indexOf("#")+1) == ""){
                alert();
            }
            
            
        });

        

        
        // function prepareDataForDisplay(fileName){
        //     // get username
        //     // get format
        //     // return output string

        //     var r = JSON.parse(fileName);
        //     var name = r[name];
        //     if (r['type'] == "regular-text"){
        //         return "@oj9rds94n/" + name + r['text'];
        //     }else if (r['type'] == "td-box"){
        //         return "Not implemented yet"
        //     }
        // };

        function displayUserInput(uIn){
            var block = document.createElement("p");
            var msg = document.createTextNode("@oj9rds94n/" + name + r['text']);
            block.appendChild(msg);
            var element = document.getElementById("chatDisplay");
            element.appendChild(blcok);
            
        }

        // // get style 
        // var r = JSON.parse(fileName);
        // var style = r['style'];
        // // deploy style
        // var destination = document.getElementById("chatDisplay");
        // destination.setAttribute("style", style);
        // deplot content

        // disply user's input first
        displayUserInput(userIn);
        
        // display upstrem data
        var re = document.getElementById("result").innerHTML;
        var block = document.createElement("p");
        var msg = document.createTextNode("@oj9rds94n/ " + "TDRAF: " + re);
        block.appendChild(msg);
        var element = document.getElementById("chatDisplay");
        element.appendChild(blcok);
        
        
    })

    // //This is to check whether the php page has any error
    // $("button").click(function(){
    // 	$("#resultV").post("action_page.php");
    // 	alert("finished");
    // });

});