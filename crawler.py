import urllib.request
import re
import http.cookiejar
#视频编号
vid="0lmgk2kez0lztri"
#初始评论地址
url1="http://video.coral.qq.com//filmreviewr/c/upcomment/"+vid+"?reqnum=2"

#构建header，伪装浏览器
headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Encoding":"gb2312,uft-8",
	"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	"User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:57.0)Gecko/20100101Firefox/57.0",
	"Connection":"keep-alive",
	"referer":"qq.com"}
#设置cookie
cjar=http.cookiejar.CookieJar()
#创建opener，并添加header，cookie
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
headall=[]
for key,value in headers.items():
	item=(key,value)
	headall.append(item)
	opener.addheaders=headall
#安装全局opener
urllib.request.install_opener(opener)

#自定义函数爬取评论信息
def crawd (vid,comid):
	url="http://video.coral.qq.com/filmreviewr/c/upcomment/"+vid+"?commentid="+comid+"&reqnum=3"
	data=urllib.request.urlopen(url).read().decode("utf-8")
	return data
#正则表达式，评论id，用户，评论内容
idpat='"id":"(.*?)"'
nickpat='"nick":"(.*?)",'
contpat='"content":"(.*?)",'

#爬取评论内容，初始设置1~10页
for j in range(1,10):
	if j==1:
		data=urllib.request.urlopen(url1).read().decode("utf-8")
	else:
		data=crawd(vid,comid)
	idlist=re.compile(idpat,re.S).findall(data)
	nicklist=re.compile(nickpat,re.S).findall(data)
	contentlist=re.compile(contpat,re.S).findall(data)
	print("-"*10)
	print("第"+str(j)+"页评论")
	for I in range(0,len(idlist)):
		print("用户名是:"+eval('u"'+nicklist[i]+'"'))
		print("评论内容是:"+eval('u"'+contentlist[i]+'"'))
		print("\n")
		comid=idlist[len(idlist)-1]
