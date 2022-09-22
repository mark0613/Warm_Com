ARTICLE = {
    title: "文章標題",
    content: "文章內容",
    time: "文章日期"
}
function putArticle(){
    $('#date small').text(ARTICLE["time"])
    $('#title').text(ARTICLE["title"])
    $('#content').text(ARTICLE["content"])
}
function getArticleId(){
    let url = location.href
    let article_id = url.split('/').slice(-1)
    return Number(article_id)
}
function getReplyContent(){
    let reply_content = $('#reply-content').val()
    return reply_content
} 
function giveReply(){
    let data = {
        "article_id" : getArticleId(),
        "user_id" : "...",
        "content" : getReplyContent()
    }
    console.log(data)
    // $.post(
    //     "",
    //     data,
    //     (response, status) => {
    //         if (status == "success") {
    //             if (response["status"] == "success"){
                        //window.alert("success")
    //             }
    //         }
    //     }
    // )
}
$(document).ready(() => {
    putArticle()
    $("#reply").click(() => {
        giveReply() 
    })
    $("#back").click(() => {
        window.location.replace("give_all");
    })
});