//////STORE CURRENT URL//////
let currentURL = window.location.href;
////// ROCK PAPER SCISSORS//////
let botPick= 0
let playerPick = "String"
//////SET PAGE 1//////
let binderPageNum = 1;
let binderPageCaption = 1;
//////////////////SET CAPTIONS//////////////////////////
const captions = new Map();
	captions.set(1, " Here's my opening page of Glaceon & Leafeon. This page is for non-illustration rares. All I'm  missing rn are GX's. ^-^");
	captions.set(2, " Now this page is for the illustration/special illustration rares of Glacy & Leafy. It's pretty bare rn but that's because the eeveelutions are super expensive. :c");
	captions.set(3, " THIS IS MY ROCKSTAR PAGE !!!!!!!!!!!!!1111 YEAAAAAAAAAAAAAAAAAAHHHHHHHHHH *GUITAR SOLO* !!!!!!!!!!!!!111111!!!1!!!1!1!!!! XD");
	captions.set(4, " Nature :D");
	captions.set(5, " This one's gonna be pokemon helping out & being cozy at home !");
	captions.set(6, " This page'll be full of the HD illustrations !!!");
	captions.set(7, " Here's my pink page. Maybe I'll make it Jacinthe themed since I already have her full art ?? IDK what mons she has tho as I haven't played PLZA yet. Hmmmmmm.....");
//////////////////SET PAGE PICS/////////////////////////
const pagePics = new Map();
	pagePics.set(1, "url('/static/images/page1.png')");
	pagePics.set(2, "url('/static/images/page2.png')");
	pagePics.set(3, "url('/static/images/page3.png')");
	pagePics.set(4, "url('/static/images/page4.png')");
	pagePics.set(5, "url('/static/images/page5.png')");
	pagePics.set(6, "url('/static/images/page6.png')");
	pagePics.set(7, "url('/static/images/page7.png')");

// CHECK 4 MOBILE DEVICE & DISPLAY WARNING
window.onload = whenWindowLoads();
function mobileCheck() {
	let check = false;
	(function(a){if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4))) check = true;})(navigator.userAgent||navigator.vendor||window.opera);
	return check;
}

function whenWindowLoads() {
////////////////////HTTP REDIRECT////////////////////
	if (currentURL.indexOf("http://site") != -1) {
		window.location.replace("https://site.bunteeth.net")
	}
}

///////////////////////BUTTON FUNCTIONALITY 4 BINDER BLOG POST///////////////////////
function binderPageButtonNext() {
////NEXT PAGE////
	binderPageNum += 1;
	binderPageCaption += 1;
	if (binderPageNum > 7 || binderPageCaption > 7) {
		binderPageNum = 7;
		binderPageCaption = 7;
	}
///////////////////RENDER///////////////////////
	document.getElementById('pageContainer').style.backgroundImage = pagePics.get(binderPageNum);
	document.getElementById('pageCaption').innerHTML = captions.get(binderPageCaption);
}

function binderPageButtonBack() {
////LAST PAGE////
	binderPageNum -= 1;
	binderPageCaption -= 1;
	if (binderPageNum < 1 || binderPageCaption < 1) {
		binderPageNum = 1;
		binderPageCaption = 1;
	}
///////////////////RENDER///////////////////////
	document.getElementById('pageContainer').style.backgroundImage = pagePics.get(binderPageNum);
	document.getElementById('pageCaption').innerHTML = captions.get(binderPageCaption);
}

//ROCK PAPER SCISSORS !!!!!!!!!!!
function getRandomNumber(min, max) {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}
/////////////BOT CHOICE/////////////
function buttonTest() {
	if (playerPick != "String") {
		botPick = getRandomNumber(1,3);
		if (botPick == 1) {
			document.getElementById('botSpace').innerHTML = "Rock";
		} else if (botPick == 2) {
			document.getElementById('botSpace').innerHTML = "Paper";
		} else {
			document.getElementById('botSpace').innerHTML = "Scissors";
		}
		return gameResults();
	} else {
		return gameResults();
	}
}
////////////////////////FUNCTIONS 2 PICK CHOICES////////////////////////
function pickRock() {
	document.getElementById('botSpace').innerHTML = "";
	document.getElementById('resultSpace').innerHTML = "";
	playerPick = "You picked Rock !";
	return playerPick;
}

function pickPaper() {
	document.getElementById('botSpace').innerHTML = "";
	document.getElementById('resultSpace').innerHTML = "";
	playerPick = "You picked Paper !";
	return playerPick;
}

function pickScissors() {
	document.getElementById('botSpace').innerHTML = "";
	document.getElementById('resultSpace').innerHTML = "";
	playerPick = "You picked Scissors !";
	return playerPick;
}
///////////////////COMPARES PLAYER CHOICE 2 BOT CHOICE///////////////////
function gameResults() {
	if (botPick == 1 && playerPick == "You picked Paper !") {
		document.getElementById('resultSpace').innerHTML = "YOU WIN";
		playerPick = "String";
	} else if (botPick == 2  && playerPick == "You picked Scissors !") {
		document.getElementById('resultSpace').innerHTML = "YOU WIN";
		playerPick = "String";
	} else if (botPick== 3 && playerPick == "You picked Rock !") {
		document.getElementById('resultSpace').innerHTML = "YOU WIN";
		playerPick = "String";
	} else if (playerPick == "String") {
		document.getElementById('resultSpace').innerHTML = "ok like at least pick something >:l";
		document.getElementById('botSpace').innerHTML = "";
		document.getElementById('playerSpace').innerHTML = "";
	} else {
		playerPick = "String";
		return 	document.getElementById('resultSpace').innerHTML = "Awwww u lose :c";
	}
}
////////////////BUTTON THAT RESETS THE GAME////////////////
function refresh() {
	playerPick = "String";
	botPick = 0;
	document.getElementById('playerSpace').innerHTML = "";
	document.getElementById('botSpace').innerHTML = "";
	document.getElementById('resultSpace').innerHTML = "";
}

function changeIFrame(url) {
	document.getElementById('frame').setAttribute("src", url)
}
