def home_bl_api(request):
    method = request.POST.get("method","GET")
    url = request.POST.get("url")

    if not url:
        return HttpResponseForbidden()
    if method == "POST":
        res = requests.post(url=url,headers=api_headers)
    if method == "GET":
        res = requests.get(url=url,headers=api_headers)


    response = HttpResponse(res.content)
    del res.headers["Transfer-Encoding"]
    del res.headers["Connection"]
    response.headers = res.headers
    response.status_code = res.status_code
    return response
    
    """
    
https://api.bilibili.com/x/web-show/res/locs?pf=0&ids=3449  赛事
https://api.bilibili.com/x/web-interface/index/top/feed/rcmd?y_num=4&fresh_type=4。。。。。1&brush=1&homepage_ver=1&ps=15  首页推送视频，赛事下边

https://api.bilibili.com/pgc/web/timeline/v2?day_before=6&day_after=0&season_type=1 番剧板块
https://api.bilibili.com/x/web-interface/index/top/feed/rcmd?y_num=4&fresh_type=4&feed_version=V4&fresh_idx_1h=2&fetch_row=7&fresh_idx=2&brush=2&homepage_ver=1&ps=15 首页推送视频，番剧下边

https://api.bilibili.com/pgc/web/timeline/v2?day_before=6&day_after=0&season_type=4 国创板块
https://api.bilibili.com/x/web-interface/index/top/feed/rcmd?y_num=4&fresh_type=4&feed_version=V4&fresh_idx_1h=3&fetch_row=10&fresh_idx=3&brush=3&homepage_ver=1&ps=15 国创下边 推荐视频

https://manga.bilibili.com/twirp/comic.v1.Comic/GetRecommendComics 漫画板块 POST
https://manga.bilibili.com/twirp/comic.v1.Comic/HomeHot 漫画相关 POST 50个 可能是换一换
https://api.bilibili.com/x/web-interface/index/top/feed/rcmd?y_num=4&fresh_type=4&feed_version=V4&fresh_idx_1h=4&fetch_row=13&fresh_idx=4&brush=4&homepage_ver=1&ps=15 首页推送视频，漫画下边

    https://manga.bilibili.com/twirp/comic.v1.Comic/HomeHot?device=pc&platform=web 漫画相关 POST
    https://manga.bilibili.com/twirp/comic.v1.Comic/Recommend?device=pc&platform=web 漫画推荐 POST

https://api.bilibili.com/pugv/app/web/floor/switch?load_type=1 课堂板块
https://api.bilibili.com/x/web-interface/index/top/feed/rcmd?y_num=4&fresh_type=4&feed_version=V4&fresh_idx_1h=5&fetch_row=16&fresh_idx=5&brush=5&homepage_ver=1&ps=15 首页推送视频，课堂下边

https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&pn=1&rid=23 电影板块
https://api.bilibili.com/x/web-interface/index/top/feed/rcmd?y_num=4&fresh_type=4&feed_version=V4&fresh_idx_1h=6&fetch_row=19&fresh_idx=6&brush=6&homepage_ver=1&ps=15 首页推送视频，电影下边

https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&pn=1&rid=11 电视剧
推送
https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&pn=1&rid=177 纪录片
推送
https://api.bilibili.com/x/article/recommends?ps=15 专栏
推送





https://api.bilibili.com/x/player/playurl?qn=32&fnver=0&fnval=16&fourk=1&voice_balance=1&。。。y1T7gv&cid=833877319 该视频质量，格式
https://api.bilibili.com/x/web-interface/view?aid=388049169 该视频相关推荐
https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid=833330694&pid=388049169&segment_index=1 该视频小窗弹幕
https://api.bilibili.com/x/player/v2?aid=430654848&cid=835844002 观者信息
"""
