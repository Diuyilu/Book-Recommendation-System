<template>
  <RouterView> </RouterView>
  <div v-show="flag">
    <div>
      <el-row>
        <el-col :span="24">
          <div style="font-size: 20px">曾经看过</div>
          <el-row class="book_list" :gutter="40">
            <el-col
              :span="3"
              v-for="book in tableData()"
              :key="book.db_id"
              style="margin-bottom: 20px"
            >
              <el-card
                class="box-card"
                shadow="hover"
                style="height: 280px; width: 200px; border: 0px; cursor: pointer"
                @click="push_router(book.db_id)"
              >
                <img :src="book.image_address" style="width: 155px" id="image" />
              </el-card>
              <div class="book_title">
                {{ book.book_title }}
              </div>
            </el-col>
          </el-row>
        </el-col>
        <div class="pagination-block">
          <!-- <div class="example-demonstration">分页</div> -->
          <el-pagination
            background
            :page-sizes="[7, 10]"
            :page-size="7"
            layout="prev, pager, next"
            :total="state.total"
            @current-change="handleCurrentChange"
            @size-change="handleSizeChange"
          />
        </div>
      </el-row>
      <el-row>
        <div style="font-size: 20px">你的标签</div>
      </el-row>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { onMounted, watch, reactive, ref } from 'vue'
import { on } from 'events'

let flag = true
const message = ref()

const get_history_book_info = async () => {
  message.value = books
  state.total = books.length
}

const tableData = () => {
  if (message.value) {
    return message.value.filter(
      (item, index) => index < state.page * state.limit && index >= state.limit * (state.page - 1)
    )
  } else return []
}

const router = useRouter()
function push_router(db_id) {
  const book_id = db_id
  console.log(book_id)
  router.push({
    name: 'historyinfo',
    query: {
      book_id: JSON.stringify(book_id)
    }
  })
}

function change_flag(x) {
  flag = x
}

watch(
  () => router.currentRoute.value.name,
  (to, from) => {
    if (to === 'historyinfo') {
      change_flag(false)
    } else if (to === 'history') {
      change_flag(true)
    }
  }
)

const state = reactive({
  page: 1,
  limit: 7,
  // total: message.value.length
  total: 0
})

const handleCurrentChange = (e) => {
  state.page = e
}
//改变页数限制
const handleSizeChange = (e) => {
  state.limit = e
}

onMounted(() => {
  console.log('yesyesyes!')
  get_history_book_info()
})

