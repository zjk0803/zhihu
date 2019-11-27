from bs4 import BeautifulSoup

import requests
allowed_domains = ["www.zhihu.com"]
start_urls = ['https://www.zhihu.com/']
#website = "https://www.zhihu.com/people/xia-si-gou/activities"
start_answer_url = " https://www.zhihu.com/api/v4/questions/354577663/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=3&offset=3&platform=desktop&sort_by=default"
headers = {"User_Argent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}
result = requests.get(start_answer_url,headers = headers)

result.encoding = "utf-8"

content = result.text

print(content)
var b = function(e) {
        return __g._encrypt(encodeURIComponent(e))
    };
e: "client_id=c3cef7c66a1843f8b3a9e6a1e3160e20&grant_type=password&timestamp=1574857351044&source=com.zhihu.web&signature=bbe519d38e788500397920580a65842d6242e999&username=kunco2%40qq.com&password=z348461436&captcha=&lang=cn&utm_source=&ref_source=other_https%3A%2F%2Fwww.zhihu.com%2Fsignin%3Fnext%3D%252F"

e: "client_id=c3cef7c66a1843f8b3a9e6a1e3160e20" \
   "&grant_type=password" \
   "&timestamp=1574857351044" \
   "&source=com.zhihu.web" \
   "&signature=bbe519d38e788500397920580a65842d6242e999" \
   "&username=kunco2%40qq.com" \
   "&password=z348461436" \
   "&captcha=" \
   "&lang=cn" \
   "&utm_source=" \
   "&ref_source=other_https%3A%2F%2Fwww.zhihu.com%2Fsignin%3Fnext%3D%252F"
