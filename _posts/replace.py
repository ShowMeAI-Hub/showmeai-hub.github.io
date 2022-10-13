old_str = '''<table id="customers" align="center">
    <tr>
        <th>技术方向</th>
        <th>课程及链接</th>
    </tr>
    <tr>
        <td rowspan="5">计算机数学基础</td>
        <td><a href="/mit-6.042j">MIT-计算机科学的数学基础</a></td>
    </tr>
    <tr>
        <td><a href="/uc-math100">辛辛那提大学-微积分I</a></td>
    </tr>
    <tr>
        <td><a href="/uc-math101">辛辛那提大学-微积分II</a></td>
    </tr>
    <tr>
        <td><a href="/uc-math1071">辛辛那提大学-离散数学</a></td>
    </tr>
    <tr>
        <td><a href="/stanford-engr108">斯坦福-线性代数与矩阵方法导论</a></td>
    </tr>
    <tr>
        <td rowspan="3">计算机科学导论</td>
        <td><a href="/stanford-cs105">斯坦福-计算机科学导论</a></td>
    </tr>
    <tr>
        <td><a href="/harvard-cs50-cs">哈佛-计算机科学导论</a></td>
    </tr>
    <tr>
        <td><a href="/mit-6.0001">MIT-计算机科学与Python编程导论</a></td>
    </tr>
    <tr>
        <td rowspan="2">数据结构与算法</td>
        <td><a href="/mit-6.046j">MIT-数据结构与算法设计</a></td>
    </tr>
    <tr>
        <td><a href="/umd-cmsc420-0101">马里兰大学-数据结构</a></td>
    </tr>
    <tr>
        <td rowspan="2">数据库</td>
        <td><a href="/cmu-14-455">CMU-数据库系统导论</a></td>
    </tr>
    <tr>
        <td><a href="/cmu-15-721">CMU-数据库系统进阶</a></td>
    </tr>
    <tr>
        <td rowspan="2">机器学习及应用</td>
        <td><a href="/cs229">斯坦福CS229</a></td>
    </tr>
    <tr>
        <td><a href="/mit-6.036">MIT-机器学习导论</a></td>
    </tr>
    <tr>
        <td rowspan="8">深度学习及应用</td>
        <td><a href="/cs230">斯坦福CS230</a></td>
    </tr>
    <tr>
        <td><a href="/harvard-cs50-ai">哈佛-Python人工智能入门</a></td>
    </tr>
    <tr>
        <td><a href="/mit-6.s191">MIT-深度学习导论</a></td>
    </tr>
    <tr>
        <td><a href="/ntu-hylee-ml">李宏毅-机器学习(&深度学习)</a></td>
    </tr>
    <tr>
        <td><a href="/tech-adl">应用深度学习(全知识点覆盖)</a></td>
    </tr>
    <tr>
        <td><a href="/berkeley-csw182">UC Berkeley-深度神经网络设计、可视化与理解</a></td>
    </tr>
    <tr>
        <td><a href="/wisc-stat453">威斯康星-深度学习和生成模型导论</a></td>
    </tr>
    <tr>
        <td><a href="/berkeley-fsdl">UC Berkeley-全栈深度学习训练营</a></td>
    </tr>
    <tr>
        <td rowspan="4">自然语言处理</td>
        <td><a href="/cs224n">斯坦福CS224n（深度学习与NLP）</a></td>
    </tr>
    <tr>
        <td><a href="/cs124">斯坦福CS124（从语言到信息）</a></td>
    </tr>
    <tr>
        <td><a href="/cs520">斯坦福CS520（知识图谱）</a></td>
    </tr>
    <tr>
        <td><a href="/umass-cs685">马萨诸塞-自然语言处理进阶</a></td>
    </tr>
    <tr>
        <td rowspan="3">计算机视觉</td>
        <td><a href="/cs231n">斯坦福CS231n（深度学习与CV）</a></td>
    </tr>
    <tr>
        <td><a href="/eecs498">密歇根eecs498（CS231n进阶课）</a></td>
    </tr>
    <tr>
        <td><a href="/adl4cv">慕尼黑工大adl4cv（深度学习与CV高阶课）</a></td>
    </tr>
    <tr>
        <td >多模态</td>
        <td><a href="/cmu-11-777">CMU-多模态机器学习</a></td>
    </tr>
    <tr>
        <td >图机器学习</td>
        <td><a href="/cs224w">斯坦福CS224w</a></td>
    </tr>
    <tr>
        <td rowspan="2">强化学习</td>
        <td><a href="/cs234">斯坦福CS234（强化学习）</a></td>
    </tr>
    <tr>
        <td><a href="/cs285">伯克利CS285（深度强化学习）</a></td>
    </tr>
    <tr>
        <td >无监督学习</td>
        <td><a href="/cs294-158">伯克利CS294-158（深度无监督学习）</a></td>
    </tr>
    <tr>
        <td rowspan="3">AI与生物医疗</td>
        <td><a href="/mit-6.874">MIT-面向生命科学的深度学习</a></td>
    </tr>
    <tr>
        <td><a href="/mit-6.047">MIT-基因组学机器学习</a></td>
    </tr>
    <tr>
        <td><a href="/mit-6.s897">MIT-医疗机器学习</a></td>
    </tr>
    <tr>
        <td rowspan="2">图形学与几何</td>
        <td><a href="/cmu-15-462">CMU-计算机图形学</a></td>
    </tr>
    <tr>
        <td><a href="/ammi-gml">AMMI-几何深度学习</a></td>
    </tr>
    <tr>
        <td rowspan="2">其他课程</td>
        <td><a href="/harvard-cs50-web">哈佛-基于Python/JavaScript的web编程</a></td>
    </tr>
    <tr>
        <td><a href="/mit-18.s191">MIT-计算思维导论(Julia)</a></td>
    </tr>
</table>'''

