function getArticleId(){
    let url = location.href
    let article_id = url.split('/').slice(-1)
    return Number(article_id)
}
function getReplyContent(){
    let reply_content = $('#reply-content').val()
    return reply_content
} 
async function giveReply(){
    let profile = await getUserProfile()
    let data = {
        "user_id" : profile.userId,
        "article_id" : getArticleId(),
        "content" : getReplyContent(),
    }
    jq.post(
        "/api/reply",
        data,
        (response) => {
            alert(response.message);
        }
    )
}
$(document).ready(() => {
    $("#reply").click(async () => {
        await giveReply()
        window.location.href = "/page/give_all";
    })
    $("#back").click(() => {
        window.location.href = "/page/give_all";
    })
});