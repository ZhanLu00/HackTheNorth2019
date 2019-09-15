// $(document).ready(function(){
//     $("form").submit(function(event){
//         //this line disable the action inside of form
//         event.preventDefault();
//         //.val() to get the actual value of the id
//         var formName;
//         var tUnit = $("#form-tUnit").val();
//         // set up the form name
//         theForms = document.getElementsByTagName("form");
//         for(i=0;i<theForms.length;i++){
//             formName = theForms[i].name;
//         }


//         $("#resultV").load("action_page.php", {
//             //left-right is key-value, which the value just got from extract info from above
            
//             formName: formName,
//             tUnit: tUnit,
//             time: time,
//             qUnit: qUnit,
//             flowrate: flowrate,
//             submit: submit
            
//         }, function(responseTxt, statusTxt){
//             var x =document.getElementById("resultV").innerHTML;
//             if(statusTxt == "success"){
//             }else if(statusTxt == "error"){
//                 alert("Error: " + xhr.status + ": " + xhr.statusText);
//             }else if(r.slice(r.indexOf("#")+1) == ""){
//                 alert();
//             }
            
            
//         });

//         function prepareForPloting(){
//             var responseT = document.getElementById("resultV").innerHTML;
//             var num = "";
//             var data = [];
//             var t_ = true;
//             var a = [];


//             for (i = 0; i<responseT.length; i++){
//                 switch (responseT[i]){
//                     case "#":
//                     // store the output flowrate
//                         a[0].push(Number(num));
//                         return a;
//                         break;

//                     case "^":
//                     // store data and clear the store array
//                         data.push(Number(num));
//                         num = "";

//                         if (a.length == 0) {
//                             for (let i= 0; i < data.length; i++) {
//                                 a.push([data[i]]);
//                             }
//                         }else{
//                             for (let i = 0; i<data.length; i++){
//                                 a[i].push(data[i]);
//                             }
//                         }

//                         data.length = 0;
//                         break;
                        
//                     case "?":
//                     // store the number
//                         data.push(Number(num));
//                         num = "";
//                         break;

                    
//                     default:
//                     // store data in string
//                         num += responseT[i];
//                         break;
//                 }
//             }
            
//             return a;
//         }

//         var r = document.getElementById("resultV").innerHTML;
        
//         var x = prepareForPloting();

        
//         document.getElementById("testingData").innerHTML = x;
//         document.getElementById("trueResult").innerHTML = r.slice(r.indexOf("#")+1);


        
//     })

//     // //This is to check whether the php page has any error
//     // $("button").click(function(){
//     // 	$("#resultV").post("action_page.php");
//     // 	alert("finished");
//     // });

// });