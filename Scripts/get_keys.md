keys = $("input[ng-model='game.key']")
str = ""
for(i=0;i<keys.length;i++){
	if(i%2 == 0){	
        str = str + keys[i].value + ","
    }
}
str