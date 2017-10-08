function myFunction() {
   var data = SpreadsheetApp.getActiveSheet().getDataRange().getValues();
 var index = 0;
  var first = 0;
 url = "https://f1bce1e9.ngrok.io/api/addblogger";
 for (i in data) {
   
   if(first==0){
    first = first+1;
     continue;
   }
   index++;
   if(index>100)
     break;
   //Logger.log("Data1 is ", index);
   //var row = index;

   
   //Logger.log(" I is " + row)
   //SpreadsheetApp.getActiveSheet().getRange("F" + row).setValue(data[i][2]);
   
 

 
 var payload =
     {
       "Serial":data[i][0],
       "Name":data[i][1],
       "Visibility":data[i][2],
       "Birthday":data[i][3],
       "Gender":data[i][4],
       "Location":data[i][5],
       "Status":data[i][6],
       "Joined":data[i][7],
       "Job":data[i][8],
       "Language":data[i][9],
       "BlogTraffic":data[i][10],
       "Posts":data[i][11],
       "MyComments":data[i][11],
       "UserComments":data[i][13],
       "Photos":data[i][14],
       "Friends":data[i][15],
       "Following":data[i][16],
       "Followers":data[i][17],
       "Points":data[i][18],
       "LastOnline":data[i][19],
       "Posts_Percentile":data[i][20],
       "MyComments_percentile":data[i][21],
       "Ucomments_percentile":data[i][22],
       "Photos_percentile":data[i][23],
       "Friends_percentile":data[i][24],
       "Posts_points":data[i][25],
       "MyComments_points":data[i][26],
       "Ucomments_points":data[i][27],
       "Photos_points":data[i][28],
       "Friends_points":data[i][29],
       "Total_points":data[i][30]
       
     };
 
 var options =
     {
       "method"  : "POST",
       "payload" : payload,  
       "followRedirects" : true,
       "muteHttpExceptions": true
     };
 
 var result = UrlFetchApp.fetch(url, options);
 
 if (result.getResponseCode() == 200) {
   
//   var params = JSON.parse(result.getContentText());
//   
//   Logger.log(params.name);
   Logger.log("Success");

   
 }
 }

}
