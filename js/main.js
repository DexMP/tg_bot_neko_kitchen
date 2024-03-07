let tg = window.Telegram.WebApp;
let btn = document.getElementById("btn");
let btnED = document.getElementById("btnED");
tg.expand();

btn.addEventListener('click', function(){ //вешаем событие на нажатие html-кнопки
	if (tg.MainButton.isVisible){ //если кнопка показана 
		tg.MainButton.hide() //скрываем кнопку 
	}
  else{ //иначе
  	tg.MainButton.show(); //показываем 
  }
});

btnED.addEventListener('click', function(){ //вешаем событие на нажатие html-кнопки
	if (tg.MainButton.isActive){ //если кнопка показана 
		tg.MainButton.setParams({"color": "#E0FFFF"}); //меняем цвет
		tg.MainButton.disable() //скрываем кнопку 
	}
	else{ //иначе
		tg.MainButton.setParams({"color": "#143F6B"}); //меняем цвет
		tg.MainButton.enable() //показываем 
	}
});

Telegram.WebApp.onEvent('mainButtonClicked', function(){
	tg.sendData("some string that we need to send"); 
	//при клике на основную кнопку отправляем данные в строковом виде
});