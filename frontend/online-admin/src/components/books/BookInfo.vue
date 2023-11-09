<template>
  <div v-for="book in books" :key="book.db_id">
    <el-row>
      <el-col>
        <h1 id="title">
          <span style="font-weight: bold">
            {{ book.book_title }}
          </span>
        </h1>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="4">
        <div id="cover">
          <img :src="book.image_address" alt="封面" style="max-width: 155px" />
        </div>
      </el-col>
      <el-col :span="12">
        <div id="info">
          <span class="pl">作者：</span>
          <a>{{ book.author }}</a>
          <br />
          <span class="pl">出版社：</span>
          <a>{{ book.press }}</a>
          <br />
          <span class="pl">出版年：</span>
          <a>{{ book.pubdate }}</a>
          <br />
          <span class="pl">页数：</span>
          <a>{{ book.pages }}</a>
          <br />
          <span class="pl">定价：</span>
          <a>{{ book.price }}</a>
          <br />
          <span class="pl">装帧：</span>
          <a>{{ book.binding }}</a>
          <br />
          <span class="pl">丛书：</span>
          <a>{{ book.series }}</a>
          <br />
          <span class="pl">ISBN： </span>
          <a>{{ book.ISBN }}</a>
          <br />
        </div>
      </el-col>
      <el-col :span="4">
        <div id="interest_sectl">
          <div class="rating_wrap">
            <div class="rating_logo">豆瓣评分</div>
            <div class="rating_self clearfix">
              <strong class="ll rating_num" property="v:average">
                {{ book.rating }}
              </strong>
              <div class="star">
                <el-rate
                  v-model="book.half_rating"
                  text-color="#ff9900"
                  allow-half
                  disabled
                  score-template="{value} points"
                />
              </div>
              <div class="rating_right">
                <div class="rating_sum">
                  <a :href="book.book_link + /comments/" class="rating_people">
                    {{ book.rating_number }}人评价
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col>
        <div class="related_info">
          <h2 style="color: #007722">
            <span>内容简介</span>
            &nbsp;·&nbsp;·&nbsp;·&nbsp;·&nbsp;·&nbsp;·
          </h2>
          <div class="indent" id="link-report">
            <div class="intro">
              <p>{{ book.content_validity }}</p>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row> </el-row>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const books = [
  {
    ISBN: '9787501018598',
    author: '张静',
    author_introduction:
      '\n    张静，一九五七年生于辽宁沈阳，一九八二年毕业于吉林大学历史系，获学士学位。同年，进入中国社会科学院考古研究所编辑室工作。现任考古杂志社专刊编辑部丰任、编审。主要从书考古书刊的编辑工作。先后编辑田野考古报告、考古论文集、考古专著等二十余部，撰写唐宋金银器的相关文章数篇。    齐东方，一九五六年生于辽宁昌图。一几八二年毕业于占林大学历史系，获学士学位。一几八四年获北京大学考古系硕士学位，并留校任教，一九九二年获该校博士学位。现任北京大学考古文博学院教授、博士生导师。主要从事汉唐时期考占、历史、文物',
    binding: '平装',
    book_link: 'https://book.douban.com/subject/3086383/',
    book_subtitle: null,
    book_title: '古代金银器',
    collection_time: '2023-09-15',
    content_validity:
      '\n    《古代金银器》以时代为序，详细论述了近百年来我国考古发现的大量金银器，对其所反映的各个历史时期金银器的风格特点、制作工艺等进行了相对深入的分析，为今后的相关研究提供了翔实的资料。书中配彩图8幅、插图43幅。《20世纪中国文物考古发现与研究丛书》是一套学科发展史和学术研究史丛书。其内容包括对20世纪考古与文物工作概况的综合阐述；对一些重要的考古学文化和古代区域文化研究情况的叙述；对文物考古的专题研究；对重要的文物考古发现、发掘及研究的个例纪实。',
    db_id: '3086383',
    image_address:
      'https://images.weserv.nl/?url=/img2.doubanio.com/view/subject/s/public/s5901791.jpg',
    label: '艺术史',
    menu: '\n        引言\n        一  夏商周金银器\n        (一)附属饰物及首饰\n        (二)大型饰件与熔金铸器\n        (三)金银器独自发展与原料的来源\n        (四)金银与多种工艺的结合\n        (五)金银器皿与货币的出现\n        (六)周边地区的金银器及文化交融\n        二  秦汉三国两晋南北朝金银器\n        (一)大型器皿与金银的灵异之说\n        (二)黄金冶炼与“西汉巨额黄金消失之谜”\n        (三)装饰器',
    original_title: null,
    pages: '221',
    press: '\n      文物出版社\n    ',
    price: '28.00元',
    pubdate: '2008-3',
    rating: '8.5',
    half_rating: '4.3',
    rating_number: '13',
    series: '二十世纪中国文物考古发现与研究丛书',
    series_link: 'https://book.douban.com/series/80',
    translator: '无',
    translator_introduction: '无'
  },
  {
    ISBN: '9787208182509',
    author: '[新西兰]蒂莫西·辛克莱（Timothy J. Sinclair）',
    author_introduction:
      '\n    蒂莫西·辛克莱（1963—2022年），华威大学国际政治经济学副教授，博士毕业于约克大学。主要研究领域为全球货币和金融政治经济学。他对信用评级机构的开创性研究，有助于外界对金融市场中的权力运作的理解。他的著作还包括《资本的新大师：美国债券评级机构和信誉政治》。    译者简介    张文韬，常驻中国香港，长期供职于国际信用评级领域。十余年间，曾任多个国际信用评级相关的全球性职务，并致力于对新兴经济体的市场准入和战略规划相关工作。除此之外，对国际金融和国际评级监管有长期研究。    郭茁芊，常驻北',
    binding: '平装',
    book_link: 'https://book.douban.com/subject/36392892/',
    book_subtitle: '美国的评级机构与金融危机',
    book_title: '崩溃边缘',
    collection_time: '2023-09-19',
    content_validity:
      '\n    ·信用评级机构在金融危机中究竟扮演了怎样的角色？    ·它们是“恶棍”还是“替罪羊”？    ·它们是如何推倒金融危机爆发的多米诺骨牌的？    ·华威大学副教授蒂莫西·辛克莱在《崩溃边缘：美国的评级机构与金融危机》一书中揭示了信用评级机构背后的阴暗面，让读者得以了解金融危机中信用评级机构的问责机制失效的来龙去脉。    美国的信用评级机构在金融危机中究竟扮演了怎样的角色？危机过后，评级机构又为何能用和金融危机前几乎一样的业务模式继续发展？通过对业内人士的深入访谈、对美国国会听证会的精心调查，',
    db_id: '36392892',
    image_address:
      'https://images.weserv.nl/?url=/img9.doubanio.com/view/subject/s/public/s34596205.jpg',
    label: '金融',
    menu: '\n        推荐序\n        译者序\n        序言\n        第一章 简介\n        2008年金融危机影响的深度和广度惊人，而各方也都在指摘评级机构，批判它们是金融危机的始作俑者之一，还让危机引发的巨大波澜雪上加霜。但既然如此，评级机构何以仍若无其事地存在着？\n        ◇ 后果\n        ◇ 糟糕、糟糕、糟糕\n        ◇ 一个不同的视角\n        ◇ 评级机构的“贡献”\n        ◇ 三个谜团\n        ◇ 两个论点\n       ',
    original_title: 'To the Brink of Destruction：America’s Rating Agencies and Financial Crisis',
    pages: '199',
    press: '上海人民出版社',
    price: '68.00元',
    pubdate: '2023-6-30',
    rating: 0,
    rating_number: '0',
    series: '无',
    series_link: '无',
    translator: '张文韬\n        \n           /\n            \n            郭茁芊',
    translator_introduction: '无'
  }
]
</script>

