#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lxml import etree

wb_data = """
       </span><div class="watch-later-trigger watch-later"></div></div></a><div class="info"><div class="headline clearfix"><span class="type avid">av5236569</span><span class="type hide">野生技术协会</span><a title="【Python】这可能是你见过的最简洁最没有废话的Python教程" href="//www.bilibili.com/video/av5236569?from=search&amp;seid=9646425581758693480" target="_blank" class="title">【<em class="keyword">Python</em>】这可能是你见过的最简洁最没有废话的<em class="keyword">Python</em>教程</a></div><div class="des hide">
        正确的学习姿势
主动学习。这个教程的一大特点就是简洁（需要你去搜索再搜索）比如讲类的时候，指着这一行说这就是这个类的构造函数（真的是一句带过），这时请打开百度搜索“python 类构造函数”。
实践，听完之后，不能就这么过去了，墙裂推荐刷l...
        """
html = etree.HTML(wb_data)
print(html)
result = etree.tostring(html,encoding = "UTF-8")
print(result.decode("UTF-8"))



##############################  输出  ##############################

<html>

<body>
    <div class="watch-later-trigger watch-later" />
    <div class="info">
        <div class="headline clearfix">
            <span class="type avid">av5236569</span>
            <span class="type hide">野生技术协会</span>
            <a title="【Python】这可能是你见过的最简洁最没有废话的Python教程" href="//www.bilibili.com/video/av5236569?from=search&amp;seid=9646425581758693480"
                target="_blank" class="title">【
                <em class="keyword">Python</em>】这可能是你见过的最简洁最没有废话的
                <em class="keyword">Python</em>教程</a>
        </div>
        <div class="des hide">
            正确的学习姿势 主动学习。这个教程的一大特点就是简洁（需要你去搜索再搜索）比如讲类的时候，指着这一行说这就是这个类的构造函数（真的是一句带过），这时请打开百度搜索“python 类构造函数”。 实践，听完之后，不能就这么过去了，墙裂推荐刷l...
        </div>
    </div>
</body>

</html>

