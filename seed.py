from chatbot.models import *
from team_info import user


Target.objects.all().delete()
Target.objects.create(
    id = 1,
    type = "人際",
)
Target.objects.create(
    id = 2,
    type = "經濟",
)
Target.objects.create(
    id = 3,
    type = "學業",
)
Target.objects.create(
    id = 4,
    type = "事業",
)
Target.objects.create(
    id = 5,
    type = "感情",
)
Target.objects.create(
    id = 6,
    type = "其他",
)

Article.objects.all().delete()
Article.objects.create(
    id = 1,
    title = "好煩",
    creator = user[0]["user_id"],
    content = "身為社交恐懼症，我一點也不想開學... 什麼時候才放假... 你們都怎麼調適自己? QAQ",
    time = "2022-09-22 14:28:00",
)
Article.objects.create(
    id = 2,
    title = "要考試了",
    creator = user[0]["user_id"],
    content = "要考試，明明每天都讀了好幾個小時，卻總是覺得讀不進去... 我該怎麼辦...",
    time = "2022-09-22 15:17:16",
)
Article.objects.create(
    id = 3,
    title = "比賽",
    creator = user[1]["user_id"],
    content = "最近要比賽了，有人可以幫我加油集氣嗎",
    time = "2022-09-23 08:03:28",
)
Article.objects.create(
    id = 4,
    title = "表演",
    creator = user[1]["user_id"],
    content = "要出表演了... 雖然平常練習了很久... 但還是擔心會表演得不好... 怎麼辦... 不想害大家出糗...",
    time = "2022-09-23 12:28:10",
)
Article.objects.create(
    id = 5,
    title = "我想休息",
    creator = user[2]["user_id"],
    content = "最近事情好多，好累... 快要撐不下去了... 我可以休息嗎...",
    time = "2022-09-24 19:30:00",
)
Article.objects.create(
    id = 6,
    title = "why",
    creator = user[2]["user_id"],
    content = "明明就沒做什麼事情... 但卻突然間不理我了... 為什麼... 我到底做錯什麼了...",
    time = "2022-09-24 20:20:21",
)

Reply.objects.all().delete()
Reply.objects.create(
    article = Article.objects.get(id=2),
    creator = user[1]["user_id"],
    content = "相信自己，你可以的!",
    time = "2022-09-22 19:00:28",
)
Reply.objects.create(
    article = Article.objects.get(id=2),
    creator = user[1]["user_id"],
    content = "再撐一下，就快結束了~",
    time = "2022-09-22 19:03:17",
)
Reply.objects.create(
    article = Article.objects.get(id=2),
    creator = user[2]["user_id"],
    content = "別擔心，沒事的，其實你都有讀進去，只是現在比較慌張而已~",
    time = "2022-09-23 10:25:08",
)
Reply.objects.create(
    article = Article.objects.get(id=2),
    creator = user[2]["user_id"],
    content = "ok 的啦，不要太緊張，拿出你全部的實力去考試吧! 加油!",
    time = "2022-09-23 10:30:00",
)
Reply.objects.create(
    article = Article.objects.get(id=3),
    creator = user[0]["user_id"],
    content = "加油!",
    time = "2022-09-23 17:00:01",
)
Reply.objects.create(
    article = Article.objects.get(id=3),
    creator = user[2]["user_id"],
    content = "比賽加油!",
    time = "2022-09-23 23:15:18",
)
Reply.objects.create(
    article = Article.objects.get(id=3),
    creator = user[2]["user_id"],
    content = "期待你的好消息!",
    time = "2022-09-24 02:15:11",
)

Counselor.objects.all().delete()
# real
Counselor.objects.create(
    user_id = user[0]["user_id"],
    user_name = user[0]["display_name"],
    line_id = "xxxx",
    gender = "男",
    age = "20",
    job = "學生",
    description = "一個非專業的諮商師",
    image = user[0]["image"],
    is_professional = False,
    can_be_paired = True,
).target.set([1, 2])
Counselor.objects.create(
    user_id = user[1]["user_id"],
    user_name = user[1]["display_name"],
    line_id = "oooo",
    gender = "不透露",
    age = None,
    job = "諮商師",
    description = "一個專業且神秘的諮商師",
    image = user[1]["image"],
    is_professional = True,
    can_be_paired = True,
).target.set([1, 2, 3, 4, 5, 6])
Counselor.objects.create(
    user_id = user[2]["user_id"],
    user_name = user[2]["display_name"],
    line_id = "idid",
    gender = "女",
    age = "20",
    job = None,
    description = "不開放配對...",
    image = user[2]["image"],
    is_professional = False,
    can_be_paired = False,
).target.set([1, 4])

# fake
Counselor.objects.create(
    user_id = "banana",
    user_name = "Banana",
    line_id = "banana",
    gender = "女",
    age = "33",
    job = "Banana",
    description = "Banana 諮商師",
    image = "https://images.unsplash.com/photo-1481349518771-20055b2a7b24?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1239&q=80",
    is_professional = False,
    can_be_paired = True,
).target.set([1, 3, 5])
Counselor.objects.create(
    user_id = "cactus",
    user_name = "Cactus",
    line_id = "cactus",
    gender = "男",
    age = None,
    job = None,
    description = "我帶刺但我很溫柔",
    image = "https://images.unsplash.com/photo-1459411552884-841db9b3cc2a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=474&q=80",
    is_professional = True,
    can_be_paired = True,
).target.set([1, 2, 3])
Counselor.objects.create(
    user_id = "coffee",
    user_name = "Coffee",
    line_id = "coffee",
    gender = "女",
    age = "24",
    job = "心理醫生",
    description = "來杯咖啡，慢慢說吧~",
    image = "https://images.unsplash.com/photo-1613336026275-d6d473084e85?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
    is_professional = True,
    can_be_paired = True,
).target.set([2, 3, 5])