const books = [
  {
    ISBN: '9787111114741',
    author: '王佑',
    author_introduction:
      '\n    王佑先生，企业资源管理研究中心资深顾问，AMT个人高级会员，拥有多年的国际国内管理咨询产业研究经验，曾广泛深入地参与中国企业管理提升及住处化应用咨询实践。成功领导、参与为多家知名企业（如国家电力华东公司、正泰集团、大唐电信、白沙集团、海信集团、东方电子等）提供咨询建议。作为特约撰稿，有多篇专篇文章在经济管理类及IT信息类著名报刊与核心期刊上发表。同时，王佑先生参与在国内较早地提出了“甲方咨询”模式，并在多家企业取得成功实践。\n    \n    主要培训领域： 像咨询顾问一样思考、人力资源管理及I',
    binding: '精装(无盘)',
    book_link: 'https://book.douban.com/subject/1075677/',
    book_subtitle: null,
    book_title: '像咨询顾问一样思考',
    collection_time: '2023-09-19',
    content_validity:
      '\n    管理咨询行业是当今为数不多的高收益行业之一，同时也是最引人入胜的行业之一。这个略带神秘的行业留下了很多疑惑，管理咨询究竟能给企业带来什么？咨询顾问如何对企业进行诊断和研究？怎样才能成为一名优秀的咨询顾问？企业如何选择合适的咨询公司开展咨询项目？……        本书将为你解开这些疑惑。',
    db_id: '1075677',
    half_rating: '4.0',
    image_address:
      'https://images.weserv.nl/?url=/img1.doubanio.com/view/subject/s/public/s1177110.jpg',
    label: '商业',
    menu: '\n        丛书序\n        前言\n        第一部分 拨开管理咨询的重重迷雾：其实管理咨询并不神秘\n        第二部分 掌握管理咨询的方法论：你也能成为优秀的咨询顾问\n        第三部分 专业咨询顾问的百宝箱----管理咨询的分析工具\n        第四部分 揭示咨询项目的工作流程：深入了解咨询顾问的工作步骤\n        第五部分 分析咨询项目的成功要素：小心掉入咨询的“陷阱”\n        第六部分 认识咨询公司的管理要素：对咨询公司的“咨询”\n        附',
    original_title: null,
    pages: '347',
    press: '\n      机械工业出版社\n    ',
    price: '36.00',
    pubdate: '2003-2-1',
    rating: '8.0 ',
    rating_number: '28',
    series: '无',
    series_link: '无',
    translator: '无',
    translator_introduction: '无'
  },
  {
    ISBN: '9787115614162',
    author: '[荷] 费莉安·赫尔曼斯 (Felienne Hermans)',
    author_introduction:
      '\n    费莉安•赫尔曼斯（Felienne Hermans），荷兰莱顿大学副教授，致力于研究人类如何利用认知科学快速、高效地学习程序设计语言。费莉安对ChatGPT给软件工程领域带来的深远影响有独到见解，多次就这一话题接受媒体专访。她是TC39（JavaScript标准委员会） 成员，还自创了Hedy程序设计语言。',
    binding: '平装',
    book_link: 'https://book.douban.com/subject/36362026/',
    book_subtitle: null,
    book_title: '程序员超强大脑',
    collection_time: '2023-09-20',
    content_validity:
      '\n    为什么你在写代码时总会遇到这样或那样的问题？为什么你总是记错某些语法？为什么有些人能够快速学会新的编程语言，而有些人则不能？在试图解决困难或复杂的问题时，我们的大脑其实有一套特定的工作方式。本书从认知科学角度剖析优秀程序设计背后的脑科学原理，为你揭开大脑思考编程的奥秘。本书分为四大部分，共有13章。你将了解如下内容：如何高效地学习新的编程语言，如何快速地理解复杂的代码，如何牢固地记住各种语法，如何在繁杂的程序设计工作中优化认知资源。    编辑推荐    随着ChatGPT横空出世，作为程序员的',
    db_id: '36362026',
    half_rating: 0,
    image_address:
      'https://images.weserv.nl/?url=/img2.doubanio.com/view/subject/s/public/s34522383.jpg',
    label: '编程',
    menu: '\n        第 一部分 代码阅读\n        第 1章 剖析程序设计之惑 2\n        1.1 代码造成的各种困惑 2\n        1.1.1 第 一种困惑：缺乏知识 3\n        1.1.2 第二种困惑：缺乏信息 4\n        1.1.3 第三种困惑：缺乏加工能力 4\n        1.2 影响程序设计的不同认知过程 5\n        1.2.1 长时记忆和程序设计 5\n        1.2.2 短时记忆和程序设计 6\n        1.2.3 工作记忆和程序设计',
    original_title: "The Programmer's Brain",
    pages: '214',
    press: '人民邮电出版社',
    price: '89.8元',
    pubdate: '2023-5',
    rating: 0,
    rating_number: '0',
    series: '图灵程序设计丛书·程序员修炼系列',
    series_link: 'https://book.douban.com/producers/42',
    translator: '蒋楠',
    translator_introduction: '无'
  },
  {
    ISBN: '9787521734782',
    author: '[瑞典] 英格玛·伯格曼',
    author_introduction:
      '\n    作者简介    英格玛·伯格曼 | INGMAR BERGMAN    享誉全球的电影、戏剧导演，作家、编剧。1918 年7 月14 日出生于瑞典的乌普萨拉，2007 年7 月30 日在法罗岛的家中与世长辞，享年89 岁。    伯格曼活跃于影坛、戏剧舞台超过60 年，一生编剧、执导60 余部电影、170 余部戏剧。他曾荣获威尼斯电影节终身成就奖、奥斯卡最佳外语片等多项国际电影大奖，被誉为“导演中的导演”“电影界的哲学家”“作者电影第一人”。    在文学领域，伯格曼也有着极高的造诣，因其戏剧剧',
    binding: '精装',
    book_link: 'https://book.douban.com/subject/35578733/',
    book_subtitle: '伯格曼文集',
    book_title: '我们都是马戏团',
    collection_time: '2023-09-14',
    content_validity:
      '\n    【编辑推荐】    ★影史巨匠伯格曼60年文选结集出版，瑞典语直译，首次译介为简体中文版    ★伯格曼基金会、斯德哥尔摩城市档案馆、瑞典电影局等权威机构多份珍贵档案首度公开    ★写作历程跨越60 余年，收录80 余篇文章，揭开伯格曼复杂、隐秘的内心世界    ★通透深刻、真诚温柔、自恋自嘲、尖酸刻薄、 辛辣幽默，全方位展现多面伯格曼    【内容简介】    伯格曼：我的恐惧是关于被消耗的情感，那些沉寂中的人们隐藏的无言之苦。我相信——至少我愿意相信——电影的最大的使命就是为观众竖起一面镜',
    db_id: '35578733',
    half_rating: '4.2',
    image_address:
      'https://images.weserv.nl/?url=/img2.doubanio.com/view/subject/s/public/s34126211.jpg',
    label: '艺术',
    menu: '\n        前言：诗歌的诞生 / i\n        第一部分：艺术与艺术家\n        关于艺术的角色\n        关于《第七封印》 / 3\n        亲爱的可怕的观众! / 6\n        犹在镜中 / 8\n        我的钢琴家 / 11\n        蛇皮 / 18\n        每个人都有梦想、欲望和需求 / 23\n        关于电影\n        魔幻的市场娱乐 / 28\n        三条蜈蚣腿 / 31\n        把玩珍珠 / 39\n    ',
    original_title: null,
    pages: '416',
    press: '中信出版集团',
    price: '69.00元',
    pubdate: '2022-2',
    rating: '8.3 ',
    rating_number: '220',
    series: '雅众·电影',
    series_link: 'https://book.douban.com/series/51678',
    translator: '王凯梅',
    translator_introduction: '无'
  },
  {
    ISBN: '9781718502604',
    author: 'Jeremy Kubica',
    author_introduction:
      '\n    Jeremy Kubica is an engineer director specializing in artificial intelligence and machine learning. He received a Ph.D. in Robotics from Carnegie Mellon University and a BS in Computer Science from Cornell University. He spent his graduate school yea',
    binding: 'Paperback',
    book_link: 'https://book.douban.com/subject/36217372/',
    book_subtitle: 'An Amusing Adventure with Coffee-Filled Examples',
    book_title: 'Data Structures the Fun Way',
    collection_time: '2023-09-15',
    content_validity:
      '\n    This accessible and entertaining book provides an in-depth introduction to computational thinking through the lens of data structures — a critical component in any programming endeavor. Through diagrams, pseudocode, and humorous analogies, you’ll lea',
    db_id: '36217372',
    half_rating: 0,
    image_address:
      'https://images.weserv.nl/?url=/img1.doubanio.com/view/subject/s/public/s34394720.jpg',
    label: '数学',
    menu: '\n        Introduction\n        Chapter 1: Information in Memory\n        Chapter 2: Binary Search\n        Chapter 3: Dynamic Data Structures\n        Chapter 4: Stacks and Queues\n        Chapter 5: Binary Search Trees\n        Chapter 6: Tries and Adapting Da',
    original_title: null,
    pages: '304',
    press: '‎No Starch Press',
    price: null,
    pubdate: '2022-11',
    rating: 0,
    rating_number: '0',
    series: '无',
    series_link: '无',
    translator: '无',
    translator_introduction: '无'
  },
  {
    ISBN: '9787300110929',
    author: '哈维·S·罗森(Harvey.S.Rosen)',
    author_introduction:
      '\n    哈维·S·罗森是普林斯顿大学约翰·温伯格(JohnL．Weinberg)经济学和商业政策教授，计量经济学会会员，国家经济研究局研究员。主要研究领域包括财政学、劳动经济学、应用微观经济学。1989-1991年，他曾任美国财政部部长助理代表（税收分析）。2003-2005年，先是作为总统经济顾问委员会的委员，后担任该委员会的主席。',
    binding: '平装',
    book_link: 'https://book.douban.com/subject/4048193/',
    book_subtitle: null,
    book_title: '财政学',
    collection_time: '2023-10-25',
    content_validity:
      '\n    本书自1985年第一版面世以来，一直是美国一流大学的首选教科书。本书最显著的特色是吸收了近30年来西方财政学理论的新进展。其目标是将制度、理论和经济计量等方面的内容交织在一起，让学生对于政府的开支和征税活动具有一个清晰而连贯的认识。本书适合作为财经院校本科及研究生的财政学教材，也可作为相关领域人员的参考书。',
    db_id: '4048193',
    half_rating: '4.5',
    image_address:
      'https://images.weserv.nl/?url=/img2.doubanio.com/view/subject/s/public/s6077412.jpg',
    label: '经济学',
    menu: '\n        第1篇　开场白\n        第1章　导论\n        财政思想\n        政府一览\n        小结\n        讨论题\n        附录：有关财政问题的研究\n        第2章　实证分析工具\n        理论的作用\n        因果性与相关性\n        实验研究\n        观察研究\n        准实验研究\n        结论\n        小结\n        讨论题\n        第3章　规范分析工具\n        福利经',
    original_title: null,
    pages: '575',
    press: '\n      中国人民大学出版社\n    ',
    price: '63.00元',
    pubdate: '2009-9',
    rating: '8.9 ',
    rating_number: '236',
    series: '经济科学译丛',
    series_link: 'https://book.douban.com/series/2942',
    translator: '郭庆旺',
    translator_introduction: '无'
  },
  {
    ISBN: '9787569923445',
    author: '鲁迅',
    author_introduction:
      '\n    选编者：陈平原    1954－    广东潮州人。中国现代文学研究的一座高峰。    北京大学中文系教授（2008－2012年任北大中文系主任）、教育部“长江学者”特聘教授、中央文史研究馆馆员、国务院学位委员会学科评议组成员，中国俗文学学会会长。    他对20世纪中国文学、中国小说与中国散文、现代中国教育及学术、图像与文字等领域有着精深研究和独到见解。    代表作品丨《中国小说叙事模式的转变》《千古文人侠客梦》《中国散文小说史》等。',
    binding: '双封',
    book_link: 'https://book.douban.com/subject/30230500/',
    book_subtitle: null,
    book_title: '生生死死',
    collection_time: '2023-10-23',
    content_validity:
      '\n    《生生死死》收集了由陈平原选编的周作人、鲁迅、梁实秋、冰心、俞平伯等42位名家的60篇谈论“生”与“死”话题的文章，大致区分为“生死意义”“丧祭仪式与生者”“关于自杀的种种”和“人到中年”四个部分。人终有一死，如何向死而生。书中作者对于生死各自不同的感悟、对生命意义的总结让我们看到不同年龄、不同阶层生死观的同时，也提醒每个人“好好的活”“好好的死”，努力追寻生命的意义。',
    db_id: '30230500',
    half_rating: '3.9',
    image_address:
      'https://images.weserv.nl/?url=/img9.doubanio.com/view/subject/s/public/s29780724.jpg',
    label: '散文',
    menu: '无',
    original_title: null,
    pages: '320',
    press: '\n      北京时代华文书局\n    ',
    price: '49.80',
    pubdate: '2018-6-1',
    rating: '7.8 ',
    rating_number: '76',
    series: '漫说文化丛书',
    series_link: 'https://book.douban.com/series/42176',
    translator: '无',
    translator_introduction: '无'
  },
  {
    ISBN: '9787511045751',
    author: '[日] 坂卓磨',
    author_introduction:
      '\n    著绘者：坂卓磨    1974年出生于日本神奈川县。大学学习工程专业，毕业后一边在公司上班，一边从事喜欢的绘画创作。从2012年起，在培养了许多绘本作家的著名绘本培训中心，跟随绘本名家深入学习绘本创作。《雪地下面的朋友们》就是他基于这个时期的创意出版的绘本处女作，且一鸣惊人，作为日本绘本作家的今日之星而广受瞩目。    译者：彭懿    儿童文学作家、绘本研究者及推广者。曾获中国新闻出版领域的蕞高奖中国出版政府奖，以及冰心儿童图书奖、第十一届亚太地区出版者协会图书奖翻译铜奖等。他是中国蕞早研究绘',
    binding: '精装',
    book_link: 'https://book.douban.com/subject/34885060/',
    book_subtitle: null,
    book_title: '雪地下面的朋友们',
    collection_time: '2023-09-18',
    content_validity:
      '\n    《雪地下面的朋友们》是丁虹绘本馆神奇旅行绘本系列精品，适合3～6岁儿童阅读，带领我们进入一个极富想象力、神秘奇幻的世界。    地面，大雪覆盖，地下，是动物们温馨的家。    一只冒失的鼹鼠不期的造访给寂寞的兔子增添了温暖和乐趣。随后，鼹鼠和兔子一起挖洞，打通了动物们之间温馨的交流......虽然每个动物都有各自的兴趣爱好，但一个人真的好孤独，总好像缺少些什么。于是，大家就往旁边的邻居家里挖呀挖，一个动物、两个动物……越来越多的动物们汇集在一起。    雪地下面的世界，由于有了这些朋友们而变得更',
    db_id: '34885060',
    half_rating: 0,
    image_address:
      'https://images.weserv.nl/?url=/img2.doubanio.com/view/subject/s/public/s33925293.jpg',
    label: '绘画',
    menu: '无',
    original_title: null,
    pages: '40',
    press: '\n      海豚出版社\n    ',
    price: '56.00元',
    pubdate: '2019-11',
    rating: 0,
    rating_number: '0',
    series: '神奇旅行绘本系列',
    series_link: 'https://book.douban.com/series/57877',
    translator: '彭懿',
    translator_introduction: '无'
  },
  {
    ISBN: '9787545539509',
    author: '丰子恺',
    author_introduction:
      '\n    丰子恺。画家、散文家，卓有成就的文艺大师，师从弘一法师，学贯中西。朱自清、郁达夫、巴金、叶圣陶、林清玄，对其文章和漫画赞誉有加。日本汉学家吉川幸次郎则说，丰子恺是最中国的中国人。他的散文兼有平易纯朴之风、宽仁隽永之意和童真天然之趣，是现代文学中备受推崇的佳品，多篇被选入教材，作语文教育典范。其漫画幽默风趣，流传广泛，深受人们的喜爱，读者争相收藏。',
    binding: null,
    book_link: 'https://book.douban.com/subject/30330588/',
    book_subtitle: '丰子恺散文漫画精品集',
    book_title: '不负人间好',
    collection_time: '2023-10-23',
    content_validity:
      '\n    这是丰子恺散文漫画精品集中的一本，特别收录了《生机》《无常之恸》《实行的悲哀》等31篇经典散文，回忆形色各人：感怀细微事物，悲哀中生出珍重，举重若轻，感人肺腑。    浮生若梦，心中有慈悲，山河远阔，人间烟火，不辜负走这一趟。    文艺大师丰子恺告诉你，在复杂世界里，过好珍贵一生的四种核心能力：质朴、有趣、发现美好、坦然率真。    丰子恺女儿丰一吟授权审阅版本。丰子恺散文漫画精品集系列中的第一本《此生多珍重》入选读者票选年度十大好书。    丰子恺的这套散文漫画集精选了120多篇丰子恺的经典',
    db_id: '30330588',
    half_rating: '4.5',
    image_address:
      'https://images.weserv.nl/?url=/img2.doubanio.com/view/subject/s/public/s29873722.jpg',
    label: '随笔',
    menu: '\n        PART1 人事万端\n        实行的悲哀\n        生机\n        晨梦\n        忆儿时\n        梦痕\n        大帐簿\n        送考\n        白象\n        PART2 惜缘惜福\n        疗养院记\n        湖畔夜饮\n        缘\n        一饭之恩\n        比较\n        小白之死\n        家\n        PART3人间有情\n        春\n        秋\n  ',
    original_title: null,
    pages: null,
    press: '天地出版社',
    price: '49.80元',
    pubdate: '2018-10',
    rating: '9.1 ',
    rating_number: '128',
    series: '丰子恺散文漫画精品集“珍重此生”系列',
    series_link: 'https://book.douban.com/series/43797',
    translator: '无',
    translator_introduction: '无'
  },
  {
    ISBN: '9787542623003',
    author: '汉斯·约纳斯',
    author_introduction: null,
    binding: '平装',
    book_link: 'https://book.douban.com/subject/1827054/',
    book_subtitle: '异乡神的信息与基督教的开端',
    book_title: '诺斯替宗教',
    collection_time: '2023-10-24',
    content_validity:
      '\n    本书研究和论述了异乡神的信息与基督教的开端——诺斯替宗教的一些哲学性内容。全书包括三个部分：诺斯替文献——主要教义与象征性语言，诺斯替体系，诺斯替主义与古典精神。',
    db_id: '1827054',
    half_rating: '4.6',
    image_address:
      'https://images.weserv.nl/?url=/img2.doubanio.com/view/subject/s/public/s2182433.jpg',
    label: '宗教',
    menu: '\n        中译木导读\n        初版前言\n        再版前言\n        第三次印刷按语\n        第一章　导论：希腊文化的东方与西方\n        第一部分　诺斯替文献——主要教义与象征性语言\n        第二章　诺斯的含义与诺斯替运动的范围\n        第三章　诺斯替意象与象征性语言\n        第二部分　诺斯替思想体系\n        第四章　西门·马古\n        第五章　《珍珠之歌》\n        第六章　创造世界的天使；《马克安福音》\n    ',
    original_title: 'The Gnostic Religion',
    pages: '346',
    press: '\n      上海三联书店\n    ',
    price: '39.00元',
    pubdate: '2006-6',
    rating: '9.2 ',
    rating_number: '656',
    series: '上海三联人文经典书库',
    series_link: 'https://book.douban.com/series/865',
    translator: '张新樟',
    translator_introduction: '无'
  },
  {
    ISBN: '9787559860743',
    author: '(瑞典) 妮娜·波顿',
    author_introduction:
      '\n    作者：妮娜•波顿（Nina Burton），瑞典皇家科学院文学协会成员，斯德哥尔摩KTH皇家理工学院客座诗人。2016年出版专著《古腾堡星系新星》（The Gutenberg Galaxy Nova），获得2016年瑞典国内最高文学奖——奥古斯特文学奖。    译者：薛荷仙，语言学博士、副教授。主要从事外语教学，研究领域为英汉语言对比分析和中国优秀传统文化国际传播。',
    binding: '精装',
    book_link: 'https://book.douban.com/subject/36432214/',
    book_subtitle: '一场跨越物种的生命对话',
    book_title: '夏日木屋札记',
    collection_time: '2023-09-20',
    content_validity:
      '\n    继《鳗鱼的旅行》之后备受瞩目的自然文学作品，一次奇妙又有趣的瑞典乡间木屋避暑之旅，一段与不同物种邂逅、互动的美妙时光。    瑞典奥古斯特文学奖获得者妮娜•波顿全新力作，一位文学家兼生物学家眼中的生命百态和物种进化史。    【内容简介】    一本诞生于瑞典夏季小木屋的优雅小品，一次奇妙又有趣的乡间避暑之旅。    瑞典奥古斯特文学奖获得者妮娜•波顿全新力作，讲述了作者在母亲的乡间木屋度假时，与周围世界的小生物邂逅、互动的奇妙经历。飞蚁共舞其实是一场盛大的“婚礼”？看似讨厌的乌鸦其实聪明可爱又',
    db_id: '36432214',
    half_rating: '4.2',
    image_address:
      'https://images.weserv.nl/?url=/img1.doubanio.com/view/subject/s/public/s34570339.jpg',
    label: '随笔',
    menu: '\n        *辑一 小屋秘密初探\n        蓝色的屋顶 3\n        初遇松鼠 7\n        鸣声四起 14\n        与松鼠、蓝山雀为邻 24\n        鸟儿的迁徙 30\n        鸟儿的歌声 41\n        晚餐时的不速之客 49\n        *辑二 门外翅声不停\n        忙碌的昆虫 55\n        被遗弃的蜂巢 60\n        熊蜂与红梅森蜂 66\n        蜂巢、蜂蜜——合作的结晶 76\n        蜜蜂的语言 83',
    original_title: null,
    pages: '324',
    press: '广西师范大学出版社',
    price: '78',
    pubdate: '2023-7',
    rating: '8.5 ',
    rating_number: '108',
    series: '自由大地丛书',
    series_link: 'https://book.douban.com/series/47248',
    translator:
      '薛荷仙\n        \n           /\n            \n            刘羿\n        \n           /\n            \n            陈薇宇',
    translator_introduction: '无'
  }
]
</script>

<style lang="scss" scoped>
.book_list {
  margin-top: 20px;
  display: flex;
  // justify-content: center;
  // align-items: center;
  height: 390px;
}
.box-card {
  display: flex;
  justify-content: center;
  align-items: center;
}
.book_title {
  margin-top: 10px;
  margin-left: 35px;
  display: flex;
  justify-content: center;
  // align-items: center;
}
.pagination-block {
  margin-top: 20px;
  margin-left: 38vw;
  // justify-content: center;
  // align-items: center;
}
</style>
