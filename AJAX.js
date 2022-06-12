function checkin(year,k){
var team=new Object();
var final=[]
for(let i=1;i<14;i++){
    var ht2=new XMLHttpRequest();
    console.log(i);
ht2.open("GET",`https://jsonmock.hackerrank.com/api/football_matches?competition=UEFA%20Champions%20League&year=${year}&page=${i}`,true)
ht2.send()
var t=""
ht2.onreadystatechange=function(){
    if(this.readyState===4){
        var abc=JSON.parse(this.responseText)
        t=abc["data"]
        for(let x in t){
            if(t[x]["team1"] in team){
                team[t[x]["team1"]]+=1
            }
            else{
                team[t[x]["team1"]]=1
            }
            if(t[x]["team2"] in team){
                team[t[x]["team2"]]+=1
            }
            else{
                team[t[x]["team2"]]=1
            }
        }
        console.log(team,i)
        for (x123 in team ){
            if (team[x123]>=k){
                final.push(x123)
            }
        }
        console.log(final)
        var se=new Set(final)
        if(i==13){
            return se;
        }
    }
    if(this.status!==200){
        console.log("FFFFAAAAIIIILLL")
    }
}

}
}