new_str = '''<table>
	<thead>
		<tr>
			<th>合辑</th>
			<th>课程链接</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td rowspan="5">
				<a href="https://www.showmeai.tech/tutorials/38">
					<strong>CS数学基础课程合辑</strong>
				</a>
			</td>
			<td>
				<a href="https://www.showmeai.tech/article-detail/346">【ENGR108】Stanford斯坦福 · 线性代数与矩阵方法导论课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/354">【6.042J】MIT麻省理工 · 计算机科学的数学基础课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/376">【MATH100】辛辛那提大学 · 微积分Ⅰ课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/377">【MATH101】辛辛那提大学 · 微积分Ⅱ课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/378">【MATH1071】辛辛那提大学 · 离散数学课程</a>
			</td>
		</tr>
		<tr>
			<td rowspan="9">
				<a href="https://www.showmeai.tech/tutorials/29">
					<strong>计算机基础课程合辑</strong>
				</a>
			</td>
			<td>
				<a href="https://www.showmeai.tech/article-detail/357">【14-455】CMU卡内基梅隆 · 数据库系统导论课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/358">【15-721】CMU卡内基梅隆 · 数据库系统进阶课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/359">【CS105】Stanford斯坦福 · 计算机科学导论课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/348">【CS50-CS】Harvard哈佛 · 计算机科学导论课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/362">【CS50-WEB】Harvard哈佛 · 基于Python / JavaScript的Web编程课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/349">【6.0001】MIT麻省理工 · 计算机科学与Python编程导论课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/363">【6.046J】MIT麻省理工 · 数据结构与算法设计课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/372">【18.S191】MIT麻省理工 · 计算思维导论(Julia)课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/385">【CMSC420】马里兰大学 · 数据结构课程</a>
			</td>
		</tr>
		<tr>
			<td rowspan="3">
				<a href="https://www.showmeai.tech/tutorials/28">
					<strong>机器学习课程合辑</strong>
				</a>
			</td>
			<td>
				<a href="https://www.showmeai.tech/article-detail/380">【AndrewNG-ML】吴恩达 · 机器学习专项课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/382">【CS229】Stanford斯坦福 · 机器学习课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/353">【6.036】MIT麻省理工 · 机器学习导论课程</a>
			</td>
		</tr>
		<tr>
			<td rowspan="10">
				<a href="https://www.showmeai.tech/tutorials/77">
					<strong>深度学习课程合辑</strong>
				</a>
			</td>
			<td>
				<a href="https://www.showmeai.tech/article-detail/379">【AndrewNG-DL】吴恩达 · 深度学习专项课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/383">【CS230】Stanford斯坦福 · 深度学习课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/355">【CSW182】Berkeley伯克利 · 深度神经网络设计、可视化与理解课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/356">【FSDL】Berkeley伯克利 · 全栈深度学习训练营课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/361">【CS50-AI】Harvard哈佛 · Python人工智能入门课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/386">【6.S191】MIT麻省理工 · 深度学习导论课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/373">【APPLY-DL】科罗拉多大学 · 应用深度学习(全知识点覆盖)课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/375">【STAT453】威斯康星 · 深度学习和生成模型导论课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/369">【T81-558】WUSTL · 深度神经网络应用案例实操课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/370">【HYLEE】李宏毅 · 机器学习(&amp;深度学习)课程</a>
			</td>
		</tr>
		<tr>
			<td rowspan="4">
				<a href="https://www.showmeai.tech/tutorials/55">
					<strong>NLP课程合辑</strong>
				</a>
			</td>
			<td>
				<a href="https://www.showmeai.tech/article-detail/384">【CS224n】Stanford斯坦福 · 深度学习与自然语言处理课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/360">【CS124】Stanford斯坦福 · 从语言到信息课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/351">【CS520】Stanford斯坦福 · 知识图谱课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/374">【CS685】马萨诸塞大学 · 自然语言处理进阶课程</a>
			</td>
		</tr>
		<tr>
			<td rowspan="3">
				<a href="https://www.showmeai.tech/tutorials/73">
					<strong>计算机视觉课程合辑</strong>
				</a>
			</td>
			<td>
				<a href="https://www.showmeai.tech/article-detail/381">【CS231n】Stanford斯坦福 · 深度学习与计算机视觉课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/350">【EECS498】Michigan密歇根 · 深度学习与计算机视觉(CS231n进阶课)</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/343">【ADL4CV】慕尼黑工大 · 计算机视觉深度学习进阶课</a>
			</td>
		</tr>
		<tr>
			<td rowspan="2">
				<a href="https://www.showmeai.tech/tutorials/87">
					<strong>强化学习课程合辑</strong>
				</a>
			</td>
			<td>
				<a href="https://www.showmeai.tech/article-detail/345">【CS285】Berkeley伯克利 · 深度强化学习课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/347">【CS234】Stanford斯坦福 · 强化学习课程</a>
			</td>
		</tr>
		<tr>
			<td rowspan="3">
				<a href="https://www.showmeai.tech/tutorials/74">
					<strong>AI生物医疗课程合辑</strong>
				</a>
			</td>
			<td>
				<a href="https://www.showmeai.tech/article-detail/364">【6.047】MIT麻省理工 · 基因组学机器学习课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/367">【6.874】MIT麻省理工 · 面向生命科学的深度学习课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/371">【6.S897】MIT麻省理工 · 医疗机器学习课程</a>
			</td>
		</tr>
		<tr>
			<td rowspan="6">
				<a href="https://www.showmeai.tech/tutorials/76">
					<strong>其他名校AI课程合辑</strong>
				</a>
			</td>
			<td>
				<a href="https://www.showmeai.tech/article-detail/344">【CS294】Berkeley伯克利 · 深度无监督学习课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/365">【11-777】CMU卡内基梅隆 · 多模态机器学习课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/366">【15-462】CMU卡内基梅隆 · 计算机图形学课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/352">【CS224W】Stanford斯坦福 · 图机器学习课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/368">【6.S094】MIT麻省理工 · 深度学习与无人驾驶课程</a>
			</td>
		</tr>
		<tr>
			<td>
				<a href="https://www.showmeai.tech/article-detail/387">【GDL】AMMI · 几何深度学习课程</a>
			</td>
		</tr>
	</tbody>
</table>'''

# replace file contents with regular expression
import re
import os

def file_content_replace_reg_pattern(path):
    with open(path, 'r') as f:
        data = f.read()
    with open(path, 'w') as f:
        data = data.replace(old_str, new_str)
        data = data.replace("#E4822D", '\"#E4822D\"')

        pattern = "\[(.*?)\*\*(.*?)\*\*\]\((.*?)\)"
        data = re.sub(pattern, r'<a href="\3">\1<strong>\2</strong></a>', data)

        pattern = "(<center>.*?)\*\*(.*?)\*\*.*?(</center>)"
        data = re.sub(pattern, r"\1<strong>\2</strong>\3", data)

        data = data.replace("<br>", '')
        data = data.replace("\n##", '\n<br>\n##')

        f.write(data)

def file_modify(path):
    for filename in os.listdir(path):
        if os.path.isdir(filename):
            file_modify(filename)
        elif os.path.isfile(filename) and filename.endswith(".md"):
            print(filename)
            file_content_replace_reg_pattern(filename)
        else:
            pass

file_modify(".")