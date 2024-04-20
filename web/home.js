var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() {
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }
        anHttpRequest.open( "GET", aUrl, true );
        anHttpRequest.send( null );
    }
}
let signupForm = document.getElementById("signupForm");
signupForm.addEventListener("submit", (e) => {
    e.preventDefault();

    let firstname = document.getElementById("fname");
    let lastname = document.getElementById("lname");
    let gender = document.getElementById("gender");
    let departmentname = document.getElementById("department");

    var text =  "\n\nFirstname: " + firstname.value +
                "\n" + "Lastname: " + lastname.value +
                "\n" + "Gender: " + gender.value +
                "\n" + "Department: " + departmentname.value;

    var client = new HttpClient();
    client.get('https://api.telegram.org/bot5555555555:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/sendMessage?chat_id=555555555&text=*New signup*'
    + encodeURI(text) +
    '&disable_web_page_preview=True&parse_mode=MarkDown&reply_markup={"inline_keyboard": [[{"text": "Reject ❌", "callback_data": "Reject"},{"text": "Confirm ✅", "callback_data": "Confirm"}]]}'
    , function(response) {});

    alert("Sent ✅" + text);
});