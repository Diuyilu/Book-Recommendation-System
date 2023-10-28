<template>
  <div>
    <el-row style="height: 40px">
      <!--<search-bar></search-bar>-->
      <el-tooltip effect="dark" placement="right" v-for="item in message" :key="item.id">
        <template #content>
          <p style="font-size: 14px; margin-bottom: 6px">{{ item.book_title }}</p>
          <p style="font-size: 13px; margin-bottom: 6px">
            <span>{{ item.author }}</span> / <span>{{ item.collection_time }}</span> /
            <span>{{ item.press }}</span>
          </p>
          <p style="width: 300px" class="abstract">{{ item.content_validity }} ……</p>
        </template>
        <el-card style="width: 135px; margin-bottom: 20px; height: 233px; float: left; margin-right: 15px" class="book"
          bodyStyle="padding:10px" shadow="hover">
          <div class="cover">
            <img :src="item.image_address" alt="封面" />
          </div>
          <div class="info">
            <div class="title">
              <a :href="item.book_link" target="_Blank">{{ item.book_title }}</a>
            </div>
          </div>
          <div class="author">{{ item.author }}</div>
        </el-card>
      </el-tooltip>
    </el-row>
    <el-row>
      <el-pagination :current-page="1" :page-size="10" :total="20"> </el-pagination>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { toRefs, reactive, ref, defineExpose, onMounted } from 'vue'
import { BookData, getBookInfoAPI } from '@/apis/books'

const message = ref()

// 调用getBookInfoAPI获取数据
const get_book_info = async () => {
  const res = await getBookInfoAPI()
  console.log(res.book_list)
  message.value = res.book_list
}

// 把getBookInfoAPI的结果赋值给books
// const books = get_book_info()

onMounted(() => {
  get_book_info()
})

// const temp_data = get_book_info()




const books = [
  {
    id: '1',
    cover: 'https://i.loli.net/2019/04/10/5cada7e73d601.jpg',
    title: '三体',
    author: '刘慈欣',
    date: '2019-05-05',
    press: '重庆出版社',
    abs: '文化大革命如火如荼进行的同时。军方探寻外星文明的绝秘计划“红岸工程”取得了突破性进展。但在按下发射键的那一刻，历经劫难的叶文洁没有意识到，她彻底改变了人类的命运。地球文明向宇宙发出的第一声啼鸣，以太阳为中心，以光速向宇宙深处飞驰……'
  }
]

defineExpose({
  name: 'Books',
  data: () => ({ books })
})

// export default {
//   // name: 'Books',
//   setup() {
//     const books = ref([
//       {
//         id: '1',
//         cover: 'https://i.loli.net/2019/04/10/5cada7e73d601.jpg',
//         title: '三体',
//         author: '刘慈欣',
//         date: '2019-05-05',
//         press: '重庆出版社',
//         abs: '文化大革命如火如荼进行的同时。军方探寻外星文明的绝秘计划“红岸工程”取得了突破性进展。但在按下发射键的那一刻，历经劫难的叶文洁没有意识到，她彻底改变了人类的命运。地球文明向宇宙发出的第一声啼鸣，以太阳为中心，以光速向宇宙深处飞驰……'
//       }
//     ])

//     return { books }
//   }
// }
</script>

<style lang="scss" scoped>
.cover {
  width: 115px;
  height: 172px;
  margin-bottom: 7px;
  overflow: hidden;
  cursor: pointer;
}

img {
  width: 115px;
  height: 172px;
  /*margin: 0 auto;*/
}

.title {
  font-size: 14px;
  text-align: left;
}

.author {
  color: #333;
  width: 102px;
  font-size: 13px;
  margin-bottom: 6px;
  text-align: left;
}

.abstract {
  display: block;
  line-height: 17px;
}

a {
  text-decoration: none;
}

a:link,
a:visited,
a:focus {
  color: #3377aa;
}
</style>
@/apis/books
