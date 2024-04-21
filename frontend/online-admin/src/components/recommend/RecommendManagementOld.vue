<template>
  <router-view></router-view>
  <div v-show="flag">
    <div v-for="book in tableData()" :key="book.db_id" id="booklist" style="margin-top: 10px">
      <el-row>
        <el-col :span="3">
          <div>
            <el-card
              class="box-card"
              style="height: 280px; width: 200px; border: 0px; cursor: pointer"
              @click="push_router(book.book_id)"
              shadow="hover"
            >
              <div v-if="book.image_address">
                <img :src="book.image_address" style="width: 155px" id="image" />
              </div>
              <div v-else id="image_title">
                <div style="text-align: center; font-weight: 500">
                  {{ book.book_title }}
                </div>
              </div>
            </el-card>
          </div>
        </el-col>
        <el-col :span="12" style="margin-left: 15px">
          <el-row style="margin-top: 20px">
            <div @click="push_router(book.book_id)" style="cursor: pointer">
              <h1>
                <span id="booktitle">
                  {{ book.book_title }}
                </span>
              </h1>
            </div>
          </el-row>
          <el-row>
            <el-col :span="23" id="bookcontent">
              <div>
                <h1>
                  {{ book.content_validity }}
                </h1>
              </div>
            </el-col>
          </el-row>
        </el-col>
        <el-col :span="4" id="bookinfo">
          <div id="info">
            <div v-if="book.author">
              <span class="pl">作者：</span>
              <a>{{ book.author }}</a>
              <br />
            </div>
            <div v-if="book.press">
              <div v-if="book.press != '    '">
                <span class="pl">出版社：</span>
                <a>{{ book.press }}</a>
                <br />
              </div>
            </div>
            <div v-if="book.book_subtitle">
              <span class="pl">副标题：</span>
              <a>{{ book.book_subtitle }}</a>
              <br />
            </div>
            <div v-if="book.original_title">
              <span class="pl">原作名：</span>
              <a>{{ book.original_title }}</a>
              <br />
            </div>
            <div v-if="book.translator">
              <span class="pl">译者：</span>
              <a>{{ book.translator }}</a>
              <br />
            </div>
            <div v-if="book.pubdate">
              <span class="pl">出版年：</span>
              <a>{{ book.pubdate }}</a>
              <br />
            </div>
            <div v-if="book.pages">
              <span class="pl">页数：</span>
              <a>{{ book.pages }}</a>
              <br />
            </div>
            <div v-if="book.price">
              <span class="pl">定价：</span>
              <a>{{ book.price }}</a>
              <br />
            </div>
            <div v-if="book.binding">
              <span class="pl">装帧：</span>
              <a>{{ book.binding }}</a>
              <br />
            </div>
            <div v-if="book.series">
              <span class="pl">丛书：</span>
              <a>{{ book.series }}</a>
              <br />
            </div>
            <div v-if="book.ISBN">
              <span class="pl">ISBN： </span>
              <a>{{ book.ISBN }}</a>
              <br />
            </div>
          </div>
        </el-col>
        <el-col :span="4" id="bookrating">
          <div id="interest_sectl">
            <div v-if="book.rating > 0">
              <div class="rating_wrap">
                <div class="rating_logo">推荐指数</div>
                <div class="rating_self clearfix">
                  <strong class="rating_num" property="v:average">
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
                      <!-- <a :href="book.book_link + /comments/" class="rating_people">
                      {{ book.rating_number }}人评价
                    </a> -->
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div v-else>
              <div class="rating_wrap">
                <div class="rating_logo">推荐指数</div>
                <div class="rating_self clearfix">
                  <strong class="rating_num" property="v:average">{{ fakerating }}</strong>
                  <div class="star">
                    <el-rate
                      :v-model="fakerating"
                      text-color="#ff9900"
                      allow-half
                      disabled
                      score-template="{value} points"
                    />
                  </div>
                  <div class="rating_right">
                    <div class="rating_sum">
                      <!-- <a :href="book.book_link + /comments/" class="rating_people">
                      {{ book.rating_number }}人评价
                    </a> -->
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="pagination-block" v-show="tableData().length > 0">
      <!-- <div class="example-demonstration">分页</div> -->
      <el-pagination
        background
        :page-sizes="[5, 10]"
        :page-size="5"
        layout="prev, pager, next"
        :total="state.total"
        @current-change="handleCurrentChange"
        @size-change="handleSizeChange"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { toRefs, reactive, ref, defineExpose, onMounted, watch } from 'vue'
import { BookData, getBookInfoAPI } from '@/apis/books'
import { useRouter } from 'vue-router'

const fakerating = ref(3)

const message = ref()
const router = useRouter()
const books = ref()

let flag = true

function change_flag(x) {
  flag = x
}

// 使用watch监听路由，让flag发声变化，当路由变为booksearchinfo时，flag变为false，此时不显示搜索框。当路由变为booksearch时，flag变为true，此时显示搜索框
watch(
  () => router.currentRoute.value.name,
  (to, from) => {
    if (to === 'recommendinfo') {
      change_flag(false)
    } else if (to === 'recommend') {
      change_flag(true)
    }
  }
)

// 调用getBookInfoAPI获取数据

const get_book_info = async () => {
  const res = await getBookInfoAPI()
  console.log(res.book_list)
  books.value = res.book_list
  state.total = res.book_list.length
  message.value = res.book_list
}

const state = reactive({
  page: 1,
  limit: 5,
  //   total: message.value.length
  total: 0
})

const tableData = () => {
  if (message.value) {
    return message.value.filter(
      (item, index) => index < state.page * state.limit && index >= state.limit * (state.page - 1)
    )
  } else return []
}

const handleCurrentChange = (e) => {
  state.page = e
}
//改变页数限制
const handleSizeChange = (e) => {
  state.limit = e
}

// 把getBookInfoAPI的结果赋值给books
// const books = get_book_info()

onMounted(() => {
  get_book_info()
})

// const temp_data = get_book_info()

// const books = [
//   {
//     id: '1',
//     cover: 'https://i.loli.net/2019/04/10/5cada7e73d601.jpg',
//     title: '三体',
//     author: '刘慈欣',
//     date: '2019-05-05',
//     press: '重庆出版社',
//     abs: '文化大革命如火如荼进行的同时。军方探寻外星文明的绝秘计划“红岸工程”取得了突破性进展。但在按下发射键的那一刻，历经劫难的叶文洁没有意识到，她彻底改变了人类的命运。地球文明向宇宙发出的第一声啼鸣，以太阳为中心，以光速向宇宙深处飞驰……'
//   }
// ]

// function push_router(book_id) {
//   console.log(book_id)
//   router.push({
//     name: 'bookinfo',
//     params: {
//       book_id: JSON.stringify(book_id)
//     }
//   })
// }

function push_router(book_id) {
  console.log(book_id)
  router.push({
    name: 'recommendinfo',
    query: {
      book_id: JSON.stringify(book_id)
    }
  })
}

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
#image_title {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  width: 110px;
  height: 162px;
  background-color: #e7e5e5;
  font-size: 15px;
  font-weight: 600;
  color: #29455b;
}
.book_list {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
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
