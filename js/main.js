let tg = window.Telegram.WebApp;
let buy = document.getElementById("buy");
let order = document.getElementById("order");
tg.expand();

buy.addEventListener("click", () => {
    document.getElementById("main").style.display = "none";
    document.getElementById("form").style.display = "block";
    })

order.addEventListener("click", () => {
    document.getElementById("error").innerText = "";
    let name = document.getElementById("user_name").value;
    let phone = document.getElementById("user_phoone").value;
    let adress = document.getElementById("user_adress").value;
    if (name.lenght != 0) {
        document.getElementById("error").innerText = "Имя не может быть пустым!";
        return;
    }
    if (phone.lenght != 0) {
        document.getElementById("error").innerText = "Телефон не может быть пустым!";
        return;
    }
    if (adress.lenght != 0) {
        document.getElementById("error").innerText = "Адрес не может быть пустым!";
        return;

    }
    let data = {
        name: name,
        phone: phone,
        adress: adress
    }
    tg.sendData(JSON.stringify(data));
    tg.close();
})