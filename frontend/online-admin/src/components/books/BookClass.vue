<template>
  <RouterView></RouterView>
  <div v-show="flag">
    <el-row id="label" style="margin-bottom: 20px">
      <el-col v-for="item in booklist" :key="item.label" :span="2">
        <div>
          <el-button id="labeltxt" @click="change_label(item.label)">
            {{ item.label }}
          </el-button>
        </div>
      </el-col>
    </el-row>
    <div v-for="item in booklist" :key="item.label">
      <div v-show="page_label === item.label" :key="1">
        <ul v-if="Array.isArray(item.book_list)">
          <div v-for="book in item.book_list" :key="book.db_id" id="booklist">
            <el-row>
              <el-col :span="3">
                <div>
                  <el-card
                    class="box-card"
                    style="max-width: 200px; cursor: pointer"
                    @click="push_router(book.db_id)"
                  >
                    <img :src="book.image_address" style="max-width: 155px" id="image" />
                  </el-card>
                </div>
              </el-col>
              <el-col :span="16" style="margin-left: 15px">
                <el-row style="margin-top: 20px">
                  <div @click="push_router(book.db_id)" style="cursor: pointer">
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
                    <span class="pl">出版社：</span>
                    <a>{{ book.press }}</a>
                    <br />
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
            </el-row>
          </div>
        </ul>
        <div v-else>Loading...</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, reactive, watch } from 'vue'
import { getBookLabelAPI, getBookByLabelAPI } from '@/apis/books'
import { useRouter } from 'vue-router'

const router = useRouter()
const labels = ['小说', '文学', '经典', '诗歌', '童话']
const booklist = reactive([])
let page_label = '小说'
let flag = true

const get_book_by_label = async (label) => {
  const params = { label: label }
  const res = await getBookByLabelAPI(params)
  // console.log(res.book_list)
  return res.book_list
}

const change_label = async (label) => {
  page_label = label
  console.log('当前标签:' + page_label)
  const book_list = await get_book_by_label(label)
  const index = booklist.findIndex((item) => item.label === label)
  if (index !== -1) {
    booklist[index].book_list = book_list
  }
}

function change_flag(x) {
  flag = x
}

function push_router(db_id) {
  const book_id = db_id
  console.log(book_id)
  router.push({
    name: 'bookclassinfo',
    query: {
      book_id: JSON.stringify(book_id)
    }
  })
}

watch(
  () => page_label,
  (to, from) => {
    get_book_by_label(to)
  }
)

watch(
  () => router.currentRoute.value.name,
  (to, from) => {
    if (to === 'bookclassinfo') {
      change_flag(false)
    } else if (to === 'bookclass') {
      change_flag(true)
    }
  }
)

onMounted(async () => {
  for (const label of labels) {
    const book_list = await get_book_by_label(label)
    booklist.push({
      label: label,
      book_list: book_list
    })
  }
})
</script>

<style lang="scss" scoped>
#label {
  display: flex;
  // 设置水平居中
  justify-content: center;
}
#labeltxt {
  // background-color: #f5f5f5;
  // border: none;
  // color: #000000;
  font-size: 16px;
  font-weight: 500;
  padding: 0 20px;
  // border-radius: 0;
  height: 40px;
  line-height: 40px;
  margin: 0 10px;
  cursor: pointer;
  &:hover {
    background-color: #e6e6e6;
  }
}
#booklist {
  margin-bottom: 50px;
}
#image {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
}
#booktitle {
  font-size: 30px;
  font-weight: 600;
  color: #29455b;
  justify-content: center; /* 水平居中 */
}
#bookcontent {
  display: flex;
  align-items: center;
  line-height: 2;
  margin-top: 10px;
}
#bookinfo {
  display: flex;
  align-items: center;
  margin-top: 10px;
}
.pl {
  color: #666666;
  line-height: 150%;
  font-size: 13px;
}
</style>
