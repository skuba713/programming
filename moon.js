var moon = 1.5;
var phase;
if (moon==0){
	phase = "New";
	alert("It's a new moon");
}
if (moon>0 && moon<.5){
	phase = "Crescent";
	alert("It's a crescent moon");
}
if (moon==.5){
	phase = "Half";
	alert ("It's a half moon");
}
if (moon>0.5 && moon <1){
	phase = "Gibbous";
	alert ("It's a gibbous moon");
}
if (moon == 1){
	phase = "Full"
	alert ("It's a full moon");
}


switch (phase){
	case "New":
		alert("New moon");
		break;
	case "Crescent":
		alert("Crescent moon");	
		break;
	case "Half":
		alert("Half moon");
		break;
	case "Gibbous":
		alert("Gibbous moon");
		break;
	case "Full":
		alert("Full moon");
		break;
	default:
		alert("That's no moon!");

}