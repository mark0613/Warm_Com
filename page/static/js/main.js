var jq = $.noConflict();
var liffId = "1657491571-RNWZXBEN";

async function getUserProfile() {
    return await liff
    .init({
        liffId: liffId,
    })
    .then(
        (resolve) => {
            if (!liff.isLoggedIn()) {
                sessionStorage.setItem('liffLoginRedirect', location.href)
                liff.login();
            }
            return liff.getProfile()
        }
    )
    .then(
        (resolve) => {
            return resolve;
        },
        (reject) => {
            // alert("Error")
            console.log(reject);
        }
    )  
}

async function closeLiffWindow() {
    await liff
    .init({
        liffId: liffId,
    })
    .then(() => {
        liff.closeWindow();
    })
}

function showSpinner() {
    $("#cover-spinner").show();
}

function hideSpinner() {
    $("#cover-spinner").hide();
}

window.onload = async function() {
    // TODO: loading(spinner )
    // let data = await getUserProfile();
    // TODO: remove loading
    // console.log(data);
}