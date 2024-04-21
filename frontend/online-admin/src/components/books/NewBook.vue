<template>
  <router-view></router-view>
  <div v-show="flag">
    <div v-for="book in tableData()" :key="book.book_id" id="booklist" style="margin-top: 10px">
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
        <el-col :span="16" style="margin-left: 15px">
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
            <div v-if="book.pubyear">
              <span class="pl">出版年：</span>
              <a>{{ book.pubyear }}</a>
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
import { ref, onMounted, watch, reactive } from 'vue'
import { getNewBookInfoAPI } from '@/apis/books'
import { useRouter } from 'vue-router'

const books = ref()
const get_new_book_info = async () => {
  const res = await getNewBookInfoAPI()
  console.log(res.book_list)
  books.value = res.book_list
  state.total = res.book_list.length
  message.value = res.book_list
}

const router = useRouter()

let flag = true

function push_router(b_id) {
  const book_id = b_id
  console.log(book_id)
  router.push({
    name: 'newbookinfo',
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
    if (to === 'newbookinfo') {
      change_flag(false)
    } else if (to === 'newbook') {
      change_flag(true)
    }
  }
)

const state = reactive({
  page: 1,
  limit: 5,
  //   total: message.value.length
  total: 0
})

const message = ref()

//前端限制分页（tableData为当前展示页表格）
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

onMounted(() => {
  console.log('yesyesyes!')
  get_new_book_info()
})
</script>

<style lang="scss" scoped>
#booklist {
  margin-bottom: 50px;
}
.box-card {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
}
#image {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  width: 155px;
}
#image_title {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  width: 155px;
  height: 200px;
  background-color: #e7e5e5;
  font-size: 20px;
  font-weight: 600;
  color: #29455b;
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
a {
  font-size: 13px;
}
.pagination-block {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
