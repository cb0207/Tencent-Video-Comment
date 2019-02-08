# Tencent-Video-Comment
## 腾讯视频评论抓取步骤:

	1.手动打开对应视频网址，并找到评论。打开其他相同类型剧集网址，可发现0lmgk2kez0lztri为视频编号。
	2.通过来回手动按动评论区“加载评论”，配合使用fiddler找到评论内容具体网址。
	   a.初始评论地址为：http://video.coral.qq.com//filmreviewr/c/upcomment/0lmgk2kez0lztri?reqnum=2
	   b.之后的评论加载地址为：http://video.coral.qq.com/filmreviewr/c/upcomment/0lmgk2kez0lztri?commentid=6161326949500794924&reqnum=3
	3.分析网址地址找到视频编号，以及页面规律
	   a.网址中的commendid所对应的是上一个评论页面中最后一个评论的id：可用于后续循环构建评论地址
	4.可直接打开评论地址。虽然是一些代码，但可以通过观察格式获取对应内容。并使用eval解码打印，获取最后评论
