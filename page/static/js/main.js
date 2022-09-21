async function getUserId() {
    return await liff
    .init({
        liffId: "1657491571-L0G01dnZ",
    })
    .then(
        (resolve) => {
        // if (!liff.isLoggedIn()) {
        //     liff.login();
        // }
            return liff.getProfile()
        }
    )
    .then(
        (resolve) => {
            return resolve["userId"];
        },
        (reject) => {
            // alert("Error")
            console.log(reject);
        }
    )  
}

window.onload = async function() {
    // TODO: loading(spinner )
    let data = await getUserId();
    // TODO: remove loading
    console.log(data);
}