<style lang="scss" scoped>
#title {
  font-size: 26px;
  word-wrap: break-word;
  display: block;
  font-weight: bold;
  color: #494949;
  padding: 0 0 15px 0;
  line-height: 1.1;
}
#cover {
  float: left;
  text-align: center;
  margin: 3px 12px 0 0;
  overflow: hidden;
}
#info {
  margin-top: 10px;
  font-size: 13px;
  line-height: 1.5;
  .pl {
    color: #666666;
    line-height: 150%;
    font-size: 13px;
  }
}
#interest_sectl {
  float: left;
  width: 155px;
  margin: 2px 0 0 0;
  padding: 0 0 0 15px;
  border-left: 1px solid #eaeaea;
  color: #9b9b9b;
  .rating_wrap {
    padding-bottom: 15px;
    font-size: 12px;
    line-height: 14px;
  }
  .rating_logo {
    line-height: 1;
  }
  .rating_right {
    float: left;
    padding: 10px 0 10px 6px;
  }
  .rating_self {
    padding: 0;
    line-height: 2;
  }
  .rating_num {
    color: #494949;
    padding: 0;
    min-width: 30%;
    font-size: 28px;
  }
}
.indent {
  word-break: normal;
  word-wrap: break-word;
}
.clearfix {
  display: block;
  zoom: 1;
}
.ll {
  float: left;
}
</style>
