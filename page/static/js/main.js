var jq = $.noConflict();

async function getUserProfile(liffId) {
    return await liff
    .init({
        liffId: liffId,
    })
    .then(
        (resolve) => {
            if (!liff.isLoggedIn()) {
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

async function closeLiffWindow(liffId) {
    liff
    .init({
        liffId: liffId,
    })
    .then(() => {
        liff.closeWindow();
    })
}

window.onload = async function() {
    // TODO: loading(spinner )
    // let data = await getUserProfile("1657491571-L0G01dnZ");
    // TODO: remove loading
    console.log(data);
